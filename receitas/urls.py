from django import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='recipes-home'),
    path('recipes/<int:id>/', views.recipe, name='recipes-recipe'),
]