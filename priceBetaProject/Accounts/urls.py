from django.urls import path, reverse_lazy
from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path('login/', views.loginpage, name = "login1"),
    path('password_reset_form/', views.password_reset_form, name = "password_reset_form"),
]