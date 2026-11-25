from django.shortcuts import render
from django.http import HttpResponse
from sistema.models import Medico

# Create your views here.
# VIEWS -> retornam algo, são funções, request -> response
# View responsável pela tela inicial do médico
def medico_index(request):
    return HttpResponse('Página inicial do Médico')

def medico_novo(request):
    return HttpResponse('Cadastrar novo Médico')

def medico_listar(request):
    medicos = Medico.objects.filter(ativo=True).order_by('nome')
    
    context = {
        'medicos': medicos,
    }
    return render(
        request,
        'medico/listagem_medico.html',
        context,
    )


