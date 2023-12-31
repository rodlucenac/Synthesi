from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .models import Alunos, Materias, Solicitacao, Presenca, Opcao
from django.http import JsonResponse
import json

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
        # Se os argumentos não foram fornecidos, você pode buscar essas informações de outra forma.
        # Por exemplo, você pode buscar essas informações do banco de dados ou usar dados padrão.
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10

    context = {'nome': nome, 'turma': turma, 'idade': idade}

    if request.method == 'POST':
        opc = request.POST.get('opcao')
        opcao = Opcao.objects.create(opc=opc, nome=nome)
        opcao.save()
        return redirect('monitoramento', nome=nome, turma=turma, idade=idade)
    print(nome, turma, idade)
    return render(request, 'autoavaliacao.html', context)

def pagina_solicitar(request, nome=None, turma=None, idade=None):
    if nome is None or turma is None or idade is None:
        # Se os argumentos não foram fornecidos, você pode buscar essas informações de outra forma.
        # Por exemplo, você pode buscar essas informações do banco de dados ou usar dados padrão.
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10
    
    
    if request.method == 'POST':
        msg = request.POST.get('msg')
        nova_msg = Solicitacao(msg=msg, nome=nome)
        print(msg)
        nova_msg.save()
        context = {'nome': nome, 'turma': turma, 'idade': idade}
        return render(request, 'hist_reunioes.html', context)
    else:
        if nome is None or turma is None or idade is None:
            # Se os argumentos não foram fornecidos, você pode buscar essas informações de outra forma.
            # Por exemplo, você pode buscar essas informações do banco de dados ou usar dados padrão.
            # Aqui estou apenas dando um exemplo fixo, ajuste conforme necessário.
            nome = "Aluno Padrão"
            turma = "Turma Padrão"
            idade = 10
        print(nome, turma, idade)
        context = {'nome': nome, 'turma': turma, 'idade': idade}
        return render(request, 'solicitar_reunioes.html', context)
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
        nome = "Aluno Padrão"
        turma = "Turma Padrão"
        idade = 10
    
    if request.method == 'POST':
        data = request.POST.get('data')
    
        if 'presente' in request.POST:
            presenca = 'PRESENTE'
        elif 'faltou' in request.POST:
            presenca = 'FALTOU'
        else:
            # Lógica de tratamento caso nenhum botão tenha sido pressionado
            presenca = None
        if nome and data and presenca:
            # Obtenha todos os objetos aluno com base no nome
            alunos = Alunos.objects.filter(nome=nome)
            # Verifique se há exatamente um objeto retornado
            if alunos.count() == 1:
                aluno = alunos.first()
                # Crie uma nova instância do modelo Presenca e salve no banco de dados
                nova_presenca = Presenca(nome=aluno.nome, data=data, presenca=presenca)
                nova_presenca.save()
                return redirect('eu_eo_mundo')
            else:
                # Lógica para lidar com mais de um objeto retornado (se necessário)
                pass
    alunos = Alunos.objects.all()
    materias = Materias.objects.all()
    context = {'nome': nome, 'turma': turma, 'idade': idade, 'alunos': alunos, 'materias': materias}
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