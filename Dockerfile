FROM python:3.12

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgobject-2.0-0 \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o requirements.txt e instalar as dependências Python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar todo o código do projeto para o diretório de trabalho
COPY . .

# Comando para iniciar a aplicação
CMD ["gunicorn", "personasite.wsgi:application", "--bind", "0.0.0.0:8000"]
