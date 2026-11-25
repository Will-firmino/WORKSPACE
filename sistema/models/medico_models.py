from django.db import models
from django.utils import timezone

class Medico(models.Model):
    nome = models.CharField(max_length=25) # Nome do médico.
    sobrenome = models.CharField(max_length=50) # Sobrenome do médico.
    email = models.EmailField() # Email de contato do médico.
    criacao_data = models.DateTimeField(default=timezone.now) # Data/hora do cadastro
    telefone = models.CharField(max_length=20) # Telefone de contato.
    crm = models.CharField(max_length=6) # CRM do médico.
    especialidade = models.CharField(max_length=50) # Especialidade do médico.
    mensagem = models.TextField(blank=True) # Campo opcional livre para mensagem.
    ativo = models.BooleanField(default=True) # Campo de exclusão lógica
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'