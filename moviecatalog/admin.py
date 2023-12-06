from django.contrib import admin
from .models import Movie, QuizMovie, QuizResults, Amigos, UserProfile

admin.site.register(Movie)
admin.site.register(QuizMovie)
admin.site.register(QuizResults)
admin.site.register(Amigos)
admin.site.register(UserProfile)

# username - admin
# password - moviematchadmin