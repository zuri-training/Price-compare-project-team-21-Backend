from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse



# from priceBetaApp.forms import SignUpForm


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')

def contact(request):
    return render(request,'contact.html')

def privacy(request):
    return render(request,'privacy.html')

def term(request):
    return render(request,'term.html')

def accessories_category(request):
    return render(request,'accessories_category.html')

def laptop_category(request):
    return render(request,'laptop_category.html')

def phone_category(request):
    return render(request,'phone_category.html')

def Product(request):
    return HttpResponse("It is working")

def Category(request):
    return HttpResponse('Working')

def Store(request):
    return HttpResponse('Working')

def Wishlist(request):
    return HttpResponse('Working')

