from django.contrib import admin

from .models import MoviePoster, Movie


admin.site.register(Movie)
admin.site.register(MoviePoster)