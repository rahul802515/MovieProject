from django.db import models
from django.utils import timezone


# Base class which will use in all other model class.
class TimeStampModel(models.Model):

    created_at: timezone.datetime = models.DateTimeField(auto_now_add=True)
    updated_at: timezone.datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Movie(TimeStampModel):

    title: str                              = models.CharField(max_length=1000)
    language: str                           = models.CharField(max_length=100)
    overview: str                           = models.TextField(null=True)
    release_date: timezone.datetime.date    = models.DateField()

    class Meta:
        unique_together = (
            ('title', 'language')
        )

    def __str__(self):
        return "%s" % self.title

    @property
    def poster_path(self):
        return MoviePoster.objects.filter(movie=self).values_list('poster_path')


class MoviePoster(TimeStampModel):

    movie       = models.ForeignKey(Movie, on_delete=models.CASCADE)
    poster_path = models.URLField(max_length=1000)
