from django.urls import path
from . import views

urlpatterns = [
    path('', views.escolher_nivel, name='escolher_nivel'),
    path('escolher_aula/<int:id>', views.escolher_aula, name='escolher_aula'),
    path('home/<int:id>', views.home, name='home'),
    path('selecionar_data/<int:id>', views.selecionar_data, name='selecionar_data'),
    path('resumo/<int:id>', views.resumo, name='resumo'),
]
