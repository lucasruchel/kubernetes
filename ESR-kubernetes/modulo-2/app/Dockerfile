
FROM python:3.11-slim-bookworm AS builder

WORKDIR /app


RUN useradd --create-home --shell /bin/bash appuser && chown appuser:appuser /app

RUN apt-get update && apt-get install -y curl && \
      apt-get autoremove -y && rm -rf /var/lib/apt/lists/*

USER appuser

RUN  curl -LsSf https://astral.sh/uv/install.sh | sh

# Copia os arquivos da aplicação (app.py e a pasta templates)
COPY --chown=appuser:appuser . .

RUN /home/appuser/.local/bin/uv sync --no-dev && \
   . /app/.venv/bin/activate 

# Expõe a porta que o Gunicorn irá usar
EXPOSE 5000

# Define a variável de ambiente PATH para incluir o ambiente virtual
ENV PATH="/app/.venv/bin:$PATH"

# Comando para iniciar a aplicação com Gunicorn
# Este comando será executado quando o contêiner iniciar
CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]
