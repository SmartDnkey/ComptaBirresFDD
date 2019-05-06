from rest_framework import serializers, viewsets

from ComptaBirres.models import Birra, Edicio
from datetime import date

class BirresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Birra
        fields = ('tirador', 'timestamp')

class BirresViewSet(viewsets.ModelViewSet):

    edicio = Edicio.objects.get(edicio=date.today().year)

    queryset = Birra.objects.filter(edicio=edicio)
    serializer_class = BirresSerializer