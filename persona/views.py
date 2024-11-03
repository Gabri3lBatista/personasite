from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Neurodivergente, Problemas, Solucoes
from .forms import PersonaForm, SolucaoForm, ProblemaForm
from weasyprint import HTML
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import Http404
import random
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Persona, Neurodivergente, Problemas, Solucoes
from .forms import PersonaForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
import tempfile
from django.conf import settings

from urllib.parse import urljoin




# Função para a página principal
@login_required
def main_page(request):
    return render(request, 'index.html')

@login_required
def sobre_page(request):
    return render(request, 'sobre.html')


# Função para listar todas as personas
@login_required
def persona_list(request):
    personas = Persona.objects.filter(user=request.user).order_by('nome')  # Adicione uma ordenação aqui
    neurodivergentes = Neurodivergente.objects.all()

    paginator = Paginator(personas, 5)
    page_number = request.GET.get('page') or 1
    page_number = int(page_number)

    try:
        personas_paginadas = paginator.page(page_number)
    except EmptyPage:
        personas_paginadas = paginator.page(paginator.num_pages)

    success_message = request.session.pop('success_message', None)

    return render(request, 'personas/persona_list.html', {
        'personas': personas_paginadas, 
        'neurodivergentes': neurodivergentes, 
        'paginator': paginator,
        'success_message': success_message
    })
    
    
#ramdomizar as cores

def random_color():
    colors = ['bg-primary', 'bg-secondary', 'bg-success', ]
    return random.choice(colors)


