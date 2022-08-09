from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from .models import Product, Category, Store, Wishlist



# from priceBetaApp.forms import SignUpForm


def index(request):
    return render(request,'index.html')

def Product(request):
    return HttpResponse("It is working")

def Category(request):
    return HttpResponse('Working')

def Store(request):
    return HttpResponse('Working')

def Wishlist(request):
    return HttpResponse('Working')

