from django_filters import rest_framework as filters, ModelMultipleChoiceFilter
from .models import Match, Profile, Team

class CharFIlterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class MatchsFilter(filters.FilterSet):
    game = CharFIlterInFilter(field_name='game__title', lookup_expr='in')
    league = CharFIlterInFilter(field_name='league__league', lookup_expr='in')

    class Meta:
        model = Match
        fields = ['game', 'league']

class ProfilesFilter(filters.FilterSet):
    game = CharFIlterInFilter(field_name='game__title', lookup_expr='in')
    league = CharFIlterInFilter(field_name='league__league', lookup_expr='in')
    team = CharFIlterInFilter(field_name='team__title', lookup_expr='in')

    class Meta:
        model = Profile
        fields = ['game', 'league', 'team']

class TeamsFilter(filters.FilterSet):
    games = CharFIlterInFilter(field_name='games__title', lookup_expr='in')
    league = CharFIlterInFilter(field_name='league__league', lookup_expr='in')

    class Meta:
        model = Team
        fields = ['games', 'league']