# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Instalar as dependências do sistema necessárias para WeasyPrint
RUN apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libgobject-2.0-dev \  # Corrigido o nome do pacote
    libcairo2 \
    libffi-dev \
    shared-mime-info

# Copiar o arquivo de dependências do projeto (requirements.txt)
COPY requirements.txt .

# Instalar as dependências Python
RUN pip install -r requirements.txt

# Copiar todo o código do projeto para o diretório de trabalho
COPY . .

# Expor a porta que o Django vai rodar
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
