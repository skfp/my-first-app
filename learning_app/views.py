from django.shortcuts import render
import pandas as pd
from learning_app.models import Card,User,Answer
from random import randrange
from django.utils import timezone

# Create your views here.

def home(request):
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id) 
    one_card= {'one_card_object': one_card_object}
    return render(request, 'learning_app/home.html', one_card)

def learn(request, previous_id, previous_ans):
    if previous_id>0:
        tn=timezone.now()
        new_id="".join([tn.year,tn.month,tn.day,tn.hour,tn.minute,tn.second])
        NewAnswerRecord = Answer(answer_id=new_id, card_id_ans=previous_id, pile_id=1, answer=previous_ans)
        NewAnswerRecord.save()
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id) 
    one_user_object=User.objects.get(user_id=1) 
    if one_card_object.card_type in ["N","NEW"]:
        my_user = User.objects.get(user_id=1)
        my_user.new_left_today = my_user.new_left_today-1
        my_user.save()
    one_context = {'one_user_object': one_user_object,'one_card_object': one_card_object}
    return render(request, 'learning_app/learn.html', one_context)

def learn_a(request):
    #random_id=17
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id) 
    one_card= {'one_card_object': one_card_object}
    return render(request, 'learning_app/learn_a.html', one_card)

def learn_q(request):
    #random_id=17
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id)
    one_user_object=User.objects.get(user_id=1) 
    if one_card_object.card_type in ["N","NEW"]:
        my_user = User.objects.get(user_id=1)
        my_user.new_left_today = my_user.new_left_today-1
        my_user.save()
    one_context = {'one_user_object': one_user_object,'one_card_object': one_card_object}
    return render(request, 'learning_app/learn_q.html', one_context)


def minus_one_new(request):
    my_user = User.objects.get(user_id=1)
    #my_user.update(new_left_today=F('new_left_today') - 1)
    #my_user.refresh_from_db()
    my_user.new_left_today = my_user.new_left_today-1
    my_user.save()
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id)
    one_user_object=User.objects.get(user_id=1) 
    one_context = {'one_user_object': one_user_object,'one_card_object': one_card_object}
    return render(request, 'learning_app/learn_q.html', one_context)

def load(request):
    virgin_data=pd.read_csv("learning_app/static/data/input.csv",sep=";")
    data_pl_lt=virgin_data.drop(['Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'], axis=1)
    for i in range(data_pl_lt.shape[0]):
        NewCardRecord = Card(card_id = data_pl_lt['id'][i],pile_id = 1,first_lng=data_pl_lt['pl'][i],second_lng= data_pl_lt['lt'][i],card_type=data_pl_lt['class'][i])
        NewCardRecord.save()
    return render(request, 'learning_app/load.html', {})


def add_e(request):
    NewAnswerRecord = Answer( answer_id=1, card_id_ans=1, pile_id=1, answer="E")
    NewAnswerRecord.save()



