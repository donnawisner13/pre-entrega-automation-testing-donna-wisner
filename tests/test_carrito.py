"""
Añadir un producto al carrito haciendo clic en el botón correspondiente
Verificar que el contador del carrito se incremente correctamente
Navegar al carrito de compras
Comprobar que el producto añadido aparezca correctamente en el carrito
"""
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import create_driver
from utils.funciones_auxiliares import login, agregar_primer_producto, obtener_contador_carrito

@pytest.fixture
def driver():
    """
    Fixture de Pytest que crea y cierra el navegador automáticamente.
    """
    driver = create_driver()
    yield driver
    driver.quit()

def test_agregar_producto_al_carrito(driver):
    """
    Test que valida que se pueda agregar un producto al carrito
    y que aparezca correctamente listado.
    """
    # Paso 1: Login
    login(driver)
    time.sleep(2)

    # Paso 2: Agregar el primer producto
    agregar_primer_producto(driver)
    time.sleep(2)

    # Paso 3: Validar que el contador del carrito sea 1
    contador = obtener_contador_carrito(driver)
    assert contador == "1", f" El contador del carrito no es 1, es {contador}"
    print(" Producto agregado correctamente (contador = 1)")
    time.sleep(2)

    # Paso 4: Ingresar al carrito
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()
    time.sleep(2)

    # Paso 5: Espera explícita a que se cargue la página del carrito
    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_contains("/cart.html"))
    time.sleep(2)

    # Paso 6: Verificar que haya al menos un producto en el carrito
    cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(cart_items) >= 1, " No se encontró ningún producto en el carrito."
    print(f"🧾 Verificación del carrito exitosa (hay {len(cart_items)} productos listados).")
    time.sleep(2)