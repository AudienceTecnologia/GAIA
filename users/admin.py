from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User, Aluna, Local, Professor


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos Personalizados", {"fields": ("Tipo", "Telefone", "CPF", "Data_De_Nascimento")}),
    )

admin.site.register(Aluna)
admin.site.register(Local)
admin.site.register(Professor)