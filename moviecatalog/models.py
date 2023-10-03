from django.db import models

class Movie(models.Model):
  poster = models.ImageField(upload_to="images/")
  name = models.CharField(max_length=50)
  releaseDate = models.DateField()
  director = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)

