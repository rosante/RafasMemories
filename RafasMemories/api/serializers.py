from rest_framework import routers, serializers, viewsets
from .models import Memoria

class MemoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memoria
        fields = ('id', 'nome', 'descricao', 'datacriacao', 'alerta', 'dataevento')