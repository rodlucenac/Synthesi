# Generated by Django 4.2.5 on 2023-11-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Synthesi', '0016_remove_alunos_contato_remove_alunos_cpf_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alunos',
            name='idade',
            field=models.CharField(max_length=255),
        ),
    ]