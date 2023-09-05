from django.shortcuts import render
from urls.recipes.factory import make_recipe
from .models import Recipe
from django.http import HttpResponse, Http404

def contato(request):
    recipes = Recipe.objects.all( ).order_by('-id')
    return render(request, 'home.html', context={'recipes':recipes})


def recipe(request, id):
    recipes = Recipe.objects.filter(id__icontains = id)
    return render(request, 'recipe_view.html', context={'recipe':recipes, 'is_detail_page':True})


def category(request, category_id):
    recipe = Recipe.objects.filter(category__id = category_id, is_published=True)
    if not recipe:
        #return HttpResponse(content='Not found', status=404)
        raise Http404('Not found, please verify the url ')
    return render(request, 'category.html', context={'category':recipe, 'title':f'{recipe.first().category.name}'})

    recipes = Recipe.objects.all()
    return render(request, 'recipe_view.html', context={'recipes':recipes, 'is_detail_page':True})


def category(request, category_id):
    category = Recipe.objects.filter(
        is_published=True,
        category__id = category_id)
    return render(request, 'home.html', context={'category':category})

