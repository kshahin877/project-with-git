from django.shortcuts import render

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
    return render(request,'blogapp/login.html')