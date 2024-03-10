from django.contrib import admin

# Register your models here

from .models import Persona, Neurodivergente

admin.site.register(Persona)

admin.site.register(Neurodivergente)
