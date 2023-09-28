from django.shortcuts import render, get_list_or_404
from .models import Recipe


def home(request):
    recipes = Recipe.objects.filter( is_published=True).order_by('-id')
    return render(request, 'home.html', context={'recipes':recipes})


def recipe(request, id):
    recipes = Recipe.objects.filter(pk = id, is_published=True)
    return render(request, 'recipe_view.html', context={'recipe':recipes, 'is_detail_page':True})


def category(request, category_id):
    # recipe = Recipe.objects.filter(category__id = category_id, is_published=True)
    # if not recipe:
    #     #return HttpResponse(content='Not found', status=404)
    #     raise Http404('Not found, please verify the url ')
    recipe = get_list_or_404(
        Recipe.objects.filter(
        category_id=category_id,
        is_published=True
        ).order_by('-id'))
    return render(request, 'category.html', context={'category':recipe})

def search(request):
    dado = request.GET.get('dados')
    
    busca = Recipe.objects.filter(title=dado, is_published=True).order_by('id')
    print(busca)
    return render(request, 'home.html', {'dado':busca})


