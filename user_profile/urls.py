
from django.contrib import admin
from django.urls import path, include

from user_profile import views

urlpatterns = [
    path("", views.index, name="index"),
]
