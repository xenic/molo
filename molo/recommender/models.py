from django.db import models
from django.contrib.auth.models import User


class StandardRepr(models.Model):
    def __repr__(self):
        vals = []
        for f in self.__dict__:
            if not f.startswith('_'):
                vals.append(f + '=' + self.__dict__[f].__repr__())
        return '{}({})'.format(self.__class__.__name__, ', '.join(vals))

    class Meta:
        abstract = True


class Genre(StandardRepr):
    name = models.CharField(max_length=32)


class Occupation(StandardRepr):
    name = models.CharField(max_length=32)


class AgeRange(StandardRepr):
    value = models.IntegerField()
    description = models.CharField(max_length=16)


class Movie(StandardRepr):
    title = models.CharField(max_length=256)
    year = models.IntegerField(null=True)
    genres = models.ManyToManyField(Genre)


class Rater(StandardRepr):
    gender = models.CharField(max_length=8)
    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=10)
    user = models.OneToOneField(User)


class Rating(StandardRepr):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    rating = models.IntegerField()
    rate_time = models.DateTimeField(auto_now=False)
