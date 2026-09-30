from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# VIEWS -> retornam algo, são funções, request -> response
# View responsável pela tela inicial do paciente
def paciente_view(request):
    print('Página paciente funcionou')
    return HttpResponse('Página inicial do paciente')


