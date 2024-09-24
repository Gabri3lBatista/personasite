# Usar uma imagem base Python
FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo de dependências para o contêiner
COPY requirements.txt .

# Atualizar o pip e instalar as dependências
RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install -r requirements.txt

# Copiar o código do projeto
COPY . .

# Expor a porta que o contêiner vai rodar
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
