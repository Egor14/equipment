from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('log/', views.entry, name='entry'),
]