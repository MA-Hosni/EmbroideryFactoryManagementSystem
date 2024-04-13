from django.urls import path
from . import views


urlpatterns = [
    path('admin/', views.follownotification, name='follownotification'),
    path('', views.notificationclient, name='notificationclient'),
]