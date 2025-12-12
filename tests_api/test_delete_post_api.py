import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_delete_post():
    """
    DELETE /posts/1
    - Status code 200 o 204
    """
    response = requests.delete(f"{BASE_URL}/posts/1")

    assert response.status_code in [200, 204], \
        f"❌ Status inesperado: {response.status_code}"