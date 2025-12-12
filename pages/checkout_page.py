from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # LOCATORS
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _CONTINUE_BUTTON = (By.ID, "continue")
    _FINISH_BUTTON = (By.ID, "finish")
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Esperar a estar en alguna URL de checkout
        self.wait.until(EC.url_contains("checkout"))

    def completar_informacion(self, nombre: str, apellido: str, codigo_postal: str):
        """
        Completa los datos requeridos para avanzar con el checkout.
        """
        first_name = self.driver.find_element(*self._FIRST_NAME)
        last_name = self.driver.find_element(*self._LAST_NAME)
        postal_code = self.driver.find_element(*self._POSTAL_CODE)

        first_name.clear()
        first_name.send_keys(nombre)

        last_name.clear()
        last_name.send_keys(apellido)

        postal_code.clear()
        postal_code.send_keys(codigo_postal)

        return self

    def continuar(self):
        """Avanza a la página de revisión."""
        self.driver.find_element(*self._CONTINUE_BUTTON).click()
        return self

    def finalizar(self):
        """Hace clic en Finish para completar la compra."""
        self.driver.find_element(*self._FINISH_BUTTON).click()
        return self

    def obtener_mensaje_confirmacion(self) -> str:
        """
        Retorna el mensaje final que confirma la compra.
        Ejemplo: "Thank you for your order!"
        """
        header = self.wait.until(EC.visibility_of_element_located(self._COMPLETE_HEADER))
        return header.text