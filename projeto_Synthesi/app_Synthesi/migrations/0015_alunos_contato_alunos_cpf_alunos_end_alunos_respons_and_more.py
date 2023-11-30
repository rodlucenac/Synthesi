# Generated by Django 4.2.5 on 2023-11-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Synthesi', '0014_autoavaliacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='contato',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alunos',
            name='cpf',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alunos',
            name='end',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alunos',
            name='respons',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alunos',
            name='rh',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alunos',
            name='idade',
            field=models.IntegerField(),
        ),
    ]
