from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
    ]

fieldsets = UserAdmin.fieldsets
add_fieldsets = UserAdmin.add_fieldsets 

admin.site.register(CustomUser, CustomUserAdmin)