from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
  poster = models.ImageField(upload_to="images/")
  name = models.CharField(max_length=50)
  releaseDate = models.DateField()
  director = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)

class QuizMovie(models.Model):
  title = models.CharField(max_length=80)
  poster = models.ImageField(upload_to="images/posters", blank=True, null=True)
  year = models.IntegerField()
  director = models.CharField(max_length=50)
  genre = models.CharField(max_length=30)
  subgenre = models.CharField(max_length=30, blank=True, default='')

class QuizResults(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  movPool = models.JSONField()
  dictAnswers = models.JSONField()
  pos = models.IntegerField(null=True)
  permaFavGenre = models.CharField(max_length=25, blank=True, null=True)

class Amigos (models.Model):
  username = models.CharField(max_length=50)
  name = models.CharField(max_length=50)
  generofav = models.CharField(max_length=50)
  pic = models.ImageField(upload_to="images/")

class UserProfile(models.Model):
  name = models.CharField(max_length=25, default="Name")
  email = models.EmailField(unique=True, default="email@gmail.com")
  bio = models.TextField(default='Olá, estou usando o MovieMatch!', null=True)
  pic = models.ImageField(upload_to="images/", default="images/defaultpfp.png", null=True)
  generofav = models.CharField(max_length=50, null=True, blank=True)