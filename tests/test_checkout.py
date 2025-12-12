import pytest
import time

from utils.driver_setup import create_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def driver():
    """
    Fixture que crea y cierra el navegador.
    """
    driver = create_driver()
    yield driver
    driver.quit()


def test_checkout_flujo_completo(driver):
    """
    Valida un flujo completo de compra:
    - Login
    - Agregar producto al carrito
    - Ir al carrito
    - Iniciar checkout
    - Completar datos
    - Finalizar compra
    """
    # Paso 1: Login
    login_page = LoginPage(driver)
    login_page.abrir().login_completo("standard_user", "secret_sauce")
    time.sleep(1)

    # Paso 2: Página de inventario: agregar un producto
    inventory_page = InventoryPage(driver)
    inventory_page.agregar_primer_producto()
    time.sleep(1)

    # Paso 3: Ir al carrito
    cart_page = inventory_page.ir_al_carrito()
    time.sleep(1)

    # Paso 4: Iniciar checkout (ahora devuelve CheckoutPage)
    checkout_page = cart_page.proceder_checkout()
    time.sleep(1)

    # Paso 5: Completar datos y finalizar compra
    checkout_page.completar_informacion("Donna", "Wisner", "1234") \
                 .continuar() \
                 .finalizar()
    time.sleep(1)

    # Paso 6: Verificar mensaje de confirmación
    mensaje = checkout_page.obtener_mensaje_confirmacion()
    print(f"🧾 Mensaje de confirmación: {mensaje}")
    assert "Thank you" in mensaje, "❌ No se encontró el mensaje de confirmación de compra."

    # (Opcional) Verificar URL final
    assert "checkout-complete" in driver.current_url, \
        f"❌ La URL final no es la de checkout completo: {driver.current_url}"