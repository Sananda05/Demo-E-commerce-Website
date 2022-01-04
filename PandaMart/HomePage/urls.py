from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from PandaMart.settings import STATIC_URL

from . import views

urlpatterns = [
   path('homepage/', views.homePageView),
]

if settings.DEBUG:

        urlpatterns+= static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
       