from django.urls import path
from django.contrib import admin
from . import views

#Define a list of URL patterns

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("book/add", views.add_book, name="add_book"),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path("edit/<int:pk>", views.edit_book, name="edit_page"),
    path("book/<int:pk>", views.view_book, name="book_profile"), 
]