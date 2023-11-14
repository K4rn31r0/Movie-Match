from django.shortcuts import render
from .models import Movie, QuizMovie
from .scripts.quiz_genero import avaliaFilme, detGenFav
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  movieList = Movie.objects.all()
  return render(request, "homepage.html", context={"Filmes":movieList})
@login_required
def about_us(request):
  return render(request, "about_us.html")
@login_required
def profile(request):
  return render(request, "profile.html")
@login_required
def series(request):
  return render(request, "series.html")
@login_required
def movies(request):
  return render(request, "movies.html")
@login_required
def quiz(request):
  print('Flash!')
  quizMovieList = QuizMovie.objects.all()
  listaFilmes = list(quizMovieList)
  dicNotaUser = avaliaFilme(listaFilmes)
  #detGenFav(dicNota)
  context={"thelist":quizMovieList}
  return render(request, "quiz_fav.html", context)
@login_required
def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})

def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")