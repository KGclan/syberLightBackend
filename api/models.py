from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

class Game(models.Model): 
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=50, blank=False, verbose_name='Название для запроса')
    title = models.CharField(max_length=100, blank=False, verbose_name='Название')
    description = models.TextField(blank=False, verbose_name='Описание')
    logo = models.ImageField(verbose_name='Логотип')

    def image_tag(self):
        return mark_safe('<img src="/directory/%s" width="auto" height="65px" />' % (self.logo))

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
    
    def __str__(self):
        return self.title

class League(models.Model):
    id = models.AutoField(primary_key=True)
    league = models.CharField(max_length=100, verbose_name='Название лиги')

    class Meta:
        verbose_name = 'Лига'
        verbose_name_plural = 'Лиги'
    
    def __str__(self):
        return self.league

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=100, verbose_name='Название статуса')

    class Meta:
        verbose_name = 'Статус пользователя'
        verbose_name_plural = 'Статусы пользователей'
    
    def __str__(self):
        return self.status

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=15, verbose_name='Ник')
    image = models.ImageField(verbose_name='Аватар')
    about_me = models.TextField(max_length=2000, verbose_name='О себе')
    rating = models.CharField(max_length=30, verbose_name='Рейтинг игрока')
    age = models.IntegerField(verbose_name='Возраст')
    win = models.IntegerField(verbose_name='Победы')
    lose = models.IntegerField(verbose_name='Поражения')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Почта')
    vk = models.CharField(max_length=1000, verbose_name='Ссылка на вк')

    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='Лига')

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
    players = models.ManyToManyField(Profile, verbose_name='Игроки', related_name='team')
    games = models.ManyToManyField(Game, verbose_name='Игры')
    league = models.ManyToManyField(League, verbose_name='Лига')

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
    
    def __str__(self):
        return self.title

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    url = models.CharField(max_length=1000, verbose_name='Ссылка на трансляцию')

    teams = models.ManyToManyField(Team, verbose_name='Команды')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name='Лига')

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'

    def __str__(self):
        return f'Номер: {self.id} Игра: {self.game} Дата: {self.date} Время: {self.time}'

class News(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    body = models.TextField(max_length=3000, verbose_name='Новость')
    image = models.ImageField()

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    
    def __str__(self):
        return self.title

class ApplicationForProfile(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50, verbose_name='Почта')
    logo = models.ImageField(verbose_name='Аватар')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    rating = models.CharField(max_length=30, verbose_name='Рейтинг игрока')
    age = models.IntegerField(verbose_name='Возраст')
    game = models.CharField(max_length=100, verbose_name='Игра')
    about_me = models.TextField(max_length=2000, verbose_name='О себе')
    league = models.CharField(max_length=200, verbose_name='Лига')
    player = models.BooleanField(verbose_name='Статус')
    nickname = models.CharField(max_length=30, verbose_name='Никнэйм')
    document = models.ImageField(verbose_name='Документ удостоверяющий личность')

    class Meta:
        verbose_name = 'Заявка на создание профиля'
        verbose_name_plural = 'Заявки на создание профиля'
    
    def __str__(self):
        return self.id

class ApplicationForTraining(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(verbose_name='Дата тренировки')
    start = models.TimeField(verbose_name='Начало')
    finish = models.TimeField(verbose_name='Окончание')
    name = models.CharField(max_length=150, verbose_name='ФИО')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    email = models.CharField(max_length=50, verbose_name='Почта')
    game = models.CharField(max_length=50, verbose_name='Игра')

    class Meta:
        verbose_name = 'Заявка на прохождение тренировки'
        verbose_name_plural = 'Заявки на прохождение тренировки'
    
    def __str__(self):
        return self.id






