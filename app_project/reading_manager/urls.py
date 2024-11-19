from django.urls import path
from django.contrib import admin
from . import views

#Define a list of URL patterns

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
]