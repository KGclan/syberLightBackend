# Generated by Django 3.1.7 on 2022-05-20 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(max_length=3000, verbose_name='Новость'),
        ),
    ]
