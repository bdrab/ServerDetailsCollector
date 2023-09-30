from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
from . import functions

urlpatterns = [
    path('add', functions.add, name="add"),
]
