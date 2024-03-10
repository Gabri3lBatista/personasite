# Importações necessárias do Django
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Persona, Neurodivergente, Problemas, Solucoes
from .forms import PersonaForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import Http404
from random import shuffle

# Função para listar todas as personas

def main_page(request):
    return render(request, 'index.html')

@login_required
def persona_list(request):
    personas = Persona.objects.all().filter(user=request.user)
    neurodivergenete = Neurodivergente.objects.all()
    return render(request, 'personas/persona_list.html', {'personas': personas, 'neurodivergentes': neurodivergenete})

def persona_info(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if persona.user != request.user:
        return redirect('persona:persona_list')

    neurodivergencias = persona.neurodivergente.all()

    info_neurodivergencias = []
    for neurodivergencia in neurodivergencias:
        problemas = list(Problemas.objects.filter(neurodivergente=neurodivergencia))
        solucoes = []

        # Garanta que as soluções correspondam aos problemas
        for problema in problemas:
            solucoes_problema = Solucoes.objects.filter(problema=problema)
            solucoes.extend(list(solucoes_problema))

        # Randomize a ordem dos problemas e soluções
   

        info_neurodivergencias.append({
            'neurodivergencia': neurodivergencia,
            'problemas': problemas,
            'solucoes': solucoes,
        })

    context = {
        'persona': persona,
        'info_neurodivergencias': info_neurodivergencias,
    }

    return render(request, 'personas/persona_info.html', context)


@login_required
def persona_create(request):
    print("entrou")

    # Certifique-se de que as instâncias de Neurodivergente existam no banco de dados
    neurodivergentes_names = ['Dislexia', 'Autismo', 'TDAH']
    for neuro_name in neurodivergentes_names:
        Neurodivergente.objects.get_or_create(nome=neuro_name)

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.user = request.user
            persona.save()

            # Associe as neurodivergências escolhidas à persona
            neurodivergentes_escolhidos = form.cleaned_data.get('neurodivergente')
            persona.neurodivergente.set(neurodivergentes_escolhidos)
            persona.save()

            print("válido")
            return redirect('persona:persona_list')
        else:
            print(form.errors)
    else:
        form = PersonaForm()

    return render(request, 'personas/persona_create.html', {'form': form})

# Função para atualizar uma persona existente
@login_required
def persona_update(request, pk):
    # Obtém a persona pelo ID (pk)
    try:
        persona = Persona.objects.get(pk=pk)
    except Persona.DoesNotExist:
        raise Http404("A Persona não existe.")
        
    if persona.user != request.user:
        # Persona não pertence ao usuário, redirecione para uma página de erro ou outra página
        return redirect('persona:persona_list')  # 403.html é um template de erro padrão do Django para permissões

    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            # Salva as alterações da persona
            persona = form.save(commit=False)
            
            # Associe as neurodivergências escolhidas à persona
            neurodivergentes_escolhidos = form.cleaned_data.get('neurodivergente')
            persona.neurodivergente.set(neurodivergentes_escolhidos)
            
            persona.save()
            
            print("validoedita")
            # Redireciona para a lista de personas após a atualização
            return redirect('persona:persona_info', pk=persona.pk)
        else:
            print("não validoedita")
            print(form.errors)
    else:
        # Cria um formulário preenchido com os dados da persona para exibir no método GET
        form = PersonaForm(instance=persona)
    return render(request, 'personas/persona_update.html', {'form': form})
# Classe para lidar com a exclusão de uma persona usando uma View genérica do Django(DeleteView):
@login_required
def persona_delete(request, pk):
    persona = Persona.objects.get(pk=pk)

    if request.method == "POST":
        persona.delete()
        return redirect('persona:persona_list')

    return render(request, 'personas/persona_delete.html', {'persona': persona})

    
# Path: persona/urls.py
