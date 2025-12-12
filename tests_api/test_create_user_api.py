import requests
from utils.logger import get_logger

log = get_logger(__name__)

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_create_post():
    """
    POST /posts
    - Status code 201
    - El body devuelto coincide con lo enviado
    - Contiene un id generado
    """
    payload = {
        "title": "Nuevo Post",
        "body": "Contenido de prueba",
        "userId": 1
    }
    log.info("Iniciando test API: crear post")
    log.info(f"Enviando POST /posts con payload: {payload}")

    response = requests.post(f"{BASE_URL}/posts", json=payload)
    log.info(f"Respuesta recibida con status code: {response.status_code}")
    
    assert response.status_code == 201, f"❌ Status inesperado: {response.status_code}"

    data = response.json()

    log.info(f"Post creado correctamente con ID: {data.get('id')}")

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data, "❌ Falta la clave 'id' en la respuesta."