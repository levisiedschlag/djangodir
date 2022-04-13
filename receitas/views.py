import imp
from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes import factory

# Create your views here.
def index(request):
    contexto = {
        'recipes': [factory.make_recipe() for _ in range(10)],
    }
    return render(request, 'receitas/pages/home.html', contexto)

def recipe(request, id):
    contexto = {
        'recipe':factory.make_recipe(),
        'is_detail_page': True
    }
    return render(request, 'receitas/pages/recipe-view.html', contexto)
