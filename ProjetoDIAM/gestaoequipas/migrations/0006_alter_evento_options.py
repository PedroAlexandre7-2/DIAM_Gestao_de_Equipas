# Generated by Django 4.1.7 on 2023-05-13 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoequipas', '0005_alter_response_response'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evento',
            options={'permissions': (('writeDeleteAlocacaoEventos', 'o utilizador pode criar eventos, apagar eventos e inscrever em eventos'),)},
        ),
    ]
