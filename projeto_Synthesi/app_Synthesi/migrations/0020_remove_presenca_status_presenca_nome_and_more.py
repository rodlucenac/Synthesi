# Generated by Django 4.2.5 on 2023-11-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Synthesi', '0019_remove_presenca_nome_remove_presenca_presenca_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presenca',
            name='status',
        ),
        migrations.AddField(
            model_name='presenca',
            name='nome',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='presenca',
            name='presenca',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
