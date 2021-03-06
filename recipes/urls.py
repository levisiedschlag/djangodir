from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.home, name='recipes-home'),
    path('recipes/category/<int:id>/', views.category, name='recipes-category'),  # noqa: E501
    path('recipes/<int:id>/', views.recipe, name='recipes-recipe'),
    path('recipes/search/', views.search, name='search-recipe'),
]
