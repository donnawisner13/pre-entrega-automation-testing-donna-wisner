"""
Navegar a la página de login de saucedemo.com
Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
Validar login exitoso verificando que se haya redirigido a la página de inventario
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import create_driver_simple
from utils.funciones_auxiliares import login

@pytest.fixture
def driver():
    """
    Fixture de Pytest que crea y cierra el navegador automáticamente.
    """
    driver = create_driver_simple()
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    """
    Test que valida que el login se realice correctamente.
    """
    # Paso 1: Ingresar al sitio y hacer login usando la función auxiliar
    login(driver)

    # Paso 2: Espera explícita a que la URL cambie a /inventory.html
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))

    # Paso 3: Validar URL
    assert "/inventory.html" in driver.current_url, "❌ No se redirigió correctamente a /inventory.html"

    # Paso 4: Validar título “Products” o “Swag Labs”
    app_logo = driver.find_element(By.CLASS_NAME, "app_logo").text
    header_title = driver.find_element(By.CLASS_NAME, "title").text
    assert (app_logo == "Swag Labs") or ("Products" in header_title), \
        f"❌ Título inesperado. app_logo='{app_logo}', header='{header_title}'"

    print("✅ Test Login OK")