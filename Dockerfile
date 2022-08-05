# imagem base que será utilizada
FROM python:3.8.0

# criando um diretório
RUN mkdir /Retech
# definindo váriaveis de ambiente
# python não gera arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# as mensagens de log não ficaram armazenadas em buffers
ENV PYTHONUNBUFFERED 1

# definindo o diretório
WORKDIR /Retech

# copia o requirements para o diretório /Retech
COPY requirements.txt .
# intalar as dependencias do projeto
RUN pip install -r requirements.txt

# copia tudo que está na pasta local e envia para o diretório /Retech
COPY . .

# Expondo porta do django
EXPOSE 8000