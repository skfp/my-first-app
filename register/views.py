# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import UserManager


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
    	form = RegisterForm()
    #UserManager.create_user(form.your_name,form.your_mail,form.your_pass)

    return render(response, "register/register.html", {"form":form})