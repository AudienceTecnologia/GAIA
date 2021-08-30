from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User as UserModel
from django.db.models import Max
from django.db.models import Q

from .models import *
from .forms import *
from users.forms import *
from users.models import *

def escolher_nivel(request):

    form = MatriculaForm()

    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        form.save()
        
        return redirect('escolher_aula/' + str(Matricula.objects.last().id))

    context = {'form': form}

    return render(request, 'escolher_nivel.html', context)

def escolher_aula(request, id):

    form = MatriculaForm(instance=get_object_or_404(Matricula, pk=id))

    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=get_object_or_404(Matricula, pk=id))
        form.save()
        
        ultima_matricula = Matricula.objects.last()

        return redirect('/home/' + str(ultima_matricula.id))

    context = {'form': form}

    return render(request, 'escolher_aula.html', context)

def home(request, id):

    matricula = get_object_or_404(Matricula, pk=id)

    form = MatriculaForm(instance=matricula)

    dia_semana = request.GET.get('dia_semana')
    horario = request.GET.get('horario')

    form.fields['Dia_De_Aula_Disponivel'].queryset = Dia_De_Aula_Disponivel.objects.filter(Quantidade_Atual_De_Alunas__lt=4).order_by('Inicio')
    
    if request.method == 'POST':
        frequencia = request.POST.get('Frequencia')

        form = MatriculaForm(request.POST, instance=matricula)
        form.save()

        ultima_matricula = Matricula.objects.last()

        return redirect('/resumo/' + str(ultima_matricula.id))

    context = {'form': form, 'matricula': matricula}

    return render(request, 'home.html', context)


def resumo(request, id):

    resumo = Matricula.objects.get(pk=id)

    resumo.Valor = resumo.Frequencia.Valor
    resumo.save()

    try:
        Dia_Semana1 = list(resumo.Dia_De_Aula_Disponivel.values_list('Dia_Semana')[0])[0]
    except:
        Dia_Semana1 = ''

    try:
        Dia_Semana2 = list(resumo.Dia_De_Aula_Disponivel.values_list('Dia_Semana')[1])[0]
    except:
        Dia_Semana2 = ''

    try:
        Dia_Semana3 = list(resumo.Dia_De_Aula_Disponivel.values_list('Dia_Semana')[2])[0]
    except:
        Dia_Semana3 = ''

    qtde_atual_alunas = list(resumo.Dia_De_Aula_Disponivel.values_list('Quantidade_Atual_De_Alunas'))

    qtdes = []

    for i in range(len(qtde_atual_alunas)):
        qtdes.append(int(qtde_atual_alunas[i][0]) + 1)

    id_dia = list(resumo.Dia_De_Aula_Disponivel.values_list('id'))

    ids = []

    for i in range(len(id_dia)):
        ids.append(id_dia[i][0])
    
    form = UserCreationForm()
    matriculaForm = MatriculaForm(instance=resumo)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

        Status = request.POST.get('Status')
        print(Status)
        
        resumo.Status = Status
        resumo.Termos_E_Condicoes = True
        resumo.Aluna = User.objects.last()
        resumo.save()

        ultima_aluna = User.objects.last()
        ultima_aluna.Tipo = "aluna"
        ultima_aluna.save()

        if resumo.Status == 'pago':
            for i in ids:
                dia_aula = Dia_De_Aula_Disponivel.objects.get(pk=i)
                dia_aula.Quantidade_Atual_De_Alunas = dia_aula.Quantidade_Atual_De_Alunas + 1
                dia_aula.save()
        
        return redirect('/')

    context = {'form': form, 'matriculaForm': matriculaForm, 'resumo': resumo, 'Dia_Semana1': Dia_Semana1, 'Dia_Semana2': Dia_Semana2, 'Dia_Semana3': Dia_Semana3}

    return render(request, 'resumo.html', context)