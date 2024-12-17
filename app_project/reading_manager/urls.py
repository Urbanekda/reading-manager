from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include

#Define a list of URL patterns

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("book/add", views.add_book, name="add_book"),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    path("edit/<int:pk>", views.edit_book, name="edit_page"),
    path("book/<int:pk>", views.view_book, name="book_profile"), 
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html', next_page="index"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),


]