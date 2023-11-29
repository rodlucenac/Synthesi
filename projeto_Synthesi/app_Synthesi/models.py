from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Adicione campos específicos do perfil (por exemplo, é_professor, é_gestao, etc.)

class Alunos(models.Model):
    nome = models.TextField(max_length=255)
    turma = models.TextField(max_length=255)
    idade = models.CharField(max_length=100)

class ButtonColor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, default='rgb(255, 255, 255)')
