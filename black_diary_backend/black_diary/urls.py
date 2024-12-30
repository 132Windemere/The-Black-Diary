from django.contrib import admin
from django.urls import path, include

dark_api = "api/"

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path(dark_api, include("dark_diary.urls")),
]
