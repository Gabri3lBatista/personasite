from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Neurodivergente, Problemas, Solucoes
import os
from django.conf import settings

@receiver(post_migrate)
def inicializar_dados(sender, **kwargs):
    if sender.name == 'persona':  # Certifique-se de que está verificando o nome correto do app

        dados_neurodivergentes = {
            'Dislexia': {
                'Problemas com Fontes': [
                    {
                        'descricao': 'Utilize fontes sans-serifadas, pois possibilitam distinguir e possuir um espaçamento mínimo adequado entre cada carácter. Obs: Mesmo assim, algumas podem conter caracteres semelhantes como Arial ou Helvetica.',
                        'por_que_resolver': 'Tipo de Fonte - Para pessoas com TDAH e dislexia, geralmente, fontes do tipo sans-serif são mais fáceis de distinguir seus caracteres individualmente além de possuírem um espaçamento mínimo adequado entre cada caractere monospacing, sendo assim, diminui a possibilidade do usuário confundir a identificação de caracteres, sem atrasar sua leitura.',
                        'exemplo_texto': 'Utilize fontes como Tiresias, Verdana ou  pois se pode distinguir entre as letras “I” maiúscula e “l” minuscula.',
                        'exemplo_foto': 'exemplos/exemplo1.jpg',  # Caminho relativo à pasta de mídia
                    },
                    {
                        'descricao': 'Para extensos parágrafos, tamanho de 12 pontos na fonte do corpo textual. Para subtítulos ou legendas, no mínimo, o tamanho de 9 pontos - tamanhos menores podem ser ilegíveis em algumas plataformas. Para títulos (cabeçalhos), use um tamanho de fonte que seja pelo menos 20% maior do que o texto normal.',
                        'por_que_resolver': 'Tamanho da fonte - Fontes no tamanho adequado conforme sua hierarquia da informação - isto é, ser capaz de discernir o que é um cabeçalho, subtítulo, parágrafo, legendas e afins - torna o texto fácil de ler em um relance, resultando uma a leitura mais rápida e fácil para todos devido ao baixo esforço cognitivo no ato de assimilar os caracteres quanto para manter o foco.',
                        'exemplo_texto': 'Garantir que um site ou aplicativo funcione tanto em modo retrato quanto em modo paisagem, a menos que uma orientação específica seja essencial.',
                        'exemplo_foto': 'exemplos/exemplo2.png',
                    },
                ],
                'Problemas com texto': [
                    {
                        'descricao': 'Considere distribuir seu texto em colunas menores a fim de facilitar a leitura. Costuma-se trabalhar com o padrão de 12 colunas em um ambiente desktop. Com isso, é ideal dispor o texto em colunas com 45 até 70 caracteres por linha. Forneça um espaçamento adequado entre cada coluna.',
                        'por_que_resolver': 'Texto em colunas - Quanto mais texto é apresentado ao usuário de um lado a outro da tela, mais difícil se torna a leitura devido ao esforço cognitivo necessário para acompanhar.',
                        'exemplo_texto': 'Quanto mais texto é apresentado ao usuário de um lado a outro da tela, mais difícil se torna a leitura devido ao esforço cognitivo necessário para acompanhar.',
                        'exemplo_foto': 'exemplos/exemplo3.png',
                    },
                    {
                        'descricao': '4.1.3 - Mensagens de status [AA] - Qualquer tipo de mensagem que é resultado de uma ação ou que informa o andamento de um processo e que seja relevante para a pessoa, deve ser transmitida sem que ocorra uma mudança de contexto (foco) na tela.',
                        'por_que_resolver': 'Minimizar a confusão e garantir que a pessoa esteja ciente do que está acontecendo sem perder o foco do que está fazendo.',
                        'exemplo_texto': 'Mostrar uma mensagem de carregamento na mesma página, sem redirecionar para outra tela.',
                        'exemplo_foto': None,
                    },
                ],
                # Adicione mais problemas e soluções conforme necessário...
            },
        }

        for neurodivergencia, problemas in dados_neurodivergentes.items():
            neurodivergente_obj, _ = Neurodivergente.objects.get_or_create(nome=neurodivergencia)
            for problema_descricao, solucoes in problemas.items():
                problema_obj, _ = Problemas.objects.get_or_create(neurodivergente=neurodivergente_obj, descricao=problema_descricao)
                for solucao in solucoes:
                    # Verifique se a solução já existe antes de criar
                    exemplo_foto = solucao.get('exemplo_foto')
                    if exemplo_foto:
                        exemplo_foto_path = os.path.join(settings.MEDIA_ROOT, exemplo_foto)
                    else:
                        exemplo_foto_path = None
                    
                    # Check if the solution already exists
                    solucao_obj, created = Solucoes.objects.get_or_create(
                        problema=problema_obj,
                        descricao=solucao['descricao'],
                        defaults={
                            'por_que_resolver': solucao['por_que_resolver'],
                            'exemplo_texto': solucao['exemplo_texto'],
                            'exemplo_foto': exemplo_foto_path
                        }
                    )

                    if not created:
                        # Update fields if necessary
                        solucao_obj.por_que_resolver = solucao['por_que_resolver']
                        solucao_obj.exemplo_texto = solucao['exemplo_texto']
                        solucao_obj.exemplo_foto = exemplo_foto_path
                        solucao_obj.save()
