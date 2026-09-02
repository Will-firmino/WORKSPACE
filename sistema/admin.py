from django.contrib import admin
from sistema import models

@admin.register(models.Paciente) # Registo o Paciente no Portal do Python
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)