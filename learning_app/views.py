from django.shortcuts import render, redirect
import pandas as pd
from learning_app.models import Card,AppUser,Answer,Pile#,ExcelFile
from random import randrange
from django.utils import timezone
from datetime import date
from django import forms
from django.http import HttpResponseRedirect
#from datetime import datetime,timedelta
from django.views.decorators.csrf import csrf_protect

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.staticfiles.storage import staticfiles_storage

from .forms import UploadFileForm, LoginForm, EditPile, AddCard, CreateNewPileFromOurPiles#, CreateUserForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user_id=request.user.id
    else:
        user_id=0
    pile_list=Pile.objects.filter(user_id=1)
    pile_list_dict={'pile_list':pile_list, 'user_id':user_id}
    return render(request, 'learning_app/home.html', pile_list_dict)


def start(request, pile_id, user_id):
    our_pile_id=pile_id
    one_pile_object=Pile.objects.get(pile_id=pile_id) 
    pile_name=one_pile_object.pile_name
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id) 
    count_all = len(Card.objects.filter(pile_id=pile_id))
    count_new = len(Card.objects.filter(pile_id=pile_id, card_type__in=["N","NEW"]))
    count_norm = len(Card.objects.filter(pile_id=pile_id, card_type__in=["S","M","L","H"]))
    count_wrong = len(Card.objects.filter(pile_id=pile_id, card_type="W"))
    one_card= {'one_card_object': one_card_object, 'our_pile_id':our_pile_id, 'user_id':user_id, 'pile_name':pile_name,
    'count_all':count_all, 'count_new':count_new, 'count_norm':count_norm, 'count_wrong':count_wrong}
    return render(request, 'learning_app/start.html', one_card)

def learn(request, user_id, pile_id, previous_id, previous_ans):
    if request.user.is_authenticated:
        if request.user.id == user_id:
            current_user_id = request.user.id
            my_pile = Pile.objects.get(pile_id=pile_id)
            user_of_this_pile = my_pile.user_id
            if request.user.id == user_of_this_pile:
                if previous_id>0:
                    tn=timezone.now()
                    tnl=[tn.year,tn.month,tn.day,tn.hour,tn.minute,tn.second]
                    tnls=[]
                    for t in tnl:
                        tnls.append(str(t))
                    new_id="".join(tnls)
                    NewAnswerRecord = Answer(answer_id=new_id, card_id_ans=previous_id, pile_id=pile_id, answer=previous_ans)
                    NewAnswerRecord.save()
                    previous_card_object=Card.objects.get(card_id=previous_id, pile_id=pile_id) 
                
                #my_pile = Pile.objects.get(pile_id=pile_id)
                is_last=False
                #random_id=randrange(8)+1
                
                #possible_cards: nowe + zle + zwykle_z_dzisiejsza_data      datetime.date(2005, 1, 1))
                possible_cards_new=Card.objects.filter(pile_id=pile_id,card_type__in=["NEW","N"]) 
                possible_cards_normal=Card.objects.filter(pile_id=pile_id,card_type__in=["S","M","L","H"],next_learn_date=date.today())
                possible_cards_wrong=Card.objects.filter(pile_id=pile_id,card_type="W") 
                #possible_cards=Card.objects.get(card_id=random_id, pile_id=pile_id)
                #count_new=max(0,len(possible_cards_new))
                count_new=min(my_pile.new_left_today,len(possible_cards_new))
                count_normal=len(possible_cards_normal)
                count_wrong=len(possible_cards_wrong)
                count_possible=count_new+count_normal+count_wrong
                random_number=randrange(count_possible)
                if random_number + 1 <= count_new:
                    id_list=[x.card_id for x in possible_cards_new]
                    random_id=id_list[randrange(len(possible_cards_new))]
                elif count_normal + count_new >= random_number + 1 > count_new:
                    id_list=[x.card_id for x in possible_cards_normal]
                    random_id=id_list[randrange(len(possible_cards_normal))]
                else:
                    id_list=[x.card_id for x in possible_cards_wrong]
                    random_id=id_list[randrange(len(possible_cards_wrong))]
                one_card_object=Card.objects.get(card_id=random_id, pile_id=pile_id)

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
                    next_tz=timezone.now()
                    previous_card_object.card_type="W"
                    previous_card_object.next_learn_date=date(next_tz.year,next_tz.month,next_tz.day)
                    previous_card_object.save()
                if previous_ans=="E":
                    previous_card_object.card_type="L"
                    next_tz=timezone.now() + timezone.timedelta(days=7)
                    previous_card_object.next_learn_date=date(next_tz.year,next_tz.month,next_tz.day)
                    previous_card_object.save()
                if previous_ans=="M":
                    previous_card_object.card_type="M"
                    next_tz=timezone.now() + timezone.timedelta(days=4)
                    previous_card_object.next_learn_date=date(next_tz.year,next_tz.month,next_tz.day)
                    previous_card_object.save()
                if previous_ans=="H":
                    previous_card_object.card_type="S"
                    next_tz=timezone.now() + timezone.timedelta(days=2)
                    previous_card_object.next_learn_date=date(next_tz.year,next_tz.month,next_tz.day)
                    previous_card_object.save()
                one_pile_object=Pile.objects.get(pile_id=pile_id)
                user_id=one_pile_object.user_id
                one_context = {'one_card_object': one_card_object, 'one_pile_object':one_pile_object, 'is_last':is_last,'user_id':user_id, 'current_user_id':current_user_id }
                return render(request, 'learning_app/learn.html', one_context)
            else:
                return render(request, 'learning_app/not_auth.html', {})
        else:
            return render(request, 'learning_app/not_auth.html', {})
    else:
        return render(request, 'learning_app/not_auth.html', {})

