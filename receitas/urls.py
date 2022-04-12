from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('sobre/', views.sobre),
    path('contato/', views.contato),
]