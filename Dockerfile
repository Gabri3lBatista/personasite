FROM python:3.12-slim

# Atualizar repositórios e instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgobject-2.0-0 \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libffi-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o requirements.txt e instalar as dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código do projeto para o diretório de trabalho
COPY . .

# Comando para iniciar a aplicação
CMD ["gunicorn", "personasite.wsgi:application", "--bind", "0.0.0.0:8000"]
