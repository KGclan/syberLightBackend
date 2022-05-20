from django.contrib import admin
from .models import Game, Profile, Status, Team, Match, League, News


admin.site.register(Game)
admin.site.register(League)
admin.site.register(Status)
admin.site.register(Profile)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(News)
