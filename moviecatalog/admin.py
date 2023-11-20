from django.contrib import admin
from .models import Movie, QuizMovie, QuizResults

admin.site.register(Movie)
admin.site.register(QuizMovie)
admin.site.register(QuizResults)

# username - admin
# password - moviematchadmin