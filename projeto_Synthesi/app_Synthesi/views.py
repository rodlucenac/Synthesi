from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

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
    return render(request, 'eu_eo_mundo.html')
