from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('download/', views.download, name="download"),
    path('refresh/', views.refresh, name="refresh"),
    path('logout/', views.user_logout, name="logout"),
    path('login', views.login_user, name="login"),
]