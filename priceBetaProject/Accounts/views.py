from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth import login

# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def login(request):
    return render(request,'login.html')
