from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def pagina_inicio(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('senha')
        usuario = authenticate(request, email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('salas')
        else:
            messages.error(request, 'Email ou senha incorretos.')
    else:
        print("Não é uma requisição POST")
    return render(request, 'inicio.html')


    

def pagina_cadastro_prof(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password= request.POST.get('senha1')
        senha2= request.POST.get('senha2')
        
        if password != senha2:
            messages.error(request, 'Suas senhas não são iguais.')
        else:
            meu_usuario = User.objects.create_user(email, password)
            meu_usuario.save()
            return redirect('inicio')
    return render(request, 'cadastro_prof.html')
    
def pagina_cadastro_gest(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password= request.POST.get('senha1')
        senha2= request.POST.get('senha2')
        print(email, password, senha2)
        
        if password != senha2:
            messages.error(request, 'Suas senhas não são iguais.')
        else:
            meu_usuario = User.objects.create_user(email, password)
            meu_usuario.save()
            print(meu_usuario)
            return redirect('inicio')
    return render(request, 'cadastro_gestao.html')

def pagina_salas(request):
    return render(request, 'salas.html')

def pagina_eu_mundo(request):
    return render(request, 'eu_eo_mundo.html')
