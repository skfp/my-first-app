from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), max_length=50) #, widget=forms.TextInput(attrs={'placeholder': 'password'}))
    

class EditPile(forms.Form):
    new_pile_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'pile name'}))
    new_cards_per_day = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'new cards per day'}))

class AddCard(forms.Form):
    first_lng = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'first language'}))
    second_lng = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'second language'}))

class IncreaseNumberOfNewCards(forms.Form):
    increase_value = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'number of additional cards'}))

CHOICES = [('-','Create empty pile'),
    ('verbs_eng.csv','English irregular verbs (PL)'),('verbs_ger.csv','German irregular verbs (PL)'),
    ('lt.csv','Lithuanian words (PL)')]
class CreateNewPileFromOurPiles(forms.Form):
    pile_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'pile name'}))
    file_name = forms.CharField(label='Pile content', widget=forms.RadioSelect(choices=CHOICES))
    new_cards_per_day = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'new cards per day'}))


class CreateUserForm(forms.Form):
    your_mail = forms.EmailField(max_length=80, widget=forms.TextInput(attrs={'placeholder': 'email address'}))
    your_login = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'login'}))
    your_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}), max_length=50)

#class SignUpForm(UserCreationForm):
#    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#    class Meta:
#        model = User
#        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )





