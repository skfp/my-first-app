from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('<int:user_id>/learn/<int:pile_id>/<int:previous_id>/<str:previous_ans>/', views.learn, name='learn'),
    path('upload/', views.upload, name='upload'),
    path('end/', views.end, name='end'),
    path('not_auth/', views.not_auth, name='not_auth'),
    path('login_view/', views.login_view, name='login_view'),
    path('<int:user_id>/edit_pile/<int:pile_id>/', views.edit_pile, name='edit_pile'),
    path('<int:user_id>/add_card/<int:pile_id>/', views.add_card, name='add_card'),
    path('register/', views.register, name='register'),
    path('user_created/', views.user_created, name='user_created'),
    path('<int:user_id>/start/<int:pile_id>/', views.start, name='start'),
    path('<int:user_id>/choose/', views.choose, name='choose'),
    path('<int:user_id>/create_new_pile/', views.create_new_pile, name='create_new_pile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]



