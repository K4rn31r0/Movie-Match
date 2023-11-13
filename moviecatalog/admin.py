from django.contrib import admin
from .models import Movie, QuizMovie

admin.site.register(Movie)
admin.site.register(QuizMovie)

# username - admin
# password - moviematchadmin