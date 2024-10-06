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
        fields = ['nome', 'idade', 'interesses', 'profissao', 'sexo', 'neurodivergente', 'problemas']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Para o caso de edição
        if self.instance.pk:
            # O queryset é filtrado com base nas neurodivergências da instância
            self.fields['problemas'].queryset = Problemas.objects.filter(
                neurodivergente__in=self.instance.neurodivergente.all()
            ).distinct()
            # Seleciona os problemas já marcados anteriormente
            self.fields['problemas'].initial = self.instance.problemas.all()
        
        # Para o caso de envio de dados (ao submeter o formulário)
        elif 'neurodivergente' in self.data:
            try:
                # Pega os IDs das neurodivergências no POST data
                neurodivergente_ids = self.data.getlist('neurodivergente')
                print(f'Neurodivergente IDs from data: {neurodivergente_ids}')  # Debug
                # Filtra problemas relacionados com as neurodivergências selecionadas
                self.fields['problemas'].queryset = Problemas.objects.filter(
                    neurodivergente__id__in=neurodivergente_ids
                ).distinct()
            except (ValueError, TypeError) as e:
                print(f'Error while filtering problemas: {e}')  # Debugging
                pass
        else:
            # Nenhum neurodivergente foi selecionado ainda
            self.fields['problemas'].queryset = Problemas.objects.none()
