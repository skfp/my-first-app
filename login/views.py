from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import UserManager


#def login(response):
#    if response.method == "POST":
#        form = RegisterForm(response.POST)
#        if form.is_valid():
#            form.save()
#        return redirect("/home")
#    else:
#    	form = RegisterForm()
#    return render(response, "login/login.html", {"form":form})

def login(response):
    #username = request.POST['username']
    #password = request.POST['password']
    form = RegisterForm(response.POST)
    user = authenticate(request, username=username, password=password)
    our_user=AppUser.objects.filter(user_name=username)
    our_user_id=our_user.user_id
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        success_page='/'+str(our_user_id)+'/'+'choose/'
        ...
        return HttpResponseRedirect(success_page)
    else:
        # Return an 'invalid login' error message.
        ...
        return HttpResponseRedirect('/home/')




