from django.contrib import admin
from .models import Genre, AgeRange, Occupation

admin.site.register(Genre)
admin.site.register(AgeRange)
admin.site.register(Occupation)
