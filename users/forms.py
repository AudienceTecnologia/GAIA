from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'Data_De_Nascimento', 'email', 'Telefone', 'CPF', 'password1', 'password2')