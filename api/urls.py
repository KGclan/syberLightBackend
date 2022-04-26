from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),

    path('games/', views.GameList.as_view()),
    path('games/<slug:slug>/', views.GameDetail.as_view()),

    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),

    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail.as_view()),

    path('matchs/', views.MatchList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)