# Função para exibir informações detalhadas da persona
@login_required
def persona_info(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    color = random_color()

    if persona.user != request.user:
        return redirect('persona:persona_list')

    neurodivergencias = persona.neurodivergente.all()
    info_neurodivergencias = []

    for neurodivergencia in neurodivergencias:
        problemas = Problemas.objects.filter(neurodivergente=neurodivergencia, id__in=persona.problemas.all())
        problemas_com_solucoes = []

        for problema in problemas:
            solucoes = Solucoes.objects.filter(problema=problema)
            problemas_com_solucoes.append({
                'id': problema.id,  # Adiciona o ID do problema
                'descricao': problema.descricao,
                'solucoes': solucoes
            })

        info_neurodivergencias.append({
            'neurodivergencia': neurodivergencia,
            'problemas': problemas_com_solucoes,
        })

    context = {
        'persona': persona,
        'info_neurodivergencias': info_neurodivergencias,
        'random_colors': color,
    }

    return render(request, 'personas/persona_info.html', context)
# Função para exibir soluções para um problema específico
@login_required
def problema_solucoes(request, pk):
    problema = get_object_or_404(Problemas, pk=pk)
    solucoes = Solucoes.objects.filter(problema=problema)

    solucoes_detalhadas = [
        {
            'id': solucao.id,
            'nome': solucao.nome,
            'descricao': solucao.descricao,
            'por_que_resolver': solucao.por_que_resolver,
            'exemplo_texto': solucao.exemplo_texto,
            'exemplo_foto': solucao.exemplo_foto.url if solucao.exemplo_foto else None,
        }
        for solucao in solucoes
    ]

    return JsonResponse({
        'problem_title': problema.descricao,  # Use descrição em vez de nome
        'solucoes': solucoes_detalhadas
    })
# Função para criar uma nova persona
@login_required
def get_solutions(request):
    problem_id = request.GET.get('problem_id')
    solucoes = Solucoes.objects.filter(problema_id=problem_id).values('id', 'nome')
    return JsonResponse({'solucoes': list(solucoes)})


@login_required
def persona_create(request):
    neurodivergentes_names = ['Dislexia', 'Autismo', 'TDAH']
    for neuro_name in neurodivergentes_names:
        Neurodivergente.objects.get_or_create(nome=neuro_name)

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = form.save(commit=False)
            persona.user = request.user
            persona.save()
            neurodivergentes_escolhidos = form.cleaned_data.get('neurodivergente')
            print(f'Neurodivergentes escolhidos: {neurodivergentes_escolhidos}')  # Debug
            persona.neurodivergente.set(neurodivergentes_escolhidos)

            problemas_escolhidos = form.cleaned_data.get('problemas')
            print(f'Problemas escolhidos: {problemas_escolhidos}')  # Debug
            if problemas_escolhidos:
                persona.problemas.set(problemas_escolhidos)
            
            persona.save()
            messages.success(request, 'Persona criada com sucesso!')
            request.session['success_message'] = 'Persona criada com sucesso!'
            return redirect('persona:persona_list')
        else:
            # Para debug
            print(f'Erros do formulário: {form.errors}')
    else:
        form = PersonaForm()

    return render(request, 'personas/persona_create.html', {'form': form})
# Função para atualizar uma persona existente
@login_required
def persona_update(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if persona.user != request.user:
        return redirect('persona:persona_list')

    if request.method == "POST":
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            persona = form.save(commit=False)
            neurodivergentes_escolhidos = form.cleaned_data.get('neurodivergente')
            persona.neurodivergente.set(neurodivergentes_escolhidos)
            persona.problemas.set(form.cleaned_data.get('problemas'))
            persona.save()
            return redirect('persona:persona_info', pk=persona.pk)
    else:
        form = PersonaForm(instance=persona)

    return render(request, 'personas/persona_update.html', {'form': form})

# Função para excluir uma persona
@login_required
def persona_delete(request, pk):
    persona = get_object_or_404(Persona, pk=pk)

    if request.method == "POST":
        persona.delete()
        return redirect('persona:persona_list')

    return render(request, 'personas/persona_delete.html', {'persona': persona})



@login_required
def fetch_problems(request):
    neurodivergente_ids = request.GET.get('neurodivergente_ids', '').split(',')
    
    # Filtrando valores vazios ou inválidos
    neurodivergente_ids = [id for id in neurodivergente_ids if id.isdigit() and id]
    
    if neurodivergente_ids:
        print("Neurodivergente IDs recebidos:", neurodivergente_ids)  # Verifique os IDs recebidos

        # Filtra os problemas com base nos neurodivergente_ids válidos
        problemas = Problemas.objects.filter(neurodivergente__id__in=neurodivergente_ids).distinct()
        print("Problemas encontrados:", problemas)  # Verifique os problemas encontrados

        problemas_por_neurodivergencia = {}
        for problema in problemas:
            neurodivergencia = problema.neurodivergente.nome
            if neurodivergencia not in problemas_por_neurodivergencia:
                problemas_por_neurodivergencia[neurodivergencia] = []
            problemas_por_neurodivergencia[neurodivergencia].append(problema)

        # Renderiza o template e retorna o HTML gerado
        html = render_to_string('personas/problemas_list.html', {
            'problemas_por_neurodivergencia': problemas_por_neurodivergencia
        })
        return JsonResponse({'html': html})
    else:
        # Se nenhum neurodivergente_id for válido, retorna um HTML vazio
        return JsonResponse({'html': ''})

@login_required
def solution_detail(request, id):
    solution = get_object_or_404(Solucoes, pk=id)
    
    # Gerar a URL completa da imagem de exemplo
    exemplo_foto_url = request.build_absolute_uri(solution.exemplo_foto.url)
    exemplo_foto_url = exemplo_foto_url.replace('/app/media/', '/')  
    
    # Retorne os dados em formato JSON
    return JsonResponse({
        'descricao': solution.descricao,
        'por_que_resolver': solution.por_que_resolver,
        'exemplo_texto': solution.exemplo_texto,
        'exemplo_foto': exemplo_foto_url ,  # Certifique-se de retornar a URL gerada corretamente
    })

# Função para gerar o PDF

@login_required
def generate_pdf(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    color = random_color()

    neurodivergencias = persona.neurodivergente.all()
    info_neurodivergencias = []

    for neurodivergencia in neurodivergencias:
        problemas = Problemas.objects.filter(neurodivergente=neurodivergencia, id__in=persona.problemas.all())
        solucoes = Solucoes.objects.filter(problema__in=problemas)

        info_neurodivergencias.append({
            'neurodivergencia': neurodivergencia,
            'problemas': problemas,
            'solucoes': [
                {
                    'descricao': solucao.descricao,
                    'por_que_resolver': solucao.por_que_resolver,
                    'exemplo_texto': solucao.exemplo_texto,
                    'exemplo_foto': solucao.exemplo_foto.url if solucao.exemplo_foto else None,
                }
                for solucao in solucoes
            ]
        })

    html_string = render_to_string('personas/info_persona_pdf.html', {
        'persona': persona,
        'info_neurodivergencias': info_neurodivergencias,
        'random_color': color,
    })

    html = HTML(string=html_string)
    result = html.write_pdf()

    response = HttpResponse(result, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename=persona_{persona_id}.pdf'
    return response



@login_required
def fetchs(request):
    neurodivergente_id = request.GET.get('neurodivergente_id')
    problemas = Problemas.objects.filter(neurodivergente_id=neurodivergente_id)
    problemas_html = ''.join([f'<option value="{p.id}">{p.descricao}</option>' for p in problemas])

    return JsonResponse({'html': problemas_html})
#CRIAR PROBLEMA 

@login_required
def fetchs_neuro(request):
    neurodivergencia_id = request.GET.get('neurodivergencia_id')
    problemas = Problemas.objects.filter(neurodivergente_id=neurodivergencia_id)
    problemas_data = [{'id': problema.id, 'descricao': problema.descricao} for problema in problemas]
    return JsonResponse({'problemas': problemas_data})

@login_required
def criar_problema(request):
    if request.method == 'POST':
        form = ProblemaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona:listar_problemas')  # Redirecione após o sucesso
    else:
        form = ProblemaForm()
    return render(request, 'neuro/criar_problema.html', {'form': form})

#EDITAR PROBLEMA
@login_required
def update_problema(request, problema_id):
    problema = get_object_or_404(Problemas, id=problema_id)
    if request.method == 'POST':
        form = ProblemaForm(request.POST, instance=problema)
        if form.is_valid():
            form.save()
            return redirect('persona:listar_problemas')  # Redireciona após o sucesso
    else:
        form = ProblemaForm(instance=problema)
    return render(request, 'neuro/update_problema.html', {'form': form})

#DELETA PROBLEMAS
@login_required
def delete_problema(request, problema_id):
    problema = get_object_or_404(Problemas, id=problema_id)
    if request.method == 'POST':
        problema.delete()
        return redirect('persona:listar_problemas')  # Redireciona após a exclusão
    return render(request, 'neuro/delete_problema.html', {'problema': problema})

#LISTAR PROBLEMAS

@login_required
def criar_solucao(request):
    if request.method == 'POST':
        form = SolucaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('persona:listar_problemas')  # Redirecione após o sucesso
    else:
        form = SolucaoForm()
    return render(request, 'neuro/criar_solucao.html', {'form': form})

@login_required
def update_solucao(request, solucao_id):
    solucao = get_object_or_404(Solucoes, id=solucao_id)
    if request.method == 'POST':
        form = SolucaoForm(request.POST, instance=solucao)
        if form.is_valid():
            form.save()
            return redirect('persona:listar_solucoes')  # Redireciona após o sucesso
    else:
        form = SolucaoForm(instance=solucao)
    return render(request, 'neuro/update_solucao.html', {'form': form})

@login_required
def delete_solucao(request, solucao_id):
    solucao = get_object_or_404(Solucoes, id=solucao_id)
    if request.method == 'POST':
        solucao.delete()
        return redirect('persona:listar_solucoes')  # Redireciona após a exclusão
    return render(request, 'neuro/delete_solucao.html', {'solucao': solucao})

@login_required
def listar_problemas(request):
    neurodivergencia_id = request.GET.get('neurodivergencia_id')
    
    if neurodivergencia_id:
        problemas = Problemas.objects.filter(neurodivergente_id=neurodivergencia_id)
    else:
        problemas = Problemas.objects.all()  # Exibir todos se nenhuma neurodivergência for selecionada

    neurodivergencias = Neurodivergente.objects.all()  # Para o filtro no frontend

    return render(request, 'neuro/listar_problemas.html', {
        'problemas': problemas,
        'neurodivergencias': neurodivergencias
    })

@login_required
def listar_solucoes(request):
    neurodivergencia_id = request.GET.get('neurodivergencia_id')
    problema_id = request.GET.get('problema_id')
    
    # Filtrar os problemas com base na neurodivergência selecionada
    problemas = Problemas.objects.all()
    if neurodivergencia_id:
        problemas = problemas.filter(neurodivergente_id=neurodivergencia_id)
    
    # Filtrar as soluções com base no problema selecionado
    solucoes = Solucoes.objects.all()
    if problema_id:
        solucoes = solucoes.filter(problema_id=problema_id)
    
    neurodivergencias = Neurodivergente.objects.all()

    return render(request, 'neuro/listar_solucoes.html', {
        'solucoes': solucoes,
        'problemas': problemas,
        'neurodivergencias': neurodivergencias,
        'neurodivergencia_id': neurodivergencia_id,
        'problema_id': problema_id
    })
    
    
    
    
def persona_image(request):
    img_url = request.GET.get('img')
    if not img_url:
        raise Http404('Imagem não encontrada')
    return render(request, 'personas/persona_image.html', {'img_url': img_url})