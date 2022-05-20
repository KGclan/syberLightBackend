# Generated by Django 3.1.7 on 2022-05-16 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', models.SlugField(verbose_name='Название для запроса')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('league', models.CharField(max_length=100, verbose_name='Название лиги')),
            ],
            options={
                'verbose_name': 'Лига',
                'verbose_name_plural': 'Лиги',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=15, verbose_name='Ник')),
                ('image', models.ImageField(upload_to='', verbose_name='Аватар')),
                ('about_me', models.TextField(max_length=2000, verbose_name='О себе')),
                ('rating', models.CharField(max_length=30, verbose_name='Рейтинг игрока')),
                ('age', models.IntegerField(verbose_name='Возраст')),
                ('win', models.IntegerField(verbose_name='Победы')),
                ('lose', models.IntegerField(verbose_name='Поражения')),
                ('phone', models.CharField(max_length=11, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=50, verbose_name='Почта')),
                ('vk', models.CharField(max_length=1000, verbose_name='Ссылка на вк')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.game', verbose_name='Игра')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.league', verbose_name='Лига')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100, verbose_name='Название статуса')),
            ],
            options={
                'verbose_name': 'Статус пользователя',
                'verbose_name_plural': 'Статусы пользователей',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='')),
                ('lose', models.IntegerField(verbose_name='Поражений')),
                ('win', models.IntegerField(verbose_name='Побед')),
                ('captain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_captain', to='api.profile', verbose_name='Капитан')),
                ('games', models.ManyToManyField(to='api.Game', verbose_name='Игры')),
                ('league', models.ManyToManyField(to='api.League', verbose_name='Лига')),
                ('players', models.ManyToManyField(related_name='team_players', to='api.Profile', verbose_name='Игроки')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команды',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.status', verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('url', models.CharField(max_length=1000, verbose_name='Ссылка на трансляцию')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.game', verbose_name='Игра')),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.league', verbose_name='Лига')),
                ('teams', models.ManyToManyField(to='api.Team', verbose_name='Команды')),
            ],
            options={
                'verbose_name': 'Матч',
                'verbose_name_plural': 'Матчи',
            },
        ),
    ]
