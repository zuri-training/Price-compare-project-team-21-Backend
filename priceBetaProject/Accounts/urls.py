from django.urls import path, reverse_lazy
from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", views.SignUpView, name="signup"),
    path('login/', views.login, name = "login"),
]