from django.db import models
from django.db.models import base
from django.db.models.fields import BooleanField, CharField, DateField, DateTimeField, IntegerField, TextField, TimeField
from django.db.models.fields.related import ForeignKey, ManyToManyField


class Nivel(models.Model):
    Nome                                = CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.Nome

class Aula(models.Model):
    Nome                                = CharField(max_length=255, blank=True, null=True)
    Nivel                               = ManyToManyField(Nivel, blank=True)
    Descricao                           = TextField(blank=True, null=True)
    Duracao                             = TimeField(blank=True, null=True)
    Quantidade_Maxima_De_Alunas         = IntegerField(blank=True, null=True)
    Aula_Filmada                        = BooleanField(default=False)
    Disponibilizacao_De_Equipamentos    = BooleanField(default=False)

    def __str__(self):
        return self.Nome

DIA_SEMANA = [
    ('Segunda', 'Segunda'),
    ('Terça', 'Terça'),
    ('Quarta', 'Quarta'),
    ('Quinta', 'Quinta'),
    ('Sexta', 'Sexta'),
    ('Sábado', 'Sábado'),
    ('Domingo', 'Domingo'),
]

class Frequencia(models.Model):
    Tipo = CharField(max_length=255, blank=True, null=True)
    Valor = IntegerField(blank=True, null=True)

    def __str__(self):
        return self.Tipo

class Dia_De_Aula_Disponivel(models.Model):
    Aula                                = ForeignKey(Aula, on_delete=models.CASCADE, blank=True, null=True)
    Nivel                               = ForeignKey(Nivel, on_delete=models.CASCADE, blank=True, null=True)
    Data                                = DateField(blank=True, null=True)
    Dia_Semana                          = CharField(max_length=255, choices=DIA_SEMANA, blank=True, null=True)
    Inicio                              = TimeField(blank=True, null=True)
    Fim                                 = TimeField(blank=True, null=True)
    Quantidade_Maxima_De_Alunas         = IntegerField(blank=True, null=True)
    Quantidade_Atual_De_Alunas          = IntegerField(default=0)

    def __str__(self):
        return "Dia: " + str(self.Data.strftime("%d/%m/%Y")) + " - " + str(self.Inicio.strftime("%H:%M")) + " às " + str(self.Fim.strftime("%H:%M"))

STATUS = [
    ('atrasado', 'Atrasado'),
    ('pago', 'Pago'),
    ('cancelado', 'Cancelado'),
]

class Matricula(models.Model):
    Nivel                               = ForeignKey(Nivel, on_delete=models.CASCADE, blank=True, null=True)
    Aula                                = ForeignKey(Aula, on_delete=models.CASCADE, blank=True, null=True)
    Frequencia                          = ForeignKey(Frequencia, on_delete=models.CASCADE, blank=True, null=True)
    Dia_De_Aula_Disponivel              = ManyToManyField(Dia_De_Aula_Disponivel, blank=True)
    Valor                               = CharField(max_length=255, blank=True, null=True)
    Termos_E_Condicoes                  = BooleanField(default=False)
    Status                              = CharField(max_length=255, choices=STATUS, blank=True, null=True)

    Dia_Semana                          = CharField(max_length=255, choices=DIA_SEMANA, blank=True, null=True)
    Inicio                              = TimeField(blank=True, null=True)
