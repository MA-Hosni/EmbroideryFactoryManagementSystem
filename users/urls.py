from django.urls import path
from . import views


urlpatterns = [
    path('adherents', views.adherents, name='adherent'),
    path('employees', views.employees, name='employees'),
    path('interns', views.interns, name='interns'),
    # path('<int:id>', views.view_adherent, name='view_adherent'),
    #delete adherent
    path('delete_adherent/<int:id>/', views.delete_adherent, name='delete_adherent'),
    #delete employee
    path('delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
    #delete intern
    path('delete_intern/<int:id>/', views.delete_intern, name='delete_intern'),
    #add intern
    path('add/', views.add, name='add'),
]