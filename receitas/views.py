from django.shortcuts import render
from utils.recipes import factory
from receitas import models

# Create your views here.
def index(request):
    recipes = models.Recipe.objects.filter(is_published=True).order_by('-id')
    
    return render(request, 'receitas/pages/home.html', { 'recipes' : recipes })

def category(request, id):
    recipes = models.Recipe.objects.filter(category__id=id, is_published=True).order_by('-id')
    
    return render(request, 'receitas/pages/recipe-category.html', { 'recipes' : recipes })

def recipe(request, id):
    recipe = models.Recipe.objects.filter(id=id)
    return render(request, 'receitas/pages/recipe-view.html', { 'recipe':recipe, 'is_detail_page': True })
