from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Occupation(models.Model):
    name = models.CharField(max_length=32)


class AgeRange(models.Model):
    value = models.IntegerField()
    description = models.CharField(max_length=16)


class Movie(models.Model):
    title = models.CharField(max_length=256)
    year = models.IntegerField(null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Rater(models.Model):
    gender = models.CharField(max_length=8)
    age_range = models.ForeignKey(AgeRange, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    zipcode = models.IntegerField(null=True)

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=False)
