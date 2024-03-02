from django.db import models
from users.models import Usuario 
class Persona(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    interesses = models.TextField(default='')

    def __str__(self):
        return self.nome