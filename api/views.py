from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .models import Game, Profile, Team, Match
from .service import MatchsFilter


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer

class GameDetail(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer

class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer

class TeamDetail(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = serializers.TeamSerializer

class MatchList(generics.ListAPIView):
    """ Фильтр """
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MatchsFilter
    """ ___________________________________ """

    queryset = Match.objects.all()
    serializer_class = serializers.MatchSerializer

class MatchDetail(generics.RetrieveAPIView):
    queryset = Match.objects.all()
    serializer_class = serializers.MatchSerializer
