"""
Funciones auxiliares  llamadas desde los tests de Pytest.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver):
    """
    Realiza el inicio de sesión en saucedemo.com con credenciales válidas.
    """
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def agregar_primer_producto(driver):
    """
    Agrega el primer producto de la lista al carrito.
    """
    wait = WebDriverWait(driver, 10)

    botones_carrito = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory")))
    if not botones_carrito:
        raise Exception(" No se encontraron botones 'Add to cart'.")

    boton_carrito = botones_carrito[0]
    print(f"🖱️ Clic en botón: {boton_carrito.text}")
    boton_carrito.click()

    # Esperar a que cambie el texto del botón a "Remove" (indica que se agregó)
    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "btn_inventory"), "Remove"))
    print(" Producto agregado correctamente al carrito.")

def obtener_contador_carrito(driver):
    """
    Devuelve el número que aparece en el badge del carrito.
    """
    wait = WebDriverWait(driver, 10)
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    return badge.text