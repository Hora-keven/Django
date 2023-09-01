
from rest_framework import routers, serializers, viewsets
from .models import Pessoas
# Serializers define the API representation.
class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = ['id', 'nome', 'idade']