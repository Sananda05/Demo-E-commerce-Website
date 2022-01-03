from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
   path('', views.landingView),
   path('/login', views.loginView),
   path('/registration', views.RegistrationView),
]
