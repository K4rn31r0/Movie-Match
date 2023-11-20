from django.shortcuts import render
from .models import Movie, QuizMovie, QuizResults
from .scripts.quiz_genero import avaliaFilme, detGenFav
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import random as r


def landing_page(request):
  return render(request, "landingpage.html")
  
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
def edit_profile(request):
  return render(request, "edit-profile.html")
  
@login_required
def amigos(request):
  return render(request, "amigos.html")
  
@login_required
def movies(request):
  return render(request, "movies.html")
  
@login_required
def quiz(request):
  if request.method == "POST":
    index = int(request.POST["index"])
    nota = int(request.POST["nota"])
    
    quiz_res = QuizResults.objects.filter(user=request.user).first()
    unratedMovies = quiz_res.movPool
    i = quiz_res.pos
    answers = quiz_res.dictAnswers
    answers = avaliaFilme(unratedMovies, nota, answers, i)
    print(answers)
    
    quiz_res.pos = r.randint(0, len(unratedMovies)-1)
    quiz_res.save()

    i=quiz_res.pos
    movName = unratedMovies[i]['title']
    
    print('\nINDICE ', index)
    
    if index == 10:
      fav = detGenFav(quiz_res.dictAnswers)
      quiz_res.permaFavGenre = fav
      quiz_res.save()
      return render(request, "quiz_fav_result.html", context={"Fav":fav})
      
    index+=1
    
  else:
    unratedMovies = list(QuizMovie.objects.all().values('title','genre'))
    answers = {}
    index = 1
    i = r.randint(0, len(unratedMovies)-1)

    movName = unratedMovies[i]['title']

    quiz_res = QuizResults.objects.filter(user=request.user).first()
    if not quiz_res:
      QuizResults.objects.create(
        user=request.user,
        movPool = unratedMovies,
        dictAnswers = answers,
        pos = i
      )
    else:
      quiz_res.movPool = unratedMovies
      quiz_res.dictAnswers = answers
      quiz_res.pos = i
      quiz_res.save()
      
  return render(request, "quiz_fav.html", context = {"valorIndice":index,                                            "nomeFilme":movName})

def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("landing page")
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
  return redirect("landing page")
