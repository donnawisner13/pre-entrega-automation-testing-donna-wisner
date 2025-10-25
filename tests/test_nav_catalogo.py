"""
Verificar que el título de la página de inventario sea correcto
Comprobar que existan productos visibles en la página (al menos verificar la presencia de uno)
Validar que elementos importantes de la interfaz estén presentes (menú, filtros, etc.)
"""

"""
Pruebas de navegación y verificación del catálogo en saucedemo.com.
Criterios mínimos:
- Validar título de inventario.
- Comprobar que hay productos visibles.
- Validar elementos importantes de la interfaz (menú, filtros).
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import create_driver
from utils.funciones_auxiliares import login

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
    Verifica que el título de la página sea correcto
    y que los elementos clave del catálogo estén presentes.
    """
    # Paso 1: Login
    login(driver)

    # Paso 2: Espera explícita a que se cargue la página de inventario
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/inventory.html"))

    # Paso 3: Validar título
    header_title = driver.find_element(By.CLASS_NAME, "title").text
    app_logo = driver.find_element(By.CLASS_NAME, "app_logo").text
    assert (app_logo == "Swag Labs") or ("Products" in header_title), \
        f"❌ Título inesperado. app_logo='{app_logo}', header='{header_title}'"

    # Paso 4: Validar que haya al menos un producto visible
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) >= 1, "❌ No se encontró ningún producto visible en el catálogo."
    print(f"✅ Se encontraron {len(productos)} productos visibles en la página.")

    # Paso 5: Validar elementos importantes de la interfaz
    # Menú de hamburguesa
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    assert menu_button.is_displayed(), "❌ Botón de menú no visible."

    # Filtro de productos
    filter_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filter_dropdown.is_displayed(), "❌ Filtro de productos no visible."

    print("✅ Elementos clave de la interfaz presentes y visibles.")