from django.db import models

class Movie(models.Model):
  poster = models.ImageField(upload_to="images/")
  name = models.CharField(max_length=50)
  releaseDate = models.DateField()
  director = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)

class QuizMovie(models.Model):
  title = models.CharField(max_length=80)
  year = models.IntegerField()
  director = models.CharField(max_length=50)
  genre = models.CharField(max_length=30)
  subgenre = models.CharField(max_length=30, blank=True, default='')