
from django.urls import path
from django.http import HttpResponse
from recipes.views import contato

urlpatterns = [
    path('', contato),
]
