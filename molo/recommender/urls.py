from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^recommender/$', views.index, name='index'),
    url(r'^genre_list$', views.genre_list, name='genre_list'),
]
