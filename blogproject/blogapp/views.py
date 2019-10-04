from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'blogapp/index.html')




def category(request):
    return render(request,'blogapp/category.html')




def archive(request):
    return render(request,'blogapp/archive.html')





def contact(request):
    return render(request,'blogapp/contact.html')




def login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method=="POST":
            username=request.POST.get('usernamefield')
            password=request.POST.get('passfield')
            auth=authenticate(request,username=username,password=password)
            if auth is not None:
                messages.add_message(request, messages.SUCCESS, 'You have successfully Loged in .You can create Post' )
                auth_login(request,auth)
                return redirect('index')


    return render(request,'blogapp/login.html')




def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, 'You have successfully Loged out' )
    return redirect('index')