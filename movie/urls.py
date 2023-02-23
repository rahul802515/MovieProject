from django.urls import path

from . import views
app_name = 'movie'

urlpatterns = [

    path("movie/", views.MovieCreateView.as_view(), name="movie-create"),
    path("movie/<int:pk>/", views.MovieRUDView.as_view(), name="movie-rud"),
    path("movies/", views.MovieListView.as_view(), name="movie-list"),

    path("movie/<int:movie_id>/movie-poster/", views.MoviePosterCreateView.as_view(), name="movie-poster-create"),
    path("movie/<int:movie_id>/movie-poster/<int:pk>/", views.MoviePosterRUDView.as_view(), name="movie-poster-rud"),
    path("movie/<int:movie_id>/movie-posters/", views.MoviePosterListView.as_view(), name="movie-poster-list"),
]


