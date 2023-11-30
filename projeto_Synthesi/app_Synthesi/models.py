from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione campos específicos do perfil (por exemplo, é_professor, é_gestao, etc.)

<<<<<<< HEAD
=======
class Alunos(models.Model):
    nome = models.TextField(max_length=255)
    turma = models.TextField(max_length=255)
    idade = models.CharField(max_length=100)
    cor = models.CharField(max_length=7, default="#FFFFFF")

>>>>>>> 5752a915800ef826898edfc31a9cda8400410dcb
class Materias(models.Model):
    materia = models.TextField(max_length=255)

class Solicitacao(models.Model):
    msg = models.TextField(max_length=255)

class Aluno(models.Model):
    nome = models.TextField(max_length=255)
    idade = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    rh = models.TextField(max_length=255)
    end = models.TextField(max_length=255)
    respons = models.TextField(max_length=255)
    contato = models.TextField(max_length=255)