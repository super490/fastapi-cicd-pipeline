from fastapi.testclient import (
    TestClient,  # Es una herramienta de FastAPI para hacer peticiones a tu aplicación
)

from app.main import (
    app,  # Es la instancia de tu aplicación FastAPI que definiste en tu archivo main.py.
)

client = TestClient(app) # Crea una instancia del cliente de pruebas que apuntará a tu aplicación.

def test_health_endpoint():
    response = client.get("/health") # El cliente envía una petición de tipo GET a la ruta /health.
    assert response.status_code == 200 # : Verifica que el servidor respondió con un código HTTP 200
    data = response.json() # Convierte el cuerpo de la respuesta en un diccionario de Python
    assert data["status"] == "ok" # Comprueba que dentro del JSON recibido, revise el valor "ok"
    assert "message" in data #Verifica que la palabra "message" exista como una clave del dicc..

"""
El código realiza una prueba de integración básica.
Su objetivo es simular un cliente que visita la URL /health de tu aplicación y verificar tres cosas:

Que el servidor responde con éxito (Código 200).

Que el contenido de la respuesta indica un estado "ok".

Que la respuesta contiene un campo llamado "message".

"""
