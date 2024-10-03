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
                        'nome': 'Fontes Sans-Serifadas',
                        'descricao': '''
                * Utilize fontes sans-serifadas para melhorar a legibilidade.
                * Exemplos incluem: Tiresias, Verdana e Arial.
                * As fontes sem serifas ajudam pessoas com dislexia a lerem melhor.''',
                        'por_que_resolver': 'Para pessoas com TDAH e dislexia, geralmente, fontes do tipo sans-serif são mais fáceis de distinguir seus caracteres individualmente além de possuírem um espaçamento mínimo adequado entre cada caractere monospacing, sendo assim, diminui a possibilidade do usuário confundir a identificação de caracteres, sem atrasar sua leitura.',
                        'exemplo_texto': 'Utilize fontes como Tiresias, Verdana ou  pois se pode distinguir entre as letras “I” maiúscula e “l” minuscula.',
                        'exemplo_foto': 'exemplos/exemplo1.jpg',  # Caminho relativo à pasta de mídia
                    },
                    {
                        'nome': 'Tamanho da Fonte',
                        'descricao': 'Para extensos parágrafos, tamanho de 12 pontos na fonte do corpo textual. Para subtítulos ou legendas, no mínimo, o tamanho de 9 pontos - tamanhos menores podem ser ilegíveis em algumas plataformas. Para títulos (cabeçalhos), use um tamanho de fonte que seja pelo menos 20% maior do que o texto normal.',
                        'por_que_resolver': 'Fontes no tamanho adequado conforme sua hierarquia da informação - isto é, ser capaz de discernir o que é um cabeçalho, subtítulo, parágrafo, legendas e afins - torna o texto fácil de ler em um relance, resultando uma a leitura mais rápida e fácil para todos devido ao baixo esforço cognitivo no ato de assimilar os caracteres quanto para manter o foco.',
                        'exemplo_texto': 'Garantir que um site ou aplicativo funcione tanto em modo retrato quanto em modo paisagem, a menos que uma orientação específica seja essencial.',
                        'exemplo_foto': 'exemplos/exemplo2.png',
                    },
                ],
                'Problemas com texto': [
                    {
                        'nome': 'Texto em Colunas',
                        'descricao': 'Considere distribuir seu texto em colunas menores a fim de facilitar a leitura. Costuma-se trabalhar com o padrão de 12 colunas em um ambiente desktop. Com isso, é ideal dispor o texto em colunas com 45 até 70 caracteres por linha. Forneça um espaçamento adequado entre cada coluna.',
                        'por_que_resolver': 'Quanto mais texto é apresentado ao usuário de um lado a outro da tela, mais difícil se torna a leitura devido ao esforço cognitivo necessário para acompanhar.',
                        'exemplo_texto': 'A largura e quantidade das colunas é indeterminado, depende do projeto e do que o designer definir ser o melhor, costuma-se trabalhar com o padrão de 12 colunas em um ambiente desktop.',
                        'exemplo_foto': 'exemplos/exemplo3.png',
                    },
                    {
                        'nome': 'Distribuição Textual',
                        'descricao': 'As informações precisam ser claras, objetivas e minimalistas e previamente sinalizadas ao usuário a fim de manter sua atenção durante a leitura.',
                        'por_que_resolver': 'Longos blocos de parágrafos ininterruptos são difíceis de ler para usuários visto que é fácil, principalmente, para leitores com dislexia e TDAH se perderem em sua leitura.',
                        'exemplo_texto': 'Parágrafos podem ser divididos em seções com títulos e subtítulos para organizar o conteúdo de forma lógica. É recomendável apresentar um resumo prévio em bullets, para que o leitor saiba o que esperar e possa ler com mais atenção. Agrupe assuntos relacionados e use espaçamento adequado entre blocos textuais, evitando que tópicos diferentes pareçam tratar do mesmo assunto.',
                        'exemplo_foto': 'exemplos/exemplo4.png',
                    },
                     {
                        'nome': 'Destaque de informações textuais',
                        'descricao': 'Em um texto, é comum querer enfatizar algumas informações além do texto: como diferenciar os cabeçalhos e subtítulos, os hyperlinks dentro de um parágrafos. Pode-se utilizar recursos visuais como itálico, caixa alta, negrito e afins, contudo, algumas práticas podem atrapalhar a leitura causando o efeito contrário de destacar a informação e manter o foco do usuário.',
                        'por_que_resolver': 'Organização e consistência são importantes para que informações sejam mais fáceis de encontrar, e os usuários possam ser capazes de identificar os principais recursos de uma interface rapidamente.',
                        'exemplo_texto': 'Evite o uso excessivo de letras maiúsculas ou minúsculas. Use maiúsculas conforme a norma culta e negrito para ênfase com moderação. Evite itálico, pois prejudica a legibilidade, exceto em casos como palavras estrangeiras. Não sublinhe para ênfase, pois essa formatação está associada a links. O tachado também interfere na leitura e deve ser evitado. Mantenha a padronização em links, legendas, títulos e outros componentes para facilitar a leitura e a identificação de padrões.',
                        'exemplo_foto': 'exemplos/exemplo5.png',
                    },
                     
                ],
                'Constraste': [
                  { 
                        'nome': 'Contraste de Cores',
                        'descricao': 'Considere distribuir seu texto em colunas menores a fim de facilitar a leitura. Costuma-se trabalhar com o padrão de 12 colunas em um ambiente desktop. Com isso, é ideal dispor o texto em colunas com 45 até 70 caracteres por linha. Forneça um espaçamento adequado entre cada coluna.',
                        'por_que_resolver': 'Quanto mais texto é apresentado ao usuário de um lado a outro da tela, mais difícil se torna a leitura devido ao esforço cognitivo necessário para acompanhar.',
                        'exemplo_texto': 'A largura e quantidade das colunas é indeterminado, depende do projeto e do que o designer definir ser o melhor, costuma-se trabalhar com o padrão de 12 colunas em um ambiente desktop.',
                        'exemplo_foto': 'exemplos/exemplo6.png',
                    }, 
                ],
                'Problemas com Interpretação': [
                  {
                        'nome': 'Formulários Acessíveis',
                        'descricao': 'Criar um formulário acessível e organizado, com campos claros, opções automáticas e sugestões, minimizando a necessidade de inserção manual e reduzindo o esforço cognitivo.',
                        'por_que_resolver': 'O preenchimento de formulários pode ser desafiador para pessoas neurodivergentes. Usuários com TDAH podem se perder no objetivo dos campos; aqueles com disortografia podem cometer erros ortográficos; e pessoas com discalculia podem se confundir com números. Além disso, a "ansiedade pela informação" surge quando há excesso ou falta de clareza nas informações. Assim, é essencial que formulários sejam bem estruturados e instruídos, facilitando o preenchimento para todos os perfis, sem gerar frustrações.',
                        'exemplo_texto': 'Ao criar um formulário acessível, é importante indicar claramente quais campos são obrigatórios e opcionais, utilizando termos por extenso e evitando símbolos como o asterisco, para reduzir o esforço cognitivo do usuário. Utilize rótulos fixos (label) próximos aos campos de inserção para que o usuário tenha sempre à vista o que precisa ser preenchido. Sempre que possível, evite campos de texto manual, optando por componentes como listas de seleção ou calendários. Ofereça a opção de visualizar campos ocultos, como senhas, permitindo que o usuário verifique a escrita. A funcionalidade de auto-preenchimento de campos textuais deve ser disponibilizada para minimizar erros. Prefira representações verbais em vez de numéricas, como "Janeiro" ao invés de "01" em seleções de mês. Utilize o atributo placeholder para fornecer exemplos de preenchimento, facilitando a compreensão do que é esperado em campos de texto manual.',
                        'exemplo_foto': 'exemplos/exemplo7.png',
                    }, 
                  {
                        'nome': 'Suporte de Interpretação Textual ',
                        'descricao': 'Utilizar recursos multimídia, como imagens, fluxogramas, vídeos e áudios, que complementem o conteúdo textual. Esses recursos adicionais melhoram o processo de assimilação e acomodação, pois oferecem múltiplas formas de interpretar a mesma informação. Ao usar diferentes mídias, é possível facilitar a compreensão e a retenção de conteúdo sem sobrecarregar a capacidade cognitiva.',
                        'por_que_resolver': 'Suporte de Interpretação Textual - Uma determinada quantidade de informações pode ser ouvida, compreendida e processada por um aluno em um determinado momento. No entanto, se um segundo canal, por exemplo visual, simultaneamente transmite informações adicionais, a capacidade de processamento pode ser expandida em algum grau.',
                        'exemplo_texto': 'Utilize recursos multimídia como imagens, fluxogramas, vídeos ou áudios, e posicione-os próximos ao conteúdo textual para que o usuário possa acessar ambos simultaneamente. Isso facilita o processo de assimilação e acomodação da informação. Insira ícones e símbolos visuais para ilustrar conceitos e melhorar a clareza da comunicação. Ao aplicar esses recursos, evite sobrecarregar o usuário com informações em excesso, garantindo que ele consiga processar o conteúdo sem dificuldades. Se houver um limite de tempo, forneça um temporizador visível para que o usuário possa gerenciar seu tempo de forma eficaz e personalizada.',
                        'exemplo_foto': 'exemplos/exemplo9.png',
                    }, 
                  {
                        'nome': 'Multimídia',
                        'descricao': 'Oferecer o conteúdo em múltiplos formatos, além do texto, como imagens, vídeos e áudios. Isso proporciona uma experiência de aprendizado mais inclusiva, permitindo que os usuários escolham o formato que melhor se adapta ao seu estilo de aprendizagem.',
                        'por_que_resolver': 'Multimídia - Um processo de comunicação acontece de várias formas, não apenas textual: não se pode pressupor que apenas a disponibilização da mídia em formato de texto seja o suficiente para que o usuário capte uma informação.',
                        'exemplo_texto': 'Ao criar um formulário acessível, é importante indicar claramente quais campos são obrigatórios e opcionais, utilizando termos por extenso e evitando símbolos como o asterisco, para reduzir o esforço cognitivo do usuário. Utilize rótulos fixos (label) próximos aos campos de inserção para que o usuário tenha sempre à vista o que precisa ser preenchido. Sempre que possível, evite campos de texto manual, optando por componentes como listas de seleção ou calendários. Ofereça a opção de visualizar campos ocultos, como senhas, permitindo que o usuário verifique a escrita. A funcionalidade de auto-preenchimento de campos textuais deve ser disponibilizada para minimizar erros. Prefira representações verbais em vez de numéricas, como "Janeiro" ao invés de "01" em seleções de mês. Utilize o atributo placeholder para fornecer exemplos de preenchimento, facilitando a compreensão do que é esperado em campos de texto manual.',
                        'exemplo_foto': 'exemplos/exemplo7.png',
                    }, 
                  
                ],
                
                
                'Representação numérica': [
                   {
                        'descricao': 'Indivíduos com discalculia não possuem dificuldades apenas em habilidades matemáticas presentes na resolução de operações: o raciocínio lógico-matemático também está presente processamento de informações numéricas, fatores aritméticos e o domínio em quantificações.',
                        'por_que_resolver': 'O preenchimento de formulários pode ser desafiador para pessoas neurodivergentes. Usuários com TDAH podem se perder no objetivo dos campos; aqueles com disortografia podem cometer erros ortográficos; e pessoas com discalculia podem se confundir com números. Além disso, a "ansiedade pela informação" surge quando há excesso ou falta de clareza nas informações. Assim, é essencial que formulários sejam bem estruturados e instruídos, facilitando o preenchimento para todos os perfis, sem gerar frustrações.',
                        'exemplo_texto': 'Exiba informações matemáticas e temporais de forma clara e explícita, como "A duração estimada do voo é de 4 horas" em vez de exigir que o usuário calcule. Ao apresentar horários, permita a escolha entre os sistemas de 12 horas (AM/PM) e 24 horas, dando a opção para o usuário selecionar o formato mais confortável. Sempre que possível, converta automaticamente fusos horários e informe essa conversão de maneira clara. Ao exibir quantidades ou informações numéricas, utilize reforços visuais e textuais, como gráficos ou barras de progresso, para facilitar a interpretação. Evite mostrar números isolados; sempre acompanhe-os com descrições que ajudem na compreensão, como "2 pessoas estão online" ao invés de apenas "2".',
                        'exemplo_foto': 'exemplos/exemplo8.png',
                    }, 
                ],
                
                
                # Adicione mais problemas e soluções conforme necessário...
            },
            'Autismo': {
                'Problemas visuais e textuais': [
                    {
                        'nome': 'Cores',
                        'por_que_resolver': 'Elementos que usam apenas cores, sem imagens ou textos, podem atrair a atenção, especialmente de crianças, sem que elas compreendam o significado desses elementos. O baixo contraste entre o fundo e o texto ou objeto de primeiro plano dificulta a compreensão, a legibilidade e pode prejudicar a atenção de pessoas com TEA. No entanto, as cores e contrastes podem ser usados positivamente para guiar a atenção e diferenciar elementos.',
                        'descricao': 'Cores devem ser usadas como complemento, e não como a única forma de transmitir informações. O contraste entre o fundo e o objeto de primeiro plano deve ser suficiente para garantir a legibilidade. É importante que o conteúdo seja compreensível sem depender apenas das cores, imagens ou estilos, garantindo acessibilidade.',
                        'exemplo_texto': 'Escolha cores de fundo que contrastem adequadamente com os objetos ou textos de primeiro plano, preferindo fundos claros ou brancos. * Use cores para diferenciar seções ou relacionar conteúdos similares, mas sempre com um complemento textual ou visual. * Certifique-se de que o conteúdo possa ser compreendido sem depender exclusivamente das cores. * Associe rótulos textuais a elementos visuais e utilize ferramentas de verificação de contraste para garantir que o contraste entre o plano de fundo e os objetos esteja adequado.',
                        'exemplo_foto': 'exemplos/exemplo10.png',
                    }, 
                    {
                        'nome': 'Texto',
                        'por_que_resolver': 'Parágrafos complexos podem também ser distrativos e prejudicar a atenção ao conteúdo da página. Para crianças, o uso de linguagem simples e textos sucintos pode auxiliar não apenas na atenção e compreensão da linguagem, mas também na aquisição de vocabulário e letramento.',
                        'descricao': 'A solução para melhorar a compreensão de textos por parte de pessoas com TEA é adotar uma linguagem visual e textual simples e objetiva. Isso inclui evitar o uso de jargões, termos técnicos, abreviações, acrônimos e expressões conotativas que possam confundir ou desviar a atenção. ',
                        'exemplo_texto': 'Use linguagem simples e evite jargões, termos técnicos ou conotativos. * Mantenha parágrafos curtos e objetivos para facilitar a leitura e compreensão. * Evite o uso de metáforas ou expressões figurativas, adotando uma abordagem literal. * Utilize rótulos consistentes para botões, formulários e elementos interativos. * Evite o uso de abreviações e acrônimos que possam não ser familiares. * Adote símbolos e ícones reconhecíveis, que auxiliem na navegação. * Revise o conteúdo para garantir a ausência de erros ortográficos e gramaticais.',
                        'exemplo_foto': 'exemplos/exemplo11.png',
                    }, 
                    {
                        'nome': 'Legibilidade',
                        'por_que_resolver': 'Parágrafos longos e complexos podem distrair e dificultar a compreensão, especialmente para pessoas com TEA. Dividir o texto em partes menores, com listas e subtítulos, melhora a atenção e organização do conteúdo.',
                        'descricao': 'Utilizar elementos como subtítulos, listas, espaçamento adequado e fontes de fácil leitura (sem serifa) para garantir que o texto seja acessível e claro.',
                        'exemplo_texto': 'Tamanho do texto: Limite de 80 caracteres por linha. - Alinhamento: Evite alinhar textos à direita. - Caixa de texto: Evite usar texto todo em caixa alta. - Fontes: Prefira fontes sem serifa, como Arial, Verdana, Helvetica ou Tahoma. - Estrutura: Utilize subtítulos e listas para dividir e organizar o conteúdo. - Linguagem: Simples, clara, sem erros e com poucos jargões ou abreviações.',
                        'exemplo_foto': 'exemplos/exemplo12.png',
                    },
                    {
                        'nome': 'Compatibilidade',
                        'por_que_resolver': 'É preciso que ações, ícones e elementos da página ou aplicação sejam relacionados com ações concretas e baseados no mundo real para que a pessoa possa reconhecê-los mais facilmente.',
                        'descricao': 'Ações, ícones e elementos de interface devem ser baseados no mundo real e representar situações concretas e reconhecíveis. Isso facilita a compreensão, especialmente para pessoas com TEA e crianças, que podem transferir esse conhecimento para a vida cotidiana. Esse enfoque melhora habilidades como memorização, atenção e compreensão visual e verbal.',
                        'exemplo_texto': 'Use ícones, imagens e nomenclaturas que representem ações reais e concretas, evitando metáforas. - Sempre que possível, utilize interações que imitem o mundo real, como ações comuns em dispositivos móveis (ex: deslizar, arrastar). - Utilize representações claras de situações e emoções do cotidiano, facilitando a compreensão. - Relacione as atividades da aplicação com experiências diárias e habilidades que a criança ou usuário já tenha vivenciado. - Para crianças, crie uma interface que ajude a associar vocabulários e ações que elas poderão usar no dia a dia.',
                        'exemplo_foto': 'exemplos/exemplo13.png',
                    }, 
                ],
                'Customização': [
                    {
                        'nome': 'Customização visual',
                        'por_que_resolver': 'Pessoas com Transtorno do Espectro Autista (TEA) podem ter preferências muito variadas em relação a cores, fontes e outros elementos visuais. Uma cor ou fonte que pode ser agradável para uma pessoa pode ser desconfortável ou perturbadora para outra. Não é possível prever um padrão geral de preferências visuais, pois cada pessoa apresenta diferentes sensibilidades e necessidades.',
                        'descricao': 'Ofereça funcionalidades que permitam ao usuário personalizar a interface para melhorar sua acessibilidade. Permita aumentar o tamanho do texto, facilitando a leitura e compreensão visual. Ofereça opções de customização de cores, incluindo esquemas de alto contraste, e permita que o usuário altere a fonte, escolhendo o estilo que mais lhe agrada. Caso o site ou aplicativo tenha sons ou narrações, inclua a opção de ativá-los ou desativá-los, com controle de volume. Além disso, permita que o usuário personalize o posicionamento da navegação ou outros elementos da interface para maior controle.',
                        'exemplo_texto': 'Ajuste de texto: Permita que o usuário aumente ou diminua o tamanho do texto, mesmo que o navegador ofereça essa função nativamente. - Customização de cores e fontes: Ofereça opções para o usuário alterar cores, fontes e o esquema de cores da página (incluindo um modo de alto contraste). - Controle de voz e som: Em botões com narrações ou som, permita alterar a voz utilizada e controlar o volume ou desativar sons. - Navegação customizável: Dê a opção de alterar o posicionamento da navegação e outros elementos interativos.',
                        'exemplo_foto': 'exemplos/exemplo14.png',
                    }, 
                   
                    {
                        'nome': 'Customização Informacional',
                        'por_que_resolver': 'Pessoas com Transtorno do Espectro Autista (TEA) podem ter preferências muito variadas em relação a cores, fontes e outros elementos visuais. Uma cor ou fonte que pode ser agradável para uma pessoa pode ser desconfortável ou perturbadora para outra. Não é possível prever um padrão geral de preferências visuais, pois cada pessoa apresenta diferentes sensibilidades e necessidades.',
                        'descricao': 'Ofereça funcionalidades que permitam ao usuário personalizar a interface para melhorar sua acessibilidade. Permita aumentar o tamanho do texto, facilitando a leitura e compreensão visual. Ofereça opções de customização de cores, incluindo esquemas de alto contraste, e permita que o usuário altere a fonte, escolhendo o estilo que mais lhe agrada. Caso o site ou aplicativo tenha sons ou narrações, inclua a opção de ativá-los ou desativá-los, com controle de volume. Além disso, permita que o usuário personalize o posicionamento da navegação ou outros elementos da interface para maior controle.',
                        'exemplo_texto': 'Permitia customizar os botões com símbolos e palavras ou apenas palavras. - O som, incluindo música, deve ser opcional ou pelo menos incluir um controle de volume. - Permita alterar cores, fontes e voz utilizada nos botões. - Permita customizar cores e sons utilizados no site ou aplicação.',
                        'exemplo_foto': 'exemplos/exemplo15.png',
                    },
                ],
                 'Engajamento': [
                    {
                        'nome': 'Eliminar distrações',
                        'por_que_resolver': 'Pessoas com TEA podem ter dificuldade para prestar atenção ao conteúdo primário apresentado na tela devido à distração de conteúdo secundário, como imagens de fundo, cenários com muitos detalhes, fundos texturizados ou elementos animados.',
                        'descricao': 'Para facilitar a atenção de usuários com TEA, a solução é minimizar distrações visuais e auditivas na interface. Elimine elementos que piscam, brilham ou fazem sons de fundo, ou ofereça opções para que o usuário possa desativar essas funcionalidades. Destaque o conteúdo essencial da tela para ajudar o usuário a manter o foco no que é mais importante.',
                        'exemplo_texto': 'Evite animações e fontes chamativas: Não utilize fontes "fantasia" ou animações que desviem a atenção. - Minimize elementos desnecessários: Reduza o conteúdo visual ao essencial para a tarefa principal. - Destaque o conteúdo principal: Utilize contraste e hierarquia visual para destacar as informações ou ações mais importantes. - Desative elementos piscantes ou brilhantes: Não use elementos piscantes, especialmente para interfaces infantis. - Ofereça controles: Forneça opções para que os usuários desativem ou ajustem animações e sons, permitindo controle sobre a interface.',
                        'exemplo_foto': 'exemplos/exemplo16.png',
                    }, 
                    {
                        'nome': 'Interface minimalista',
                        'por_que_resolver': 'Pessoas com TEA podem ficar frustradas ou confusas quando muitas informações são apresentadas de uma só vez em uma única tela. Isso pode dificultar a realização de tarefas, especialmente quando as instruções para uma ação são fornecidas em conjunto com outras atividades. Interfaces carregadas com muitos elementos podem causar estresse e sobrecarga cognitiva.',
                        'descricao': 'Projete interfaces simples e claras, contendo apenas as informações e funcionalidades necessárias para a tarefa atual. Evite adicionar elementos ou funcionalidades que não são essenciais para o processo, e divida atividades complexas em múltiplas etapas ou telas. Isso permitirá que o usuário se concentre em uma tarefa de cada vez, evitando distrações.',
                        'exemplo_texto': 'Apresente na tela apenas os elementos necessários para a tarefa atual, omitindo ou escondendo informações irrelevantes. - Avalie se todas as funcionalidades planejadas são realmente essenciais para a tarefa em questão, e remova aquelas que possam causar sobrecarga. - Projete interfaces limpas, com layout organizado e claro, que foque na tarefa principal a ser realizada. - Para atividades complexas, divida-as em várias etapas, cada uma em sua própria tela, permitindo que o usuário complete uma ação de cada vez.',
                        'exemplo_foto': 'exemplos/exemplo17.png',
                    }, 
                    
                 ],
                 'Navegabilidade': [ 
                    {
                        'nome': 'Navegação Simples',
                        'por_que_resolver': 'Pessoas com TEA podem ter dificuldades para se localizar em páginas com grande quantidade de informações e links. Navegações complexas podem causar frustração e confusão, dificultando a tarefa de encontrar a informação desejada. Por isso, é importante fornecer uma navegação simples, consistente e clara, ajudando o usuário a manter o controle e a previsibilidade dentro do ambiente digital.',
                        'descricao': 'Fornecer uma navegação que seja previsível, com indicadores de localização (como trilhas de navegação), progressos claros, e um design consistente. Botões de navegação global como "Sair", "Voltar para página inicial" e "Ajuda" devem estar presentes em todas as páginas.',
                        'exemplo_texto': 'Consistência na navegação: Mantenha o mesmo menu e as mesmas opções de navegação em todas as páginas, garantindo uma experiência contínua e previsível. - Indicadores de progresso: Utilize elementos como "breadcrumbs" (trilhas de navegação) para mostrar onde o usuário está no site. Exemplo: Página inicial > Seção > Subseção. - Botões essenciais: Inclua botões globais como "Sair", "Voltar para a página inicial", "Ajuda", e "Avançar" ou "Voltar" para facilitar a navegação. - Formas alternativas de navegação: Forneça menus hierárquicos ou opções de busca para que o usuário possa encontrar facilmente o que precisa.',
                        'exemplo_foto': 'exemplos/exemplo18.png',
                    }, 
                 ]
                
                
            },
            
            'TDAH': {
                  'Problemas ': [
                    {
                        'por_que_resolver': 'Elementos que usam apenas cores, sem imagens ou textos, podem atrair a atenção, especialmente de crianças, sem que elas compreendam o significado desses elementos. O baixo contraste entre o fundo e o texto ou objeto de primeiro plano dificulta a compreensão, a legibilidade e pode prejudicar a atenção de pessoas com TEA. No entanto, as cores e contrastes podem ser usados positivamente para guiar a atenção e diferenciar elementos.',
                        'descricao': 'Cores - Cores devem ser usadas como complemento, e não como a única forma de transmitir informações. O contraste entre o fundo e o objeto de primeiro plano deve ser suficiente para garantir a legibilidade. É importante que o conteúdo seja compreensível sem depender apenas das cores, imagens ou estilos, garantindo acessibilidade.',
                        'exemplo_texto': 'Escolha cores de fundo que contrastem adequadamente com os objetos ou textos de primeiro plano, preferindo fundos claros ou brancos. * Use cores para diferenciar seções ou relacionar conteúdos similares, mas sempre com um complemento textual ou visual. * Certifique-se de que o conteúdo possa ser compreendido sem depender exclusivamente das cores. * Associe rótulos textuais a elementos visuais e utilize ferramentas de verificação de contraste para garantir que o contraste entre o plano de fundo e os objetos esteja adequado.',
                        'exemplo_foto': 'exemplos/exemplo8.png',
                    }, 
                ],  
            },
        }

        for neurodivergencia, problemas in dados_neurodivergentes.items():
            neurodivergente_obj, _ = Neurodivergente.objects.get_or_create(nome=neurodivergencia)
            for problema_descricao, solucoes in problemas.items():
                problema_obj, _ = Problemas.objects.get_or_create(neurodivergente=neurodivergente_obj, descricao=problema_descricao)
                for solucao in solucoes:
                    # Verifica se a imagem existe e define o caminho correto
                    exemplo_foto = solucao.get('exemplo_foto')
                    if exemplo_foto:
                        exemplo_foto_path = os.path.join(settings.MEDIA_ROOT, exemplo_foto)
                    else:
                        exemplo_foto_path = None
                    
                    nome_solucao = solucao.get('nome', 'Solução')

                    # Pega os valores ou define valores padrão se estiverem ausentes
                    por_que_resolver = solucao.get('por_que_resolver', '')
                    exemplo_texto = solucao.get('exemplo_texto', '')

                    # Verifica se a solução já existe
                    solucao_obj, created = Solucoes.objects.get_or_create(
                        problema=problema_obj,
                        descricao=solucao['descricao'],
                        defaults={
                            'nome': nome_solucao, 
                            'por_que_resolver': por_que_resolver,
                            'exemplo_texto': exemplo_texto,
                            'exemplo_foto': exemplo_foto_path
                        }
                    )

                    # Atualiza os dados caso tenham sido modificados
                    if  solucao_obj.por_que_resolver != por_que_resolver or \
                        solucao_obj.exemplo_texto != exemplo_texto or \
                        solucao_obj.exemplo_foto != exemplo_foto_path:
                        solucao_obj.por_que_resolver = por_que_resolver
                        solucao_obj.exemplo_texto = exemplo_texto
                        solucao_obj.exemplo_foto = exemplo_foto_path
                        solucao_obj.save()
