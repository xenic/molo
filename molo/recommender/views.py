from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hi Mom")

def genre_list(request):
    if request.POST:
        print('post')
    elif request.GET:
        print('get')
    return render('templates/genres.html', 'genre_list')
