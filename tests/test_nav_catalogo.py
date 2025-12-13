"""
Pruebas de navegación y verificación del catálogo en saucedemo.com.
Criterios mínimos:
- Validar título de inventario.
- Comprobar que hay productos visibles.
- Validar elementos importantes de la interfaz (menú, filtros).
"""

import pytest
import time
from selenium.webdriver.common.by import By
from utils.driver_setup import create_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
pytestmark = pytest.mark.ui
@pytest.fixture
def driver():
    """
    Fixture de Pytest que crea y cierra el navegador automáticamente.
    """
    driver = create_driver()
    yield driver
    driver.quit()

def test_verificar_titulo_y_elementos(driver):
    """
    Verifica que el título, la presencia de productos
    y los elementos clave del catálogo usando Page Objects.
    """
    # Paso 1: Login usando LoginPage
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    time.sleep(1)

    # Paso 2: Crear InventoryPage
    inventory_page = InventoryPage(driver)

    # Paso 3: Validar título
    titulo = inventory_page.obtener_titulo()
    assert titulo in ["Products", "Swag Labs"], f"Título inesperado: {titulo}"
    print(f"✅ Título correcto: {titulo}")

    # Paso 4: Validar que haya al menos un producto visible
    productos = inventory_page.obtener_productos()
    assert len(productos) >= 1, "❌ No se encontró ningún producto visible en el catálogo."
    print(f"🛒 Se encontraron {len(productos)} productos visibles.")

    # Paso 5: Validar elementos importantes de la interfaz
    menu_button = driver.find_element(*InventoryPage._MENU_BUTTON)
    assert menu_button.is_displayed(), "❌ Botón de menú no visible."

    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filter_dropdown.is_displayed(), "❌ Filtro de productos no visible."

    print("✅ Elementos clave de la interfaz presentes y visibles.")
    time.sleep(1)