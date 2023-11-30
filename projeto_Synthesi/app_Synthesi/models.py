from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione campos específicos do perfil (por exemplo, é_professor, é_gestao, etc.)

class Alunos(models.Model):
    nome = models.TextField(max_length=255)
    turma = models.TextField(max_length=255)
    idade = models.TextField(max_length=255)


class Materias(models.Model):
    materia = models.TextField(max_length=255)

class Solicitacao(models.Model):
    msg = models.TextField(max_length=255)


class Presenca(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField()
    presenca = models.TextField(max_length=255)


