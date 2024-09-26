# Escolher imagem Python
FROM python:3.12

# Definir diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto
COPY . .

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    libcairo2 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libffi-dev \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Executar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "personasite.wsgi:application"]
