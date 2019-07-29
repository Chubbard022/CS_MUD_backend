from rest_framework import serializers, viewsets
from .models import Room

#which model we want to expose
class RoomSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Room
        fields = ('name',)


#what rows to we want to show within the model

class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()