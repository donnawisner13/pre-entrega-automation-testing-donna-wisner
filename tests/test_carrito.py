"""
Añadir un producto al carrito haciendo clic en el botón correspondiente
Verificar que el contador del carrito se incremente correctamente
Navegar al carrito de compras
Comprobar que el producto añadido aparezca correctamente en el carrito
"""
import pytest
import time

from utils.driver_setup import create_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

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
    y que aparezca correctamente listado, usando Page Objects.
    """
    # Paso 1: Login usando LoginPage
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    time.sleep(2)

    # Paso 2: Usar InventoryPage para agregar el primer producto
    inventory_page = InventoryPage(driver)
    inventory_page.agregar_primer_producto()
    time.sleep(2)

    # Paso 3: Validar que el contador del carrito sea 1
    contador = inventory_page.obtener_contador_carrito()
    assert contador == 1, f"❌ El contador del carrito no es 1, es {contador}"
    print("✅ Producto agregado correctamente (contador = 1)")
    time.sleep(1)

    # Paso 4: Ir al carrito (devuelve CartPage)
    cart_page = inventory_page.ir_al_carrito()
    time.sleep(2)

    # Paso 5: Verificar que haya al menos un producto en el carrito
    cart_items = cart_page.obtener_productos_en_carrito()
    assert len(cart_items) >= 1, "❌ No se encontró ningún producto en el carrito."
    print(f"🧾 Verificación del carrito exitosa (hay {len(cart_items)} productos listados).")
    time.sleep(1)