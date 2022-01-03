from django.contrib import admin
from django.urls import path, include

from PandaMart import Authentication

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include('Authentication.views')),
]
