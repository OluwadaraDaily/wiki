from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entryPage, name="entry_page"),
    path("search", views.search, name="search"),
    path("create_new_page", views.createNewPage, name="create_new_page"),
    path("edit_page/<str:title>", views.editPage, name="edit_page"),
    path("random_page", views.randomPage, name="random_page")
]
