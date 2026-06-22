from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

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
