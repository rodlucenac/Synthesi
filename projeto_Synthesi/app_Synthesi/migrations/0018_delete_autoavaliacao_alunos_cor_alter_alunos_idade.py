# Generated by Django 4.2.5 on 2023-11-30 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Synthesi', '0017_alter_alunos_idade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autoavaliacao',
        ),
        migrations.AddField(
            model_name='alunos',
            name='cor',
            field=models.CharField(default='#FFFFFF', max_length=7),
        ),
        migrations.AlterField(
            model_name='alunos',
            name='idade',
            field=models.CharField(max_length=100),
        ),
    ]