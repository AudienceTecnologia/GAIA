from django.contrib import admin

from .models import Nivel, Aula, Frequencia, Dia_De_Aula_Disponivel, Matricula

admin.site.register(Nivel)
admin.site.register(Aula)
admin.site.register(Frequencia)
admin.site.register(Dia_De_Aula_Disponivel)
admin.site.register(Matricula)