from django.shortcuts import get_list_or_404, get_object_or_404, render

from recipes import models


# Create your views here.
def home(request):
    recipes = models.Recipe.objects.filter(is_published=True,).order_by('-id')

    return render(request, 'recipes/pages/home.html', {'recipes': recipes})


def category(request, id):
    recipes = get_list_or_404(models.Recipe.objects.filter(
        category__id=id, is_published=True).order_by('-id'))
    return render(request, 'recipes/pages/recipe-category.html', {
        'recipes': recipes,
        'title': f'{recipes[0].category.name}'
    })


def recipe(request, id):
    # recipe = models.Recipe.objects.filter(id=id, is_published=True).first()

    recipe = get_object_or_404(models.Recipe, id=id, is_published=True)
    return render(request, 'recipes/pages/recipe-view.html',
                  {'recipe': recipe, 'is_detail_page': True})


def search(request):
    return render(request, '')