def end(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        return render(request, 'learning_app/end.html', {'user_id':user_id})
    else:
        return render(request, 'learning_app/not_auth.html', {})

def not_auth(request):
    return render(request, 'learning_app/not_auth.html', {})


def minus_one_new(request):
    my_user = AppUser.objects.get(user_id=1)
    my_user.new_left_today = my_user.new_left_today-1
    my_user.save()
    random_id=randrange(600)
    one_card_object=Card.objects.get(card_id=random_id)
    one_user_object=AppUser.objects.get(user_id=1) 
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

def handle_uploaded_file(title,f):
    max_of_piles=0
    list_of_piles=Pile.objects.all()
    for p in list_of_piles:
        if p.pile_id>max_of_piles:
            max_of_piles=p.pile_id
    virgin_data=pd.read_csv(f,sep=";")
    data_pl_lt=virgin_data.drop(['Unnamed: 4','Unnamed: 5','Unnamed: 6','Unnamed: 7'], axis=1)
    for i in range(data_pl_lt.shape[0]):
        NewCardRecord = Card(card_id = data_pl_lt['id'][i],pile_id = max_of_piles+1,first_lng=data_pl_lt['pl'][i],second_lng= data_pl_lt['eng'][i],card_type=data_pl_lt['class'][i])
        NewCardRecord.save()
    NewPileRecord = Pile(pile_id=max_of_piles+1,pile_name=title,user_id=1,new_left_today=30,normal_left_today=0,wrong_left_today=0,new_per_day=0)
    NewPileRecord.save()

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.POST['title'],request.FILES['file'])
            return HttpResponseRedirect('/home/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def create_user(mail,login,password):
    user = User.objects.create_user(login, mail, password)

def user_created(request):
    return render(request, 'user_created.html')

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('your_login')
            raw_password = form.cleaned_data.get('your_pass')
            #mail = form.cleaned_data.get('your_mail')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
            #create_user(request.POST['your_mail'],request.POST['your_login'],request.POST['your_pass'])
            #return HttpResponseRedirect('/user_created/')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            handle_login(request,request.POST['username'],request.POST['password'])
            u=request.POST['username']
            our_user=AppUser.objects.filter(user_login=u)
            our_user_id=our_user[0].user_id
            # Redirect to a success page.
            success_page='/'+str(our_user_id)+'/'+'choose/'
            return HttpResponseRedirect(success_page)
    else:
        form = LoginForm()
    return render(request, 'login_view.html', {'form': form})

def edit_pile(request, pile_id, user_id):
    our_pile_id=pile_id
    if request.method == 'POST':
        form = EditPile(request.POST)
        if form.is_valid():
            new_pile_name = request.POST['new_pile_name']
            new_cards_per_day = request.POST['new_cards_per_day']
            our_pile=Pile.objects.get(pile_id=our_pile_id)
            our_pile.pile_name = new_pile_name
            our_pile.new_per_day = new_cards_per_day
            our_pile.save()
            success_page='/'+str(user_id)+'/'+'start/'+str(pile_id)
            return HttpResponseRedirect(success_page)
    else:
        form = EditPile()
    return render(request, 'learning_app/edit_pile.html', {'form': form, 'pile_id': our_pile_id, 'user_id': user_id})

def add_card(request, pile_id, user_id):
    our_pile_id=pile_id
    if request.method == 'POST':
        form = AddCard(request.POST)
        if form.is_valid():
            cards_in_pile=Card.objects.filter(pile_id=our_pile_id).order_by('-card_id')
            if len(cards_in_pile) == 0:
                new_card_id=1
            else:
                new_card_id=cards_in_pile[0].card_id+1
            new_card_first_lng = request.POST['first_lng']
            new_card_second_lng = request.POST['second_lng']
            new_card = Card(card_id=new_card_id, pile_id=pile_id, first_lng=new_card_first_lng, second_lng=new_card_second_lng)
            new_card.save()
            success_page='/'+str(user_id)+'/'+'start/'+str(pile_id)
            #return HttpResponseRedirect(success_page)
            return render(request, 'learning_app/add_card.html', {'form': form, 'pile_id': our_pile_id, 'user_id': user_id})
    else:
        form = AddCard()
    return render(request, 'learning_app/add_card.html', {'form': form, 'pile_id': our_pile_id, 'user_id': user_id})

def handle_login(request,u,p):
    user = authenticate(request, username=u, password=p)
    if user is not None:
        login(request, user)
    else:
    # Return an 'invalid login' error message.
        return HttpResponseRedirect('/home/')


def choose(request,user_id):
    if user_id == 0:
        return render(request, 'learning_app/not_auth.html', {})
    else:
        pile_list=Pile.objects.filter(user_id=user_id)
        pile_list_dict={'pile_list':pile_list,'user_id':user_id}
        return render(request, 'learning_app/choose.html', pile_list_dict)


def create_new_pile_from_file(user_id,pile_name,file_name,new_cards_per_day):
    list_of_piles = Pile.objects.all().order_by('-pile_id')
    new_pile_id = list_of_piles[0].pile_id+1
    new_pile = Pile(user_id=user_id, pile_id=new_pile_id, pile_name=pile_name, new_per_day=new_cards_per_day, new_left_today = new_cards_per_day)
    new_pile.save()
    if file_name!= '-':
        f = "learning_app/static/data/"+file_name
        virgin_data = pd.read_csv(f,sep=";")
        for i in range(virgin_data.shape[0]):
            first_lng_name = virgin_data.columns[0]
            second_lng_name = virgin_data.columns[1]
            first_lng = virgin_data[first_lng_name][i]
            second_lng = virgin_data[second_lng_name][i]
            new_card = Card(card_id=i+1,pile_id=new_pile_id,first_lng=first_lng,second_lng=second_lng)
            new_card.save()


def create_new_pile(request,user_id):
    if request.method == 'POST':
        form = CreateNewPileFromOurPiles(request.POST)
        if form.is_valid():
            create_new_pile_from_file(user_id,request.POST['pile_name'],request.POST['file_name'],request.POST['new_cards_per_day'])
            return HttpResponseRedirect('/home/')
    else:
        form = CreateNewPileFromOurPiles()
    return render(request, 'create_new_pile.html', {'form': form, 'user_id': user_id})

def refresh_new_cards_today_value():
    all_piles = Pile.objects.all()
    for i in all_piles:
        all_new_cards = Card.objects.filter(pile_id = i.pile_id, card_type__in=["NEW","N"]) 
        all_new_cards_count = len(all_cards)
        new_value = min(all_new_cards_count, i.new_per_day)
        i.new_left_today = new_value
#refresh_new_cards_today_value()


from learning_app.models import Card,AppUser,Answer,Pile
all_piles = Pile.objects.all()
for i in all_piles:
    all_new_cards = Card.objects.filter(pile_id = i.pile_id, card_type__in=["NEW","N"]) 
    all_new_cards_count = len(all_new_cards)
    new_value = min(all_new_cards_count, i.new_per_day)
    i.new_left_today = new_value
    i.save()

