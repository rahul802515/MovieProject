from rest_framework import generics, status, filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import JSONParser

from . import models, serializers


class MovieCreateView(generics.CreateAPIView):

    model = models.Movie
    serializer_class = serializers.MovieSerializer
    permission_classes = [AllowAny, ]
    parser_classes = [JSONParser,]

    def create(self, *args, **kwargs):
        
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class MovieRUDView(generics.RetrieveUpdateDestroyAPIView):

    model = models.Movie
    serializer_class = serializers.MovieSerializer
    parser_classes = [JSONParser,]
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return self.model.objects.all()


class MovieListView(generics.ListAPIView):

    model = models.Movie
    serializer_class = serializers.MovieSerializer
    parser_classes = [JSONParser,]
    permission_classes = [AllowAny, ]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend, ]
    filterset_fields = ['title', 'language', 'release_date']
    search_fields = ['=id', 'title']
    ordering_fields = ['created_at']
    ordering = ['-created_at', ]

    def get_queryset(self):
        return self.model.objects.all()


class MoviePosterCreateView(generics.CreateAPIView):

    model = models.MoviePoster
    serializer_class = serializers.MoviePosterSerializer
    parser_classes = [JSONParser,]
    permission_classes = [AllowAny, ]

    def create(self, *args, **kwargs):
        
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie_id = self.kwargs['movie_id'])

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class MoviePosterRUDView(generics.RetrieveUpdateDestroyAPIView):

    model = models.MoviePoster
    serializer_class = serializers.MoviePosterSerializer
    parser_classes = [JSONParser,]
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        return self.model.objects.filter(movie_id=self.kwargs['movie_id'])


class MoviePosterListView(generics.ListAPIView):

    model = models.MoviePoster
    serializer_class = serializers.MoviePosterSerializer
    parser_classes = [JSONParser,]
    permission_classes = [AllowAny, ]

    filter_backends = [filters.SearchFilter]
    search_fields = ['movie']

    def get_queryset(self):
        return self.model.objects.filter(movie_id=self.kwargs['movie_id'])