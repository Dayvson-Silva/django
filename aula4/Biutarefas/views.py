from django.shortcuts import render
from .models import Biutarefas


def get_tarefas(request):
    tarefas = Biutarefas.objects.all()
    context = {
        'tarefas' : tarefas
    }

    return render(request, 'Biutarefas.html', context)