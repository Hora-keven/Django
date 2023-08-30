from django.shortcuts import render
from urls.recipes.factory import make_recipe

def contato(request):
    return render(request, 'home.html', context={'recipes':[make_recipe() for _ in range(10)]})


def recipe(request, id):
    return render(request, 'recipe_view.html', context={'recipe':make_recipe(), 'is_detail_page':True})