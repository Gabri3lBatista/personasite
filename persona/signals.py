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
        'Dificuldade em seguir instruções': [
            '1.3.3 - Características sensoriais [A] - Qualquer tipo de instrução ou direcionamento não deve depender de um formato específico, localização espacial, som ou qualquer outra característica sensorial.',
            '1.3.4 - Orientação [AA] - Nenhuma funcionalidade deve depender de uma determinada orientação de tela (exemplo: virar o celular na horizontal), a não ser que seja imprescindível para execução da função.',
        ],
        'Dificuldades de memória': [
            '3.2.6 - Ajuda consistente [A] - Se algumas opções de ajuda forem fornecidas em uma tela (exemplo: Dados de contato humano ou um sistema automatizado), este mesmo formato deverá ser igual em todas as outras telas que a ajuda for fornecida.',
            '4.1.3 - Mensagens de status [AA] - Qualquer tipo de mensagem que é resultado de uma ação ou que informa o andamento de um processo e que seja relevante para a pessoa, deve ser transmitida sem que ocorra uma mudança de contexto (foco) na tela.',
        ],
        'Dificuldades em adaptar-se a mudanças': [
            '3.2.1 - Em foco [A] - Nenhuma mudança contextual que possa desorientar alguém, deve ocorrer a partir do foco em qualquer elemento na interface (exemplo: abertura de uma janela modal), sem que ocorra uma confirmação direta (exemplo: um botão de confirmação).',
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo pré-gravado que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
            '2.4.5 - Várias formas [AA] - As pessoas sempre deverão ter mais do que uma opção para encontrar um determinado conteúdo. Exemplo: um mesmo conteúdo pode ser acessado por um menu de navegação ou também através de um campo de busca.',
        ],
        'Sensibilidade a estímulos sensoriais': [
            '1.3.3 - Características sensoriais [A] - Qualquer tipo de instrução ou direcionamento não deve depender de um formato específico, localização espacial, som ou qualquer outra característica sensorial.',
            '1.2.5 - Audiodescrição (pré-gravado) [AA] - Deve ser fornecida uma audiodescrição ou uma transcrição descritiva em texto para todo conteúdo em vídeo pré-gravado.',
            '1.4.3 - Contraste (mínimo) [AA] - Textos devem ter uma relação de contraste entre primeiro e segundo plano de ao menos 4.5:1. (ver critério completo). Nota: caso o tamanho das fontes de textos sejam no mínimo "18pt" ou "14pt bold" a relação de contraste pode ser de 3:1.',
            '1.4.5 - Imagens de texto [AA] - Qualquer trecho na tela que pode ser exibido em formato de texto estilizado (exemplo: uma citação de uma frase de um autor específico ou um título de seção), não deve ser apresentado em formato de imagem, a não ser que possam ser customizados pela pessoa.',
            '1.4.11 - Contraste Não-Textual [AA] - Componentes de interface (exemplo: botões) e imagens essenciais para o entendimento do conteúdo devem ter uma relação de contraste entre primeiro e segundo plano de ao menos 3:1.',
        ],
        'Dificuldades em processamento auditivo': [
            '2.1.1 - Teclado [A] - Todas as funcionalidades devem ser acionadas via teclado, a menos que a funcionalidade não possibilite o controle apenas por teclado. Dica: o critério também atende a teclados bluetooth configurados em aparelhos móveis (ver critério 2.5.6).',
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo pré-gravado que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
            '1.2.5 - Audiodescrição (pré-gravado) [AA] - Deve ser fornecida uma audiodescrição ou uma transcrição descritiva em texto para todo conteúdo em vídeo pré-gravado.',
            '1.4.11 - Contraste Não-Textual [AA] - Componentes de interface (exemplo: botões) e imagens essenciais para o entendimento do conteúdo devem ter uma relação de contraste entre primeiro e segundo plano de ao menos 3:1.',
            '1.4.13 - Conteúdo em foco por mouse ou teclado [AA] - Conteúdos adicionais (exemplo: tooltip ou sub-menu) não devem ser acionados apenas com foco por mouse (mouse over) ou teclado. Caso isso ocorra, certas condições devem ser atendidas (ver critério completo).',
        ],
        'Desafios na organização de tarefas': [
            '1.3.1 - Informações e Relações [A] - A organização estrutural de uma tela deve ser construída de forma que sua arquitetura de informação faça sentido tanto para quem vê, quanto para quem ouve o conteúdo. Dica: o desafio aqui é proporcionar experiências equivalentes relacionadas aos contextos visuais e auditivos.',
            '1.3.5 - Identificar o objetivo de entrada [AA] - As pessoas devem ter clareza do que devem preencher em campos de formulários. Dica: em um campo que solicita o preenchimento do e-mail, deve ser claro qual e-mail deve ser preenchido (pessoal? comercial? etc).',
            '2.4.6 - Cabeçalhos e rótulos [AA] - Todos os títulos (diferentes níveis) e rótulos (campos de formulários) devem descrever claramente a finalidade dos conteúdos ou agrupamentos nos elementos da tela, sem que haja ambiguidade em seu entendimento.',
            '2.4.7 - Foco visível [AA] - Ao se interagir por teclado, qualquer pessoa deve conseguir identificar qual é a sua localização espacial na tela através de um foco (visível) identificador de sua localização.',
            '2.4.13 - Foco não obscurecido (mínimo) [AA] - Quando o foco visível for exibido, ele deverá possuir 2 pixels de largura, será preciso ter um espaçamento mínimo entre o conteúdo e o relacionamento de contraste com áreas adjacentes precisa ser suficiente (ver critério completo).',
        ],
        'Dificuldade em prestar atenção': [
            '3.2.1 - Em foco [A] - Nenhuma mudança contextual que possa desorientar alguém, deve ocorrer a partir do foco em qualquer elemento na interface (exemplo: abertura de uma janela modal), sem que ocorra uma confirmação direta (exemplo: um botão de confirmação).',
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo ao vivo que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
            '2.4.7 - Foco visível [AA] - Ao se interagir por teclado, qualquer pessoa deve conseguir identificar qual é a sua localização espacial na tela através de um foco (visível) identificador de sua localização.',
            '2.4.11 - Foco não obscurecido (mínimo) [AA] - Quando o foco visível for exibido em algum elemento na interface, ele não poderá ficar completamente oculto devido aos demais componentes da interface (exemplo: um rodapé fixo cobrir parcialmente este elemento).',
        ],
        'Comportamento repetitivo': [
            '2.4.1 - Ignorar blocos [A] - Deve ser fornecido um tipo de controle para que as pessoas possam ignorar determinados conteúdos repetitivos (exemplo: um menu de navegação). Dica: trata-se de um critério exclusivo para pessoas que usam teclado.',
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo ao vivo que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
            '2.4.5 - Várias formas [AA] - As pessoas sempre deverão ter mais do que uma opção para encontrar um determinado conteúdo. Exemplo: um mesmo conteúdo pode ser acessado por um menu de navegação ou também através de um campo de busca.',
        ],
        'Problemas com sequenciamento': [
            '1.3.2 - Sequência com significado [A]Seja qual for o método de interação, a apresentação das informações na tela sempre deverá ter uma sequência lógica. Dica: conteúdos responsivos não devem impactar o entendimento da informação independentemente do tamanho da tela.',
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo ao vivo que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
            '1.3.5 - Identificar o objetivo de entrada [AA] - As pessoas devem ter clareza do que devem preencher em campos de formulários. Dica: em um campo que solicita o preenchimento do e-mail, deve ser claro qual e-mail deve ser preenchido (pessoal? comercial? etc).',
            '2.4.6 - Cabeçalhos e rótulos [AA] - Todos os títulos (diferentes níveis) e rótulos (campos de formulários) devem descrever claramente a finalidade dos conteúdos ou agrupamentos nos elementos da tela, sem que haja ambiguidade em seu entendimento.',
            '2.4.7 - Foco visível [AA] - Ao se interagir por teclado, qualquer pessoa deve conseguir identificar qual é a sua localização espacial na tela através de um foco (visível) identificador de sua localização.',
            '2.4.11 - Foco não obscurecido (mínimo) [AA] - Quando o foco visível for exibido em algum elemento na interface, ele não poderá ficar completamente oculto devido aos demais componentes da interface (exemplo: um rodapé fixo cobrir parcialmente este elemento).',
        ],
        'Ansiedade': [
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo ao vivo que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
            '1.4.3 - Contraste (mínimo) [AA] - Textos devem ter uma relação de contraste entre primeiro e segundo plano de ao menos 4.5:1 (ver critério completo).',
            '3.2.6 - Ajuda consistente [A] - Se algumas opções de ajuda forem fornecidas em uma tela (exemplo: Dados de contato humano ou um sistema automatizado), este mesmo formato deverá ser igual em todas as outras telas que a ajuda for fornecida.',
        ],
            },  
            'Autismo': {
        'Dificuldade em seguir instruções': [
            '1.3.3 - Características sensoriais - [A] Evitar instruções dependentes de formato específico, localização espacial, som ou outras características sensoriais. Exemplo: Evitar expressões como "clique no botão abaixo" ou "clique no botão verde" ou "ao ouvir um bip, selecione uma opção."',
            '1.3.4 - Orientação [AA] - Nenhuma funcionalidade deve depender de uma determinada orientação de tela, a menos que seja imprescindível para execução da função.',
        ],
        'Dificuldades em adaptar-se a mudanças': [
            '3.2.1 - Em foco [A] - Nenhuma mudança contextual que possa desorientar deve ocorrer a partir do foco em qualquer elemento na interface, sem confirmação direta.',
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo pré-gravado que contenha uma faixa de áudio deve possuir legenda.',
            '2.4.5 - Várias formas [AA] - As pessoas sempre deverão ter mais do que uma opção para encontrar um determinado conteúdo. Exemplo: Um mesmo conteúdo pode ser acessado por um menu de navegação ou também através de um campo de busca.',
        ],
        'Sensibilidade a estímulos sensoriais': [
            '1.3.3 - Características sensoriais [A] - Evitar instruções dependentes de formato específico, localização espacial, som ou outras características sensoriais.',
            '1.4.3 - Contraste (mínimo) [AA] - Textos devem ter uma relação de contraste entre primeiro e segundo plano de ao menos 4.5:1. Nota: Caso o tamanho das fontes de textos seja no mínimo "18pt" ou "14pt bold", a relação de contraste pode ser de 3:1.',
            '1.4.5 - Imagens de texto [AA] - Qualquer trecho na tela que pode ser exibido em formato de texto estilizado não deve ser apresentado em formato de imagem, a menos que possam ser customizados pela pessoa.',
            '1.4.11 - Contraste Não-Textual [AA] - Componentes de interface e imagens essenciais para o entendimento do conteúdo devem ter uma relação de contraste entre primeiro e segundo plano de ao menos 3:1.',
        ],
        'Dificuldades em processamento auditivo': [
            '2.1.1 - Teclado [A] - Todas as funcionalidades devem ser acionadas via teclado, a menos que a funcionalidade não possibilite o controle apenas por teclado.',
            '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo pré-gravado que contenha uma faixa de áudio deve possuir legenda.',
            '1.2.5 - Audiodescrição (pré-gravado) [AA] - Deve ser fornecida uma audiodescrição ou uma transcrição descritiva em texto para todo conteúdo em vídeo pré-gravado.',
            '1.4.11 - Contraste Não-Textual [AA] - Componentes de interface e imagens essenciais para o entendimento do conteúdo devem ter uma relação de contraste entre primeiro e segundo plano de ao menos 3:1.',
            '1.4.13 - Conteúdo em foco por mouse ou teclado [AA] - Conteúdos adicionais não devem ser acionados apenas com foco por mouse ou teclado, a menos que certas condições sejam atendidas.',
        ],
        'Desafios na organização de tarefas': [
            '1.3.1 - Informações e Relações [A] - A organização estrutural de uma tela deve ser construída de forma que sua arquitetura de informação faça sentido tanto para quem vê quanto para quem ouve o conteúdo. Dica: O desafio aqui é proporcionar experiências equivalentes relacionadas aos contextos visuais e auditivos.',
            '1.3.5 - Identificar o objetivo de entrada [AA] - As pessoas devem ter clareza do que devem preencher em campos de formulários. Dica: Em um campo que solicita o preenchimento do e-mail, deve ser claro qual e-mail deve ser preenchido (pessoal? comercial? etc).',
            '2.4.6 - Cabeçalhos e rótulos [AA] - Todos os títulos e rótulos devem descrever claramente a finalidade dos conteúdos ou agrupamentos nos elementos da tela, sem ambiguidade.',
            '2.4.7 - Foco visível [AA] - Ao se interagir por teclado, qualquer pessoa deve conseguir identificar qual é a sua localização espacial na tela através de um foco visível identificador de sua localização.',
            '2.4.13 - Foco não obscurecido (mínimo) [AA] - Quando o foco visível for exibido, ele deverá possuir 2 pixels de largura, e será preciso ter um espaçamento mínimo entre o conteúdo e o relacionamento de contraste com áreas adjacentes.',
        ],
},
                    'TDAH': {
        'Dificuldade em seguir instruções': [
        '1.3.3 - Características sensoriais [A] - Qualquer tipo de instrução ou direcionamento não deve depender de um formato específico, localização espacial, som ou qualquer outra característica sensorial.',
        '1.3.4 - Orientação [AA] - Nenhuma funcionalidade deve depender de uma determinada orientação de tela (exemplo: virar o celular na horizontal), a não ser que seja imprescindível para execução da função.',
        ],
        'Dificuldades de memória': [
        '3.2.6 - Ajuda consistente [A] - Se algumas opções de ajuda forem fornecidas em uma tela (exemplo: Dados de contato humano ou um sistema automatizado), este mesmo formato deverá ser igual em todas as outras telas que a ajuda for fornecida.',
        '4.1.3 - Mensagens de status [AA] - Qualquer tipo de mensagem que é resultado de uma ação ou que informa o andamento de um processo e que seja relevante para a pessoa, deve ser transmitida sem que ocorra uma mudança de contexto (foco) na tela.',
        ],
        'Dificuldades em adaptar-se a mudanças': [
        '3.2.1 - Em foco [A] - Nenhuma mudança contextual que possa desorientar alguém, deve ocorrer a partir do foco em qualquer elemento na interface (exemplo: abertura de uma janela modal), sem que ocorra uma confirmação direta (exemplo: um botão de confirmação).',
        '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo pré-gravado que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
        '2.4.5 - Várias formas [AA] - As pessoas sempre deverão ter mais do que uma opção para encontrar um determinado conteúdo. Exemplo: um mesmo conteúdo pode ser acessado por um menu de navegação ou também através de um campo de busca.',
        ],
        'Problemas de atenção': [
        '3.2.1 - Em foco [A] - Nenhuma mudança contextual que possa desorientar alguém, deve ocorrer a partir do foco em qualquer elemento na interface (exemplo: abertura de uma janela modal), sem que ocorra uma confirmação direta (exemplo: um botão de confirmação).',
        '1.2.4 - Legendas (ao vivo) [AA] - Qualquer conteúdo ao vivo que contenha uma faixa de áudio (seja apenas áudio ou vídeo) deve possuir legenda.',
        '2.4.7 - Foco visível [AA] - Ao se interagir por teclado, qualquer pessoa deve conseguir identificar qual é a sua localização espacial na tela através de um foco (visível) identificador de sua localização.',
        '2.4.11 - Foco não obscurecido (mínimo) [AA] - Quando o foco visível for exibido em algum elemento na interface, ele não poderá ficar completamente oculto devido aos demais componentes da interface (exemplo: um rodapé fixo cobrir parcialmente este elemento).',
        ],
        'Comportamento hiperativo': [
        '2.2.1 - Ajustável por limite de tempo [A] - Caso seja definida uma funcionalidade que exija tempo para execução e essa não seja essencial (obrigatória do ponto de vista legal), deve-se incluir também uma opção para desligá-lo ou uma opção para ampliá-lo.',
        '2.4.7 - Foco visível [AA] - Ao se interagir por teclado, qualquer pessoa deve conseguir identificar qual é a sua localização espacial na tela através de um foco (visível) identificador de sua localização.',
        ],
                    }
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
