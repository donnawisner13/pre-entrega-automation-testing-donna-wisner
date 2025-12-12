import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_list_users_structure():
    """
    GET /users
    - Status code 200
    - La respuesta es una lista
    - Cada usuario contiene: id, name, username, email
    """
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200, f"❌ Status inesperado: {response.status_code}"

    users = response.json()

    assert isinstance(users, list), "❌ La respuesta no es una lista."
    assert len(users) > 0, "❌ La lista de usuarios está vacía."

    for user in users:
        for key in ["id", "name", "username", "email"]:
            assert key in user, f"❌ Falta la clave '{key}' en: {user}"