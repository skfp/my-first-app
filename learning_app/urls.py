from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('learn/<int:pile_id>/<int:previous_id>/<str:previous_ans>/', views.learn, name='learn'),
    path('upload/', views.upload, name='upload'),
    #path('load/', views.load_eng, name='load_eng'),
    #path('learn/a/', views.learn_a, name='learn_a'),
    #path('learn/q/', views.learn_q, name='learn_q'),
    #path('learn/q/minus_one_new/', views.minus_one_new, name='minus_one_new'),
    #path('add_e/', views.add_e, name='add_e'),
    path('end/', views.end, name='end'),
    path('login_view/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('user_created/', views.user_created, name='user_created'),
    path('start/<int:pile_id>/', views.start, name='start'),
    path('<int:user_id>/choose/', views.choose, name='choose'),
] #+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


