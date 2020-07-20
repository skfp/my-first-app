from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('<int:user_id>/learn/<int:pile_id>/<int:previous_id>/<str:previous_ans>/', views.learn, name='learn'),
    path('upload/', views.upload, name='upload'),
    #path('load/', views.load_eng, name='load_eng'),
    #path('learn/a/', views.learn_a, name='learn_a'),
    #path('learn/q/', views.learn_q, name='learn_q'),
    #path('learn/q/minus_one_new/', views.minus_one_new, name='minus_one_new'),
    #path('add_e/', views.add_e, name='add_e'),
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
] #+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


