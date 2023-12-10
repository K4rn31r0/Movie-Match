"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from moviecatalog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_page, name="landing page"),
    path('home/sobre-nos', views.about_us),
    path('home/profile', views.profile, name="profile"),
    path('home/profile/editprofile', views.editProfile),
    path('home/amigos', views.amigos),
    path('home/movies', views.movies, name="movies"),
    path('home/quiz-genero-fav/', views.quiz, name="quiz"),
    path('users/login/', views.login_user, name="login"),
    path('users/logout/', views.logout_user, name="logout"),
    path('users/register/', views.create_user, name="register"),
    path('home/',views.home, name="home"),
    
  
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
