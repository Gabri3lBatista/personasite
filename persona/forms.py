from django import forms
from .models import Persona, Neurodivergente


class PersonaForm(forms.ModelForm):
    neurodivergente = forms.ModelMultipleChoiceField(
        queryset=Neurodivergente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Persona
        fields = ['nome', 'idade', 'interesses', 'sexo', 'neurodivergente']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
   # Ajuste as escolhas do campo neurodivergente para mostrar apenas algumas opções
        allowed_neurodivergentes = Neurodivergente.objects.filter(nome__in=['Dislexia', 'Autismo', 'TDAH'])
        self.fields['neurodivergente'].queryset = allowed_neurodivergentes
        