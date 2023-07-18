
from django.urls import path
from django.http import HttpResponse
from recipes.views import contato, myview, sobre

urlpatterns = [
    path('', myview),
    path('sobre/', sobre),
    path('contato/', contato),
]
