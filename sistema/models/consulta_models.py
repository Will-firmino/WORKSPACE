from django.db import models
from django.utils import timezone

from sistema.models.medico_models import Medico
from sistema.models.paciente_models import Paciente

class Consulta(models.Model):
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE) # Chave estrangeira
    medico_id = models.ForeignKey(Medico, on_delete=models.CASCADE) # Chave estrangeira
    data_consulta = models.DateTimeField(default=timezone.now) #Data/hota da consulta
    ativa = models.BooleanField(default=True) # Campo de exclusão lógica
    observacao = models.TextField(blank=True) # Anotação opcional
    status = models.CharField(
        default='A',
        max_length=1,
        choices=[
            ('A', 'Agendada'),
            ('X', 'Cancelada'),
            ('C', 'Confirmada'),
            ('R', 'Realizada'),
        ]
    )