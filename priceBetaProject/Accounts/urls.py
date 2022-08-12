from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('login/', views.login, name = "login"),
    path('password_reset_form/', views.password_reset_form, name = "password_reset_form"),
]