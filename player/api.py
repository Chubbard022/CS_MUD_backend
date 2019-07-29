from rest_framework import serializers, viewsets
from .models import Player

#which model we want to expose
class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ()


#what rows to we want to show within the model

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()