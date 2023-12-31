
from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe, name='recipe'),
    path('recipes/category/<int:category_id>/', views.category, name='category'),
    path('recipes/search/', views.search, name='search' )
 
]
