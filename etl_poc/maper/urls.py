
from django.contrib import admin
from django.urls import path, include

from maper.views import list_data

urlpatterns = [
    path('data/', list_data),
]
