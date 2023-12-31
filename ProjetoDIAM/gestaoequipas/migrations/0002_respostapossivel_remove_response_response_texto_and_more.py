# Generated by Django 4.1.7 on 2023-05-13 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestaoequipas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespostaPossivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respostaPossivel', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='response',
            name='response_texto',
        ),
        migrations.RemoveField(
            model_name='response',
            name='votos',
        ),
        migrations.AddField(
            model_name='response',
            name='atleta',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestaoequipas.atleta'),
        ),
        migrations.AlterField(
            model_name='response',
            name='evento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestaoequipas.evento'),
        ),
        migrations.AddField(
            model_name='response',
            name='response',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestaoequipas.respostapossivel'),
        ),
    ]
