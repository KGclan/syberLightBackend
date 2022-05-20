from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Game, League, Match, News, Profile, Status, Team, Match


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = '__all__'

class LeagueTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = League
        fields = ['league']

class StatusTitleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = ['status']

class GameTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['title', 'slug']

class ProfileSerializer(serializers.ModelSerializer):
    game = GameTitleSerializer()
    league = LeagueTitleSerializer()
    team = Team.objects.filter(players__nickname=Profile.nickname)
    team = serializers.StringRelatedField(many=True)
    status = StatusTitleSerializer()

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
    league = LeagueTitleSerializer(many=True)

    class Meta:
        model = Team
        fields = ['id', 'title', 'description', 'league', 'logo', 'lose', 'win', 'players', 'games', 'captain']

class TeamTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['title']

class MatchSerializer(serializers.ModelSerializer):
    game = GameTitleSerializer()
    league = LeagueTitleSerializer()
    teams = TeamTitleSerializer(many=True)

    class Meta:
        model = Match
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'