from django import views
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='recipes-home'),
    path('recipes/category/<int:id>/', views.category, name='recipes-category'),
    path('recipes/<int:id>/', views.recipe, name='recipes-recipe'),
    
]
