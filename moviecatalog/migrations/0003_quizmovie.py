# Generated by Django 3.2.13 on 2023-11-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecatalog', '0002_alter_movie_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('year', models.IntegerField()),
                ('director', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=30)),
                ('subgenre', models.CharField(max_length=30)),
            ],
        ),
    ]
