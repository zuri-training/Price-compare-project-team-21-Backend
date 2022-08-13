from multiprocessing import context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product



# from priceBetaApp.forms import SignUpForm


def index(request):
    accessory_category = Product.objects.filter(category_id=3)
    laptop_category = Product.objects.filter(category_id=2)
    phone_category = Product.objects.filter(category_id=1)
    return render(request,'index.html', {'accessory_category': accessory_category,'laptop_category' : laptop_category , 'phone_category': phone_category} )

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def privacy(request):
    return render(request,'privacy.html')

def term(request):
    return render(request,'term.html')

@login_required
def wishlist(request):
    return render(request,'wishlist.html')

def review(request):
    return render(request,'review.html')

@login_required
def user_profile(request):
    return render(request,'user_profile.html')

# def accessories_category(request):
#     return render(request,'accessories_category.html')

@login_required
def all_accessory(request):
    accessory_category = Product.objects.filter(category_id=3)
    return render(request, 'accessory_category.html', {'accessory_category': accessory_category})

# def laptop_category(request):
#     return render(request,'laptop_category.html')

@login_required
def all_laptops(request):
    laptop_category = Product.objects.filter(category_id=2)
    return render(request, 'laptop_category.html', {'laptop_category' : laptop_category })


# def phone_category(request):
#     return render(request,'phone_category.html')
@login_required(login_url = 'login')
def all_phones(request):
    phone_category = Product.objects.filter(category_id=1)
    return render(request, 'phone_category.html', {'phone_category': phone_category})


# def Product(request):
#     return HttpResponse("It is working")

# def Category(request):
#     return HttpResponse('Working')

# def Store(request):
#     return HttpResponse('Working')

# def Wishlist(request):
#     return HttpResponse('Working')

    