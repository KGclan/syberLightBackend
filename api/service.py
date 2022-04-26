from django_filters import rest_framework as filters
from .models import Match

class CharFIlterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class MatchsFilter(filters.FilterSet):
    game = CharFIlterInFilter(field_name='game__title', lookup_expr='in')

    class Meta:
        model = Match
        fields = ['game']