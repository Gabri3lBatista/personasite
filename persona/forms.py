from django import forms
from .models import Persona, Neurodivergente, Problemas

class PersonaForm(forms.ModelForm):
    neurodivergente = forms.ModelMultipleChoiceField(
        queryset=Neurodivergente.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    problemas = forms.ModelMultipleChoiceField(
        queryset=Problemas.objects.none(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Persona
        fields = ['nome', 'idade', 'interesses','profissao', 'sexo', 'neurodivergente', 'problemas']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['problemas'].queryset = Problemas.objects.filter(neurodivergente__in=self.instance.neurodivergente.all()).distinct()
            self.fields['problemas'].initial = self.instance.problemas.all()
        elif 'neurodivergente' in self.data:
            try:
                neurodivergente_ids = self.data.getlist('neurodivergente')
                print(f'Neurodivergente IDs from data: {neurodivergente_ids}')  # Debug
                self.fields['problemas'].queryset = Problemas.objects.filter(neurodivergente__id__in=neurodivergente_ids).distinct()
            except (ValueError, TypeError) as e:
                print(f'Error while filtering problemas: {e}')  # Debug
                pass
        else:
            self.fields['problemas'].queryset = Problemas.objects.none()
