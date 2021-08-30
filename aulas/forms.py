from django import forms
from django.forms import widgets
from .models import *

class MatriculaForm(forms.ModelForm):
    
    class Meta:
        model = Matricula
        fields = '__all__'