from django import forms
from .models import Persona
from users.models import Usuario
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

  