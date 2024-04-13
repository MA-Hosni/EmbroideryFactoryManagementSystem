from django.urls import path
from . import views


urlpatterns = [
    path('submit', views.subconge, name='submitcounji'),
    path('list', views.follconge, name='followcounji'),
]