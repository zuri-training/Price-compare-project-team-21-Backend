from cgitb import html
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def login(request):
    return render(request,'login.html')

def password_reset_form(request):
    return render(request,'registration/password_reset_form.html')

def CustomUserCreationForm(request):
    form = CustomUserCreationForm()

    if request.method == "POST":


        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            email = request.POST['email']
            subject = 'Welcome to PriceBeta, the no.1 price-comparing website'
            message = f' Hi {username},thank you for choosing priceBeta, we will ensure you get the best products for the best price.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            form.save()
            messages.info(request, "Account created successfully, you can now login")
            return redirect("login")

    return render(request, "signup.html", {"form": form})

    