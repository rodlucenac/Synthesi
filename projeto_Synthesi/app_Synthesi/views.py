from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Alunos, ButtonColor
from django.http import JsonResponse

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

def pagina_monitoramento(request, nome, turma, idade):
    print(nome, turma, idade)
    context = {'nome': nome, 'turma': turma, 'idade': idade}
    return render(request, 'monitoramento.html', context)

def pagina_presenca(request):
    return render(request, 'presenca.html')

def pagina_musica(request):
    return render(request, 'musica.html')

def pagina_autoavaliacao(request, nome=None, turma=None, idade=None):
    if nome is None or turma is None or idade is None:
        # Se os argumentos não foram fornecidos, você pode buscar essas informações de outra forma.
        # Por exemplo, você pode buscar essas informações do banco de dados ou usar dados padrão.
        # Aqui estou apenas dando um exemplo fixo, ajuste conforme necessário.
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10
    print(nome, turma, idade)
    context = {'nome': nome, 'turma': turma, 'idade': idade}
    return render(request, 'autoavaliacao.html', context)

def pagina_reunioes(request, nome=None, turma=None, idade=None):
    if nome is None or turma is None or idade is None:
        # Se os argumentos não foram fornecidos, você pode buscar essas informações de outra forma.
        # Por exemplo, você pode buscar essas informações do banco de dados ou usar dados padrão.
        # Aqui estou apenas dando um exemplo fixo, ajuste conforme necessário.
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10
    print(nome, turma, idade)
    context = {'nome': nome, 'turma': turma, 'idade': idade}
    return render(request, 'hist_reunioes.html', context)

def pagina_atividades(request, nome=None, turma=None, idade=None):
    if nome is None or turma is None or idade is None:
        # Se os argumentos não foram fornecidos, você pode buscar essas informações de outra forma.
        # Por exemplo, você pode buscar essas informações do banco de dados ou usar dados padrão.
        # Aqui estou apenas dando um exemplo fixo, ajuste conforme necessário.
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10

    # Modifique esta linha para garantir que você esteja usando o campo correto para a consulta
    button_color, created = ButtonColor.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Lógica para alterar a cor do botão
        current_color = button_color.color

        if current_color == 'rgb(255, 255, 255)':
            next_color = 'rgb(255, 0, 0)'  # Vermelho
        elif current_color == 'rgb(255, 0, 0)':
            next_color = 'rgb(0, 0, 255)'  # Azul
        else:
            next_color = 'rgb(255, 255, 255)'  # Branco

        # Atualize a cor no banco de dados
        button_color.color = next_color
        button_color.save()

    context = {'nome': nome, 'turma': turma, 'idade': idade, 'button_color': button_color.color}
    return render(request, 'atividades.html', context)

def pagina_eueomundo(request):
    alunos = Alunos.objects.all() 
    for i, aluno in enumerate(alunos):
        aluno.top = 150 + (i // 4) * 200  # Ajuste os valores conforme necessário
        aluno.left = 20 + (i % 4) * 200   # Ajuste os valores conforme necessário 
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


def alterar_cor(request, nome, turma, idade):
    # Recupere ou crie uma instância de ButtonColor associada ao usuário
    button_color, created = ButtonColor.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Lógica para alterar a cor do botão
        current_color = button_color.color

        if current_color == 'rgb(255, 255, 255)':
            next_color = 'rgb(255, 0, 0)'  # Vermelho
        elif current_color == 'rgb(255, 0, 0)':
            next_color = 'rgb(0, 0, 255)'  # Azul
        else:
            next_color = 'rgb(255, 255, 255)'  # Branco

        # Atualize a cor no banco de dados
        button_color.color = next_color
        button_color.save()

    return JsonResponse({'color': button_color.color})





