# Generated by Django 4.2.5 on 2023-11-30 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Synthesi', '0024_solicitacao_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='opcao',
            name='opc',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]