"""Визначити регулярні вирази URL"""

from django.urls import path, include
from .views import logout_view
from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('', include('django.contrib.auth.urls')),
    #Сторінка реєстрації
    path('register/', views.register, name='register'),
]