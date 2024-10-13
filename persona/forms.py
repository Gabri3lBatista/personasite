from django import forms
from .models import Persona, Neurodivergente, Problemas, Solucoes

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




class ProblemaForm(forms.ModelForm):
    class Meta:
        model = Problemas
        fields = ['neurodivergente', 'descricao']


        

class SolucaoForm(forms.ModelForm):
    neurodivergente = forms.ModelChoiceField(
        queryset=Neurodivergente.objects.all(),
        label="Neurodivergência",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    problema = forms.ModelChoiceField(
        queryset=Problemas.objects.none(),  # Inicialmente vazio até a neurodivergência ser escolhida
        label="Problema",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Solucoes
        fields = ['neurodivergente', 'problema', 'descricao', 'por_que_resolver', 'exemplo_texto', 'exemplo_foto', 'nome']

       # Personalizar os labels de cada campo
    labels = {
        'problema': 'Problema Relacionado',
        'descricao': 'Qual a solução?',
        'por_que_resolver': 'Por que resolver?',
        'exemplo_texto': 'Como fazer?',
        'exemplo_foto': 'Exemplo em Foto',
        'nome': 'Nome da Solução',
    }
    def __init__(self, *args, **kwargs):
        super(SolucaoForm, self).__init__(*args, **kwargs)
        if 'neurodivergente' in self.data:
            try:
                neurodivergente_id = int(self.data.get('neurodivergente'))
                self.fields['problema'].queryset = Problemas.objects.filter(neurodivergente_id=neurodivergente_id)
            except (ValueError, TypeError):
                self.fields['problema'].queryset = Problemas.objects.none()
        elif self.instance.pk:
            self.fields['problema'].queryset = self.instance.neurodivergente.problemas_set.all()