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
                        'descricao': 'Tipo de Fonte - Utilize fontes sans-serifadas, pois possibilitam distinguir e possuir um espaçamento mínimo adequado entre cada carácter. Obs: Mesmo assim, algumas podem conter caracteres semelhantes como Arial ou Helvetica.',
                        'por_que_resolver': 'Para pessoas com TDAH e dislexia, geralmente, fontes do tipo sans-serif são mais fáceis de distinguir seus caracteres individualmente além de possuírem um espaçamento mínimo adequado entre cada caractere monospacing, sendo assim, diminui a possibilidade do usuário confundir a identificação de caracteres, sem atrasar sua leitura.',
                        'exemplo_texto': 'Utilize fontes como Tiresias, Verdana ou  pois se pode distinguir entre as letras “I” maiúscula e “l” minuscula. ',
                        'exemplo_foto': 'exemplos/exemplo1.jpg',  # Caminho relativo à pasta de mídia
                    },
                    {
                        'descricao': '1.3.4 - Orientação [AA] - Nenhuma funcionalidade deve depender de uma determinada orientação de tela (exemplo: virar o celular na horizontal), a não ser que seja imprescindível para execução da função.',
                        'por_que_resolver': 'Evitar frustração e dificuldade de uso para indivíduos que possam ter problemas em mudar a orientação da tela.',
                        'exemplo_texto': 'Garantir que um site ou aplicativo funcione tanto em modo retrato quanto em modo paisagem, a menos que uma orientação específica seja essencial.',
                        'exemplo_foto': None,
                    },
                ],
                'Dificuldades de memória': [
                    {
                        'descricao': '3.2.6 - Ajuda consistente [A] - Se algumas opções de ajuda forem fornecidas em uma tela (exemplo: Dados de contato humano ou um sistema automatizado), este mesmo formato deverá ser igual em todas as outras telas que a ajuda for fornecida.',
                        'por_que_resolver': 'Fornecer consistência ajuda na retenção da informação e na familiaridade com o sistema.',
                        'exemplo_texto': 'Manter o botão de ajuda no mesmo local em todas as páginas de um site.',
                        'exemplo_foto': None,
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
                    # Construa o caminho completo da imagem
                    exemplo_foto = solucao.get('exemplo_foto')
                    if exemplo_foto:
                        # Combine com o MEDIA_ROOT para ter o caminho completo da imagem
                        exemplo_foto_path = os.path.join(settings.MEDIA_ROOT, exemplo_foto)
                    else:
                        exemplo_foto_path = None

                    Solucoes.objects.get_or_create(
                        problema=problema_obj,
                        descricao=solucao['descricao'],
                        por_que_resolver=solucao['por_que_resolver'],
                        exemplo_texto=solucao['exemplo_texto'],
                        exemplo_foto=exemplo_foto_path  # Salve o caminho completo
                    )
