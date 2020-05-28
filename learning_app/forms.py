from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class CreateUserForm(forms.Form):
    your_mail = forms.CharField(max_length=50)
    your_login = forms.CharField(max_length=20)
    your_pass = forms.CharField(max_length=50)








