from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from . models import Pessoas
from .serializers import PessoasSerializer
# Create your views here.
class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer

