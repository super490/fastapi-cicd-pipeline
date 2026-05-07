from fastapi import FastAPI

app = FastAPI(
    title="CI/CD Demo API",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    """Endpoint de salud para monitoreo."""
    return {"status": "ok", "message": "Service is running"}

# Para correr localmente: uvicorn app.main:app --reload

# /docs para ver la documentación de la API
