FROM python:3.11-slim

WORKDIR /app

# Instala dependencias de sistema (solo las necesarias)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY app/ ./app/

# Expone el puerto que usará uvicorn (por defecto 8000)
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
