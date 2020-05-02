from django.shortcuts import render
import pandas as pd

# Create your views here.

def home(request):
    return render(request, 'learning_app/home.html', {})

def learn(request):
    return render(request, 'learning_app/learn.html', {})

def load(request):
    virgin_data=pd.read_csv("input.csv",sep=";")
    data_pl_lt=virgin_data.drop(['Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'], axis=1)
    for i in range(data_pl_lt.shape[0]):
        NewCardRecord = Card(card_id = data_pl_lt['id'][i],pile_id = 1,first_lng=data_pl_lt['pl'][i],second_lng= data_pl_lt['lt'][i],card_type=data_pl_lt['class'][i])
        #db.session.add(NewCardRecord)
        #db.session.commit()
        NewCardRecord.save()
    return render(request, 'learning_app/load.html', {})

