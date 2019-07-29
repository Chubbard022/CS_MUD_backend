from rest_framework import serializers, viewsets
from .models import Map

#which model we want to expose
class MapSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Map
        fields = ()


#what rows to we want to show within the model

class MapViewSet(viewsets.ModelViewSet):
    serializer_class = MapSerializer
    queryset = Map.objects.all()