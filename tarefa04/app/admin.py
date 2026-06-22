from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'status', 'prazo')
    list_filter = ('status', 'prazo')
    search_fields = ('nome',)
