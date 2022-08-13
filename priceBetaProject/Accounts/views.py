from django.contrib import messages
from django import http
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
#from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.conf import settings

from .forms import SignUpForm

# Create your views here.
def SignUpView(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            email = request.POST['email']
            subject = "Welcome to PriceBeta"
            message = f'Hi {username}, thank you for choosing PriceBeta, we will help you save your money while giving you quality products. At PriceBeta, you will have a wide range of products to compare and choose from.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
           
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            messages.success(request, 'Your account has been created successfully, you can now log in')
            return render(request, 'registration/signup.html')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)
            #return http.HttpResponseRedirect('signup')
            auth_login(request, user)
        return redirect('login')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})
    # form_class = CustomUserCreationForm
    # success_url = reverse_lazy("login")
    # template_name = "registration/signup.html"

def login(request):
    return render(request,'login.html')

