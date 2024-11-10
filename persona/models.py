from django.db import models
from users.models import Usuario

class Neurodivergente(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Problemas(models.Model):
    neurodivergente = models.ForeignKey(Neurodivergente, on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return self.descricao

class Solucoes(models.Model):
    problema = models.ForeignKey(Problemas, on_delete=models.CASCADE)
    descricao = models.TextField()
    por_que_resolver = models.TextField()  # Campo para "por que resolver"
    exemplo_texto = models.TextField()  # Campo para explicar o exemplo em texto
    exemplo_foto = models.ImageField(upload_to='exemplos/', blank=True, null=True)  # Campo para exemplo em foto
    nome = models.CharField(max_length=100)
    
    def clean(self):
        if not self.exemplo_texto and not self.exemplo_foto:
            raise ValidationError('Pelo menos um exemplo (texto ou foto) deve ser fornecido.')
    
    def __str__(self):
        return self.descricao

class Persona(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]

    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    interesses = models.TextField(max_length=255)
    profissao = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    neurodivergente = models.ManyToManyField('Neurodivergente', 
        limit_choices_to=models.Q(nome='Dislexia') | models.Q(nome='Autismo') | models.Q(nome='TDAH'))
    problemas = models.ManyToManyField('Problemas', blank=True)

    def __str__(self):
        return self.nome
