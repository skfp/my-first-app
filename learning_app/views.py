from django.shortcuts import render
import pandas as pd
from learning_app.models import Card,User,Answer,Pile
from random import randrange
from django.utils import timezone

# Create your views here.

def home(request):
    user_id=1
    pile_list=Pile.objects.filter(user_id=1)
    pile_list_dict={'pile_list':pile_list}
    return render(request, 'learning_app/home.html', pile_list_dict)


def start(request,pile_id):
    our_pile_id=pile_id
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id) 
    one_card= {'one_card_object': one_card_object, 'our_pile_id':our_pile_id}
    return render(request, 'learning_app/start.html', one_card)

def learn(request, pile_id, previous_id, previous_ans):
    if previous_id>0:
        tn=timezone.now()
        tnl=[tn.year,tn.month,tn.day,tn.hour,tn.minute,tn.second]
        tnls=[]
        for t in tnl:
            tnls.append(str(t))
        new_id="".join(tnls)
        NewAnswerRecord = Answer(answer_id=new_id, card_id_ans=previous_id, pile_id=pile_id, answer=previous_ans)
        NewAnswerRecord.save()
    random_id=randrange(8)+1
    one_card_object=Card.objects.get(card_id=random_id, pile_id=pile_id) 
    my_pile = Pile.objects.get(pile_id=pile_id)
    is_last=False
    if my_pile.new_left_today + my_pile.normal_left_today + my_pile.wrong_left_today == 1:
        is_last=True
    if one_card_object.card_type in ["N","NEW"]:
        my_pile.new_left_today = my_pile.new_left_today-1
        my_pile.save()
    if one_card_object.card_type in ["M","H"]:
        my_pile.normal_left_today = my_pile.normal_left_today-1
        my_pile.save()
    if one_card_object.card_type == "W":
        my_pile.wrong_left_today = my_pile.wrong_left_today-1
        my_pile.save()
    if previous_ans=="W":
        my_pile.wrong_left_today = my_pile.wrong_left_today+1
        my_pile.save()
    one_pile_object=Pile.objects.get(pile_id=pile_id)
    one_context = {'one_card_object': one_card_object, 'one_pile_object':one_pile_object, 'is_last':is_last}
#   return render(request, 'learning_app/learn.html', one_context)

def learn_a(request):
    #random_id=17
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id) 
    one_card= {'one_card_object': one_card_object}
    return render(request, 'learning_app/learn_a.html', one_card)

def end(request):
    return render(request, 'learning_app/end.html', {})

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


def load_eng(request):
    virgin_data=pd.read_csv("learning_app/static/data/input_eng.csv",sep=";")
    data_pl_lt=virgin_data.drop(['Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'], axis=1)
    for i in range(data_pl_lt.shape[0]):
        NewCardRecord = Card(card_id = data_pl_lt['id'][i],pile_id = 2,first_lng=data_pl_lt['pl'][i],second_lng= data_pl_lt['eng'][i],card_type=data_pl_lt['class'][i])
        NewCardRecord.save()
    return render(request, 'learning_app/load.html', {})




def add_e(request):
    NewAnswerRecord = Answer( answer_id=1, card_id_ans=1, pile_id=1, answer="E")
    NewAnswerRecord.save()



