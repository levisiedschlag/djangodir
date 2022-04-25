from django.shortcuts import get_list_or_404, render
from utils.recipes import factory
from receitas import models

# Create your views here.
def index(request):
    recipes = models.Recipe.objects.filter(is_published=True).order_by('-id')
    
    return render(request, 'receitas/pages/home.html', { 'recipes' : recipes })

def category(request, id):
    recipes = get_list_or_404(
        models.Recipe.objects.filter(category__id=id, is_published=True).order_by('-id')
        )
    return render(request, 'receitas/pages/recipe-category.html', { 
            'recipes' : recipes,
            'title': f'{recipes[0].category.name}'
            })

def recipe(request, id):
    recipe = models.Recipe.objects.filter(id=id, is_published=True).first()
    return render(request, 'receitas/pages/recipe-view.html', { 'recipe':recipe, 'is_detail_page': True })
