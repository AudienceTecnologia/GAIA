from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField, TextField, DateField
from django.db.models.fields.related import ForeignKey, ManyToManyField

from aulas.models import Aula, Dia_De_Aula_Disponivel, Matricula

TIPO_USUARIO = [
    ('professor', 'Professor'),
    ('aluna', 'Aluna'),
]

class User(AbstractUser):
    Tipo                        = CharField(max_length=255, choices=TIPO_USUARIO, blank=True, null=True)
    Telefone                    = CharField(max_length=255, blank=True, null=True)
    CPF                         = CharField(max_length=255, blank=True, null=True)
    Data_De_Nascimento          = DateField(blank=True, null=True)

class Aluna(models.Model):
    User                        = ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Matriculas                  = ManyToManyField(Matricula, blank=True)

class Local(models.Model):
    CEP                         = CharField(max_length=255, blank=True, null=True)
    Endereco                    = CharField(max_length=255, blank=True, null=True)
    Bairro                      = CharField(max_length=255, blank=True, null=True)
    Numero                      = CharField(max_length=255, blank=True, null=True)

class Professor(models.Model):
    User                        = ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    Bio                         = TextField(blank=True, null=True)
    Aulas                       = ManyToManyField(Aula, blank=True)
    Local                       = ManyToManyField(Local, blank=True)
    Dias_De_Aula_Disponiveis    = ManyToManyField(Dia_De_Aula_Disponivel, blank=True)