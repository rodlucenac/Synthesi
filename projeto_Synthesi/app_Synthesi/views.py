from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Aluno, Materias, Solicitacao
from .models import Alunos, Materias, Solicitacao
from django.http import JsonResponse

def atualizar_cor(request, aluno_id):
    if request.method == 'POST' and request.is_ajax():
        cor = request.POST.get('cor', '#FFFFFF')
        aluno = Alunos.objects.get(id=aluno_id)
        aluno.cor = cor
        aluno.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

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
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10
    print(nome, turma, idade)
    context = {'nome': nome, 'turma': turma, 'idade': idade}
    return render(request, 'autoavaliacao.html', context)


def pagina_solicitar(request, nome=None, turma=None, idade=None):
    if request.method == 'POST':
        msg = request.POST.get('msg')

        nova_msg = Solicitacao(msg=msg)
        print(msg)
        nova_msg.save()
        context = {'nome': nome, 'turma': turma, 'idade': idade}
        return render(request, 'hist_reunioes.html', context)
    else:
        if nome is None or turma is None or idade is None:
            nome = "Aluno Padrão"
            turma = "Turma Padrão"
            idade = 10
        print(nome, turma, idade)
        context = {'nome': nome, 'turma': turma, 'idade': idade}
        return render(request, 'solicitar_reunioes.html', context)


def pagina_reunioes(request, nome=None, turma=None, idade=None):
    if nome is None or turma is None or idade is None:
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10
    print(nome, turma, idade)
    context = {'nome': nome, 'turma': turma, 'idade': idade}
    return render(request, 'hist_reunioes.html', context)


def pagina_atividades(request, nome=None, turma=None, idade=None):
    if nome is None or turma is None or idade is None:
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10

    alunos = Alunos.objects.all()
    context = {'nome': nome, 'turma': turma, 'idade': idade, 'alunos':alunos}
    return render(request, 'atividades.html', context)

def pagina_eueomundo(request):
    alunos = Aluno.objects.all() 
    for i, aluno in enumerate(alunos):
        aluno.top = 150 + (i // 4) * 200
        aluno.left = 20 + (i % 4) * 200
    return render(request, 'eu_eo_mundo.html', {'alunos': alunos})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Aluno  # Certifique-se de que a importação do modelo está correta

def pagina_adicionar(request):
    if request.method == 'POST':
        try:
            # Captura os dados do formulário
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')
            cpf = request.POST.get('cpf')
            rh = request.POST.get('rh')
            end = request.POST.get('end')
            respons = request.POST.get('respons')
            contato = request.POST.get('contato')
            novo_aluno = Aluno(nome=nome, idade=idade, cpf=cpf, rh=rh, end=end, respons=respons, contato=contato)
            novo_aluno.save()
            return redirect('salas')
        except Exception as e:
            return HttpResponse(f"Ocorreu um erro: {e}", status=500)
    return render(request, 'adicionarAlunos.html')



def pagina_adicionarmateria(request):
    if request.method == 'POST':
        materia = request.POST.get('materia')

        nome = "exemplo_nome"
        turma = "exemplo_turma"
        idade = "exemplo_idade"

        novo_materia = Materias(materia=materia)
        print(materia)
        novo_materia.save()
        return redirect('atividades', nome=nome, turma=turma, idade=idade)
    
    
    return render(request, 'adicionar_materias.html')








