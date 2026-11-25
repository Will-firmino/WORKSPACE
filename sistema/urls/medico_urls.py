from django.urls import path
from sistema.views import medico_index, medico_novo, medico_listar

urlpatterns = [
    path('medico/', medico_index), # vollmed.com/medico
    path('medico/novo/', medico_novo, name='medico-create'),
    path('medico/listagem/', medico_listar, name='medico-list'),
]
