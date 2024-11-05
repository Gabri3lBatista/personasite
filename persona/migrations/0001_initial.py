# Generated by Django 4.2.16 on 2024-11-05 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Neurodivergente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('neurodivergente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.neurodivergente')),
            ],
        ),
        migrations.CreateModel(
            name='Solucoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('por_que_resolver', models.TextField()),
                ('exemplo_texto', models.TextField()),
                ('exemplo_foto', models.ImageField(blank=True, null=True, upload_to='exemplos/')),
                ('nome', models.CharField(max_length=100)),
                ('problema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.problemas')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('interesses', models.TextField(max_length=255)),
                ('profissao', models.CharField(max_length=100)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('neurodivergente', models.ManyToManyField(limit_choices_to=models.Q(('nome', 'Dislexia'), ('nome', 'Autismo'), ('nome', 'TDAH'), _connector='OR'), to='persona.neurodivergente')),
                ('problemas', models.ManyToManyField(blank=True, to='persona.problemas')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
