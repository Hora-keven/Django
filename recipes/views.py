from django.shortcuts import render
from django.http import HttpResponse

def contato(request):
    return render(request, 'home.html', context={
        'name':'Keven da Hora'})

def myview(request):
   return HttpResponse("Keven o mais lindo!")

def sobre(request):
    return HttpResponse('SOBRE')
