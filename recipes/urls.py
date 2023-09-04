
from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.contato, name='home'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
    path('recipe/category/<int:category_id>/', views.category, name='category')
 
]
