from django.shortcuts import render
import pandas as pd
from learning_app.models import Card
from random import randrange

# Create your views here.

def home(request):
    return render(request, 'learning_app/home.html', {})

def learn(request):
    return render(request, 'learning_app/learn.html', {})

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
    one_card= {'one_card_object': one_card_object}
    return render(request, 'learning_app/learn_q.html', one_card)


def load(request):
    virgin_data=pd.read_csv("learning_app/static/data/input.csv",sep=";")
    data_pl_lt=virgin_data.drop(['Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'], axis=1)
    for i in range(data_pl_lt.shape[0]):
        NewCardRecord = Card(card_id = data_pl_lt['id'][i],pile_id = 1,first_lng=data_pl_lt['pl'][i],second_lng= data_pl_lt['lt'][i],card_type=data_pl_lt['class'][i])
        NewCardRecord.save()
    return render(request, 'learning_app/load.html', {})




User.objects.create(user_id=1,user_name="Sylwester",user_login="sylw",
user_password="sylw",user_mail= "lordin88@vp.pl" , 
new_left_today=30,
normal_left_today=30,
wrong_left_today=10)