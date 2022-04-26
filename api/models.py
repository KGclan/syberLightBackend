from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model): 
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=50, blank=False, verbose_name='Название для запроса')
    title = models.CharField(max_length=100, blank=False, verbose_name='Название')
    description = models.TextField(blank=False, verbose_name='Описание')
    logo = models.ImageField(verbose_name='Логотип')

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=15, verbose_name='Ник')
    image = models.ImageField(verbose_name='Аватар')
    about_me = models.TextField(max_length=2000, verbose_name='О себе')
    rating = models.CharField(max_length=30, verbose_name='Рейтинг игрока')

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    game = models.ForeignKey(Game,  on_delete=models.CASCADE, verbose_name='Игра')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль игрока: {self.nickname}'

class Team(models.Model): 
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=False, verbose_name='Название')
    description = models.TextField(blank=False, verbose_name='Описание')
    logo = models.ImageField()
    lose = models.IntegerField(verbose_name='Поражений')
    win = models.IntegerField(verbose_name='Побед')
    
    captain = models.ForeignKey(Profile, verbose_name='Капитан', on_delete=models.CASCADE, related_name='team_captain')
    players = models.ManyToManyField(Profile, verbose_name='Игроки', related_name='team_players')
    games = models.ManyToManyField(Game, verbose_name='Игры')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
    
    def __str__(self):
        return self.title

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')

    teams = models.ManyToManyField(Team, verbose_name='Команды')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'

    def __str__(self):
        return f'Номер: {self.id} Игра: {self.game} Дата: {self.date} Время: {self.time}'







