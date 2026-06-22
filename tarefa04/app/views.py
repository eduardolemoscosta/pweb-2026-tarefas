from django.shortcuts import render
from datetime import date
from .models import Tarefa

def index(request):
    tarefas = Tarefa.objects.all()
    hoje = date.today()
    
    for t in tarefas:
        t.atrasada = t.prazo < hoje and t.status != 'Concluída'
        
    total = len(tarefas)
    pendentes = sum(1 for t in tarefas if t.status == 'Pendente')
    em_andamento = sum(1 for t in tarefas if t.status == 'Em Andamento')
    concluidas = sum(1 for t in tarefas if t.status == 'Concluída')
    atrasadas = sum(1 for t in tarefas if t.atrasada)
        
    context = {
        'tarefas': tarefas,
        'hoje': hoje,
        'stats': {
            'total': total,
            'pendentes': pendentes,
            'em_andamento': em_andamento,
            'concluidas': concluidas,
            'atrasadas': atrasadas,
        }
    }
    return render(request, 'index.html', context)

def usuarios(request):
    lista_usuarios = [ { 'nome': 'João Silva', 'matricula': '2023001', 'idade': 20, 'cidade': 'Natal' }, 
                      { 'nome': 'Maria Souza', 'matricula': '2023002', 'idade': 21, 'cidade': 'Mossoró' }, 
                      { 'nome': 'Pedro Santos', 'matricula': '2023003', 'idade': 19, 'cidade': 'Parnamirim' }, 
                      { 'nome': 'Ana Beatriz', 'matricula': '2023004', 'idade': 22, 'cidade': 'Caicó' }, 
                      { 'nome': 'Lucas Oliveira', 'matricula': '2023005', 'idade': 18, 'cidade': 'Currais Novos' } 
                      ]
    
    context = {
        'usuarios': lista_usuarios
    }
    return render(request, 'usuarios.html', context)
