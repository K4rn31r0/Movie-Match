from django.shortcuts import render
from .models import Movie

def home(request):
  movieList = Movie.objects.all()
  return render(request, "homepage.html", context={"Filmes":movieList})
