from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game, Match, Profile, Team, Match


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'slug']

class ProfileSerializer(serializers.ModelSerializer):
    game = GameTitleSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

class NicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['nickname']

class TeamSerializer(serializers.ModelSerializer):
    captain = NicknameSerializer()
    players = NicknameSerializer(many=True)
    games = GameTitleSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'title', 'description', 'logo', 'lose', 'win', 'players', 'games', 'captain']

class MatchSerializer(serializers.ModelSerializer):
    game = GameTitleSerializer()

    class Meta:
        model = Match
        fields = '__all__'