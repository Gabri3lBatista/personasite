# Importações necessárias do Django
from django.shortcuts import render, redirect,  get_object_or_404
from .models import Persona
from .forms import PersonaForm
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Função para listar todas as personas

def main_page(request):
    return render(request, 'index.html')

@login_required
def persona_list(request):
    personas = Persona.objects.all().filter(user=request.user)
    return render(request, 'personas/persona_list.html', {'personas': personas})

# Função para criar uma nova persona
@login_required
def persona_create(request):
    print("entrou") 
    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.user = request.user
            persona.save()
            print("valido" )
            return redirect('persona:persona_list')
    else:
        print("não valido")
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
        return render(request, 'error_page.html', {'message': 'Você não tem permissão para acessar esta persona.'})

    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            print("validoedita")
            # Salva as alterações da persona
            persona = form.save(commit=False)
            persona.save()
            # Redireciona para a lista de personas após a atualização
            return redirect('persona:persona_list')
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
