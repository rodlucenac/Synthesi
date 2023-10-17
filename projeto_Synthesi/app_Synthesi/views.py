from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def pagina_inicio(request):
    return render(request, 'inicio.html')

def pagina_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        senha1 = request.POST.get('senha')
        usuario = authenticate(request, username = username, password = senha1)
        print(usuario, username, senha1)
        if usuario is not None:
            login(request, usuario)
            return redirect('salas')
        else:
            messages.error (request, 'Email ou senha incorretos.')
    return render(request, 'login.html')
    

def pagina_cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha1= request.POST.get('senha1')
        senha2= request.POST.get('senha2')
        
        if senha1 != senha2:
            messages.error(request, 'Suas senhas não são iguais.')
        else:
            meu_usuario = User.objects.create_user(username, email, senha1)
            meu_usuario.save()
            return redirect('login')
    return render(request, 'cadastro.html')
    
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
