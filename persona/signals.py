# signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Neurodivergente, Problemas, Solucoes

@receiver(post_migrate)
def inicializar_dados(sender, **kwargs):
    if sender.name == 'persona':
        # Dicionário de dados: neurodivergência -> problema -> lista de soluções
        dados_neurodivergentes = {
            'Dislexia': {
                'Dificuldade em seguir instruções': ['11111111', '22222222', '212112212121'],
                'Dificuldades de memória': ['33333', '44444444', '55555555'],

            },
            'Autismo': {
                'Problema específico do Autismo': ['Solução 1 para Autismo', 'Solução 2 para Autismo', 'Solução 3 para Autismo'],
            },
            'TDAH': {
                'Problema específico do TDAH': ['Solução 1 para TDAH', 'Solução 2 para TDAH', 'Solução 3 para TDAH'],
            },
            # Adicione mais neurodivergências, problemas e soluções conforme necessário
        }

        for neurodivergencia_nome, problemas_solucoes in dados_neurodivergentes.items():
            # Crie instâncias de Neurodivergente
            neurodivergencia, _ = Neurodivergente.objects.get_or_create(nome=neurodivergencia_nome)

            for problema_nome, solucoes_lista in problemas_solucoes.items():
                # Associe problemas a cada Neurodivergente
                problema, _ = Problemas.objects.get_or_create(neurodivergente=neurodivergencia, descricao=problema_nome)

                # Associe soluções a cada Problema
                for solucao_descricao in solucoes_lista:
                    Solucoes.objects.get_or_create(problema=problema, descricao=solucao_descricao)
