from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('load/', views.load, name='load'),
]


