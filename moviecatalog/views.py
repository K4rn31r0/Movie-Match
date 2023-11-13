from django.shortcuts import render
from .models import Movie, QuizMovie
from .scripts.quiz_genero import avaliaFilme, detGenFav

def home(request):
  movieList = Movie.objects.all()
  return render(request, "homepage.html", context={"Filmes":movieList})

def about_us(request):
  return render(request, "about_us.html")

def quiz(request):
  print('Flash!')
  quizMovieList = QuizMovie.objects.all()
  #dicNota = avaliaFilme(quizMovieList)
  #detGenFav(dicNota)
  context={"thelist":quizMovieList}
  return render(request, "quiz_fav.html", context)