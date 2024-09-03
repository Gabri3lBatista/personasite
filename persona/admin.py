from django.contrib import admin

# Register your models here

from .models import Persona, Neurodivergente, Solucoes

admin.site.register(Persona)

admin.site.register(Neurodivergente)

admin.site.register(Solucoes)
