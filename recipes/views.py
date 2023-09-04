from django.shortcuts import render
from urls.recipes.factory import make_recipe
from .models import Recipe

def contato(request):
    recipes = Recipe.objects.all( ).order_by('-id')
    return render(request, 'home.html', context={'recipes':recipes})


def recipe(request, id):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_view.html', context={'recipes':recipes, 'is_detail_page':True})


def category(request, category_id):
    category = Recipe.objects.filter(
        is_published=True,
        category__id = category_id)
    return render(request, 'home.html', context={'category':category})
