import os
from django.core.management import execute_from_command_line
from django.apps import apps

# Mude para o diretório do projeto Django
os.chdir('c:/Users/gabri/Documents/tcc_projeto/personasite')

# Configuração para as variáveis de ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personasite.settings')

if __name__ == "__main__":
    # Carregue os modelos antes de executar comandos
    apps.populate(apps.all_models)

    # Execute comandos diretamente
    execute_from_command_line(['manage.py', 'makemigrations', 'persona'])
    execute_from_command_line(['manage.py', 'migrate'])
