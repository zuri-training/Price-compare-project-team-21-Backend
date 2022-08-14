from webbrowser import get
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth import get_user_model


from .models import CustomUser

User = get_user_model()


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'input type':'text', 
            'placeholder':'Username' 
        })
        self.fields["email"].widget.attrs.update({
            'required':'',
            'input type':'email', 
            'placeholder':'Email Address' 
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'input id':"password", 
            'type':"password", 
            'placeholder':"Password"
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'input id':"conPassword", 
            'type':"password", 
            'placeholder':"Confirm Password"
        })
    #email = forms.EmailField(max_length=254, help_text='Required. Input a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "username")