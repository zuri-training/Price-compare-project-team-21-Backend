from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
#from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate

from .forms import SignUpForm

# Create your views here.
def SignUpView(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password = raw_password)
            auth_login(request, user)
            return redirect('index')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form':form})
    # form_class = CustomUserCreationForm
    # success_url = reverse_lazy("login")
    # template_name = "registration/signup.html"

def login(request):
    return render(request,'login.html')

