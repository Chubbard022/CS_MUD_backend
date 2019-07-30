from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Room

class RoomType(DjangoObjectType):

    class Meta:
        model = Room
        #this tuple tells graphql that the Room class is a list of Nodes
        interface = (graphene.relay.Node,)

class Query(graphene.ObjectType):
    # will return a list of room types based on the room model
    room = graphene.List(RoomType)

    def resolve_room(self,info):
        return Room.objects().all()

schema = graphene.Schema(query=Query)