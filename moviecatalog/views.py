from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, QuizMovie, QuizResults, Amigos, UserProfile
from .forms import EditProfileForm
from .scripts.quiz_genero import avaliaFilme, detGenFav, detIfAmigo, detFilme
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from django.core.files.storage import default_storage
import random as r


def landing_page(request):
  movies = QuizMovie.objects.all()
  for obj in movies:
    print(obj.title, ' - ' ,obj.genre)
  return render(request, "landingpage.html")
  
@login_required
def home(request):
  movieList = QuizMovie.objects.filter(year='2023').all()
  random = movieList.order_by('?')[:6]
  return render(request, "homepage.html", context={"Filmes":random})
  
@login_required
def about_us(request):
  return render(request, "about_us.html")
  
@login_required
def profile(request):
  movieList = Movie.objects.all()
  userdata = QuizResults.objects.filter(user=request.user).first()
  profileinfo = UserProfile.objects.filter(name=request.user).first()
  userpic = profileinfo.pic
  bio = profileinfo.bio
  if userdata == None or userdata.permaFavGenre == None:
    favGenre = "Faça o quiz para ter um gênero favorito!"
  else:
    favGenre = userdata.permaFavGenre
  return render(request, "profile.html", {"Filmes":movieList, "GeneroFav":favGenre, "Pfpic":userpic, "Bio": bio})

def deletaFotoPerfil(path):
  default_storage.delete(path)
  return

@login_required
def editProfile(request):
  user = UserProfile.objects.filter(name=request.user).first()
  
  if request.method == "POST":
    form = EditProfileForm(request.POST, request.FILES)
    
    if form.is_valid():
      oldpic = user.pic.path
      user.bio = request.POST['bio']
      
      if 'pic' in request.FILES:
        if user.pic.name != 'images/defaultpfp.png':
          user.pic.delete(save=False)
          
        user.pic = request.FILES['pic']
        
      user.save()

      if oldpic and oldpic != user.pic.path:
        deletaFotoPerfil(oldpic)
        
      return redirect("profile")   
      
  else:
    form = EditProfileForm(initial={'bio':user.bio})
    
  return render(request, 'editprofile.html', context={"form":form})

  
@login_required
def amigos(request):
  amigos = Amigos.objects.all()
  amigos_data = []
  for amigo in amigos:
    if detIfAmigo(QuizResults.objects.filter(user=request.user).first(), amigo) == 'match':
      amigos_data.append({'amigo': amigo})
  return render(request, 'amigos.html', {'Amigos':amigos, 'amigos_data':amigos_data})
  
@login_required
def movies(request):
  activeuser=request.user
  userdata=QuizResults.objects.filter(user=activeuser).first()
  if userdata is None or userdata.permaFavGenre is None:
    return redirect("quiz")
  favGenre = userdata.permaFavGenre
  movieList = QuizMovie.objects.filter(genre=favGenre)
  random_movies = movieList.order_by('?')[:6]
  random_movies2 = movieList.order_by('?')[:6]
  return render(request, "movies.html", {"Filmes":random_movies,
                                         "Filmes2":random_movies2,
                                        "UserFav":favGenre})
  
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
    poster = QuizMovie.objects.filter(title=movName).first().poster
    #print('ID = ', QuizMovie.objects.filter(title=movName).first().id)
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
    poster = QuizMovie.objects.filter(title=movName).first().poster

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
      
  return render(request, "quiz_fav.html", context = {"valorIndice":index,                                            "nomeFilme":movName, "poster":poster})

def create_user(request):
  if request.method == "POST":
    try:
      user = User.objects.create_user(
        request.POST["username"],
        request.POST["email"], 
        request.POST["password"],
      )
      user.save()
      userprofile = UserProfile.objects.create(
        name = request.POST["username"],
        email = user.email
      )
      userprofile.save()
      return redirect("landing page")
    except IntegrityError:
      erro = 'ERRO: Usuário já existe!'
      return render(request, "register.html", context={"action": "Adicionar", "ErrorMsg":erro})
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

