from django.contrib import admin
from .models import Game, Profile, Status, Team, Match, League, News, ApplicationForProfile, ApplicationForTraining
from django. utils. html import format_html

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
    search_fields = ['title']

admin.site.register(League)
admin.site.register(Status)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname', 'status', 'user', 'game', 'league')
    search_fields = ('nickname', 'user')
    list_filter = ('status', 'game', 'league')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ['title']
    list_display_links = ['title']

admin.site.register(Match)
admin.site.register(News)
admin.site.register(ApplicationForProfile)
admin.site.register(ApplicationForTraining)
