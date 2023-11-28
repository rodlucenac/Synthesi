from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Alunos

def pagina_inicio(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = authenticate(request, usename = username, senha = senha)
        print(usuario, username, senha)
        if usuario is not None:
            login(request, usuario)
            return redirect('salas')
        else:
            messages.error (request, 'Usuario ou senha incorretos.')
    return render(request, 'inicio.html')



def pagina_cadastrop(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha1= request.POST.get('senha')
        senha2= request.POST.get('senha2')
        meu_usuario = User.objects.create_user(username, senha1)
        if senha1 != senha2:
            messages.error (request, 'Usuario ou senha incorretos.')
        else:
            meu_usuario.save()
            print(meu_usuario)
            return redirect('inicio')
    return render(request, 'cadastro_prof.html')


def pagina_cadastrog(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha1= request.POST.get('senha')
        senha2= request.POST.get('senha2')
        meu_usuario = User.objects.create_user(username, senha1)
        if senha1 != senha2:
            messages.error (request, 'Usuario ou senha incorretos.')
        else:
            meu_usuario.save()
            print(meu_usuario)
            return redirect('inicio')
    return render(request, 'cadastro_gestao.html')


    
def pagina_salas(request):
    return render(request, 'salas.html')

def pagina_monitoramento(request):
    return render(request, 'monitoramento.html')

def pagina_presenca(request):
    return render(request, 'presenca.html')

def pagina_musica(request):
    return render(request, 'musica.html')

def pagina_autoavaliacao(request):
    return render(request, 'autoavaliacao.html')

def pagina_eueomundo(request):
    alunos = Alunos.objects.all()  # Obtém todos os alunos do banco de dados
    return render(request, 'eu_eo_mundo.html', {'alunos': alunos})

def pagina_adicionar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        turma = request.POST.get('turma')
        idade = request.POST.get('idade')

        novo_aluno = Alunos(nome= nome, turma=turma, idade=idade)
        print(nome, turma, idade)
        novo_aluno.save()
        return redirect('salas')
    
    
    return render(request, 'adicionar.html')



