from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput())


    def save(self, commit=True):
        #user = User.objects.create_user(self.cleaned_data['username'],self.cleaned_data['email'],self.cleaned_data['password1'])
        #return user
        



