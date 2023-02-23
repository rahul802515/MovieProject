from rest_framework import serializers

from . import models


class MovieSerializer(serializers.ModelSerializer):
     
    poster_path = serializers.SerializerMethodField()

    class Meta:
        model = models.Movie
        fields = '__all__'

    def get_poster_path(self, obj: models.Movie):

        return list(obj.poster_path)


class MoviePosterSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MoviePoster
        fields = '__all__'
        read_only_fields = [
            'movie',
        ]