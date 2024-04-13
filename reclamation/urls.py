from django.urls import path
from . import views


urlpatterns = [
    path('submit', views.subcomplaint, name='submitcomplaint'),
    path('list', views.follcomplaint, name='followcomplaint'),
]