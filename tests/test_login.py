"""
Navegar a la página de login de saucedemo.com
Ingresar credenciales válidas (usuario: "standard_user", contraseña: "secret_sauce")
Validar login exitoso verificando que se haya redirigido a la página de inventario
"""

import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import create_driver
from pages.login_page import LoginPage

from utils.logger import get_logger
log = get_logger(__name__)

@pytest.fixture
def driver():
    """
    Fixture de Pytest que crea y cierra el navegador automáticamente.
    """
    driver = create_driver()
    yield driver
    driver.quit()

def test_login_exitoso(driver):
    """
    Test que valida que el login se realice correctamente usando Page Object.
    """
    log.info("Iniciando test de login")
    # Crear la página de login con el driver
    login_page = LoginPage(driver)

    # Abrir la página y hacer login completo
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    time.sleep(2)
    log.info("Login realizado, validando inventario")
    
    # Espera explícita a que la URL cambie a /inventory.html
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))
    time.sleep(1)

    # Validar URL
    assert  "/inventory.html" in driver.current_url, "❌ No se redirigió correctamente a /inventory.html"

    # Validar título “Products” o “Swag Labs”
    app_logo = driver.find_element(By.CLASS_NAME, "app_logo").text
    header_title = driver.find_element(By.CLASS_NAME, "title").text
    assert (app_logo == "Swag Labs") or ("Products" in header_title), \
        f"❌ Título inesperado. app_logo='{app_logo}', header='{header_title}'"

    print("✅ Test Login OK (POM)")
    time.sleep(1)
