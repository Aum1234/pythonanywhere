from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import inputrestaurant

# Create your views here.
def index(req):
    inputrestaurants = inputrestaurant.objects.all()
    return render(req, 'mywed/index.html', {'inputrestaurants': inputrestaurants})

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'mywed/signup.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')

def contact(req):
    return render(req,'mywed/contact.html')

def foradmin(request):
    if request.method == 'POST':

        img = request.POST.get("img")
        restaurantname = request.POST.get("restaurantname")
        address = request.POST.get("address")
        add = inputrestaurant(img=img,restaurantname=restaurantname,address=address)
        add.save()
        return redirect('index')
    return render(request, 'mywed/foradmin.html')

def foradmins(req):
    inputrestaurants = inputrestaurant.objects.all()
    ins = {
        'inputrestaurants' : inputrestaurants
        }
    return render(req, 'mywed/foradmin.html', ins)
