import pytest
import time

from utils.driver_setup import create_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
pytestmark = pytest.mark.ui

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


def test_logout_flujo_completo(driver):
    """
    Verifica que el usuario pueda cerrar sesión correctamente:
    - Login
    - Llegar al inventario
    - Abrir menú
    - Hacer logout
    - Volver a la página de login
    """
    # Paso 1: Login
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    time.sleep(1)

    # Paso 2: Estamos en inventario
    inventory_page = InventoryPage(driver)
    assert "/inventory.html" in driver.current_url, "❌ No se llegó al inventario después del login."

    # Paso 3: Se llama al método hacer_logout()
    login_page_nueva = inventory_page.hacer_logout()
    time.sleep(1)

    # # Paso 4: Validamos que volvimos al login
    assert login_page_nueva.URL in driver.current_url, \
        f"❌ No se volvió a la página de login. URL actual: {driver.current_url}"

    print("✅ Logout realizado correctamente.")