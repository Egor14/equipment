from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.start, name='start'),
    path('log/', views.entry, name='entry'),
    path('add/', views.add, name='add'),
    path('rem/<int:id>', views.rem, name='rem'),
    path('plus/<int:id>', views.plus, name='plus'),
    path('minus/<int:id>', views.minus, name='minus'),
    path('out/', views.out, name='out'),
    path('sign/', views.sign, name='sign'),
    path('query/', views.query, name='query'),
]