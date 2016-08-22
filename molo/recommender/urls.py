from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^recommender/', views.index, name='index'),
]
