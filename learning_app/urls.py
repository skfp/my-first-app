from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('load/', views.load, name='load'),
    path('learn/a/', views.learn_a, name='learn_a'),
    path('learn/q/', views.learn_q, name='learn_q'),
    path('learn/q/minus_one_new/', views.minus_one_new, name='minus_one_new'),
    path('add_e/', views.add_e, name='add_e'),
]


