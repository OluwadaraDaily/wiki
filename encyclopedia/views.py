from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util
import difflib
import random


def index(request):
	context = {
		"entries": util.list_entries()
	}
	return render(request, "encyclopedia/index.html", context)

def entryPage(request, title):
	try:
		body = util.get_entry(title)
		context = {
			"title": title,
			"body": body
		}
		return render(request, "encyclopedia/entry_page.html", context)
	except:
		context = {
			"message": "Invalid Page Requested"
		}
		return render(request, "encyclopedia/error.html", context)

def search(request):
	if request.method == "POST":
		title = request.POST["search"]
		if(util.get_entry(title) is not None):
			body = util.get_entry(title)
			context = {
				"title": title,
				"body": body
			}
			print("NOT NONE!")
			return render(request, "encyclopedia/entry_page.html", context)
			
		else:
			print("NONE!")
			output = []
			entries = util.list_entries()
			for entry in entries:
				check = difflib.SequenceMatcher(None, entry, title).ratio()
				print(check)
				if(check > 0):
					output.append(entry)
				continue;

			context = {
				"output": output
			}
			return render(request, "encyclopedia/search_results.html", context)
	else:
		return redirect("/")

def createNewPage(request):
	if(request.method == "POST"):
		title = request.POST["page-title"]
		content = request.POST["page-content"]
		entries = util.list_entries()
		for entry in entries:
			if(title == entry):
				context = {
					"message": "Entry already exists! Try Again!"
				}
				return render(request, "encyclopedia/error.html", context)
			continue;
		util.save_entry(title, content)
		body = util.get_entry(title)
		context = {
			"title": title,
			"body" : body
		}
		# return redirect("/")
		return render(request, "encyclopedia/entry_page.html", context)

	return render(request, "encyclopedia/new_page.html")
	# return HttpResponse("Create New Page")

def editPage(request, title):
	if (request.method == "POST"):
		title = request.POST["page-title"]
		content = request.POST["page-content"]
		util.save_entry(title, content)
		body = util.get_entry(title)
		context = {
			"title": title,
			"body": body
		}
		# return redirect("/")
		return render(request, "encyclopedia/entry_page.html", context)
	content = util.get_entry(title)
	context = {
		"title": title,
		"content": content
	}
	return render(request, "encyclopedia/edit_page.html", context)

def randomPage(request):
	entries = util.list_entries()
	L = len(entries)
	n = random.randint(0,L)
	title = entries[n]
	body = util.get_entry(title)
	context = {
		"title": title,
		"body": body
	}
	return render(request, "encyclopedia/entry_page.html", context)
	# return HttpResponse("A Random Page")