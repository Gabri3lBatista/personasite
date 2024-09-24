# Usar uma imagem base Python
FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instalar pacotes do sistema necessários para WeasyPrint e suas dependências
RUN apt-get update && apt-get install -y \
    libpango1.0-0 \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libgobject-2.0-0 \
    libpangoft2-1.0-0 \
    libpangocairo-1.0-0 \
    && apt-get clean

# Atualizar o pip e instalar as dependências Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o código do projeto
COPY . .

# Expor a porta que o contêiner vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
