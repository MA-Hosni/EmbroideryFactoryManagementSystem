from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.loginPage, name='loginpage'),
    path('verify/', views.verify_view, name='verifyview'),
    path('logout/', views.logoutUser, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetView.as_view(), name="password_reset_complete"),
]