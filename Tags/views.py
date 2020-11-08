# from django.shortcuts import render
from rest_framework import viewsets

from .models import Tags, Users
from .serializer import TagsSerializer, UsersSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
