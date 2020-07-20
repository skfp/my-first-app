from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)
    #password = forms.CharField(widget=forms.PasswordInput())

class EditPile(forms.Form):
    new_pile_name = forms.CharField(max_length=50)
    new_cards_per_day = forms.IntegerField()

class AddCard(forms.Form):
    first_lng = forms.CharField(max_length=200)
    second_lng = forms.CharField(max_length=200)

CHOICES = [('verbs_eng.csv','English iregular verbs'),('verbs_ger.csv','German iregular verbs')]
class CreateNewPileFromOurPiles(forms.Form):
    pile_name = forms.CharField(max_length=200)
    file_name = forms.CharField(label='Pile content', widget=forms.RadioSelect(choices=CHOICES))
    new_cards_per_day = forms.IntegerField()


#class CreateUserForm(forms.Form):
#    your_mail = forms.EmailField(max_length=80)
#    your_login = forms.CharField(max_length=20)
#    your_pass = forms.CharField(max_length=50)

#class SignUpForm(UserCreationForm):
#    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#    class Meta:
#        model = User
#        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )





