
from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.contato),
    path('recipes/<int:id>/', views.recipe),
]
