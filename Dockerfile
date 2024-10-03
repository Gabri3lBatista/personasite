# Usar uma imagem oficial do Python
FROM python:3.9-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar as dependências do Python
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar o código do projeto para o diretório de trabalho
COPY . .

# Comando para iniciar a aplicação
CMD ["gunicorn", "personasite.wsgi:application", "--bind", "0.0.0.0:8000"]
