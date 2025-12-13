import pytest
import time

from utils.driver_setup import create_driver
from utils.data_loader import leer_datos_login_desde_csv
from pages.login_page import LoginPage
pytestmark = pytest.mark.ui

@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()


# Cargamos los datos desde el CSV
datos_login = leer_datos_login_desde_csv("datos/usuarios_login.csv")


@pytest.mark.parametrize("usuario,clave,debe_funcionar", datos_login)
def test_login_parametrizado(driver, usuario, clave, debe_funcionar):
    """
    Prueba el login con distintos usuarios y claves leídos desde un CSV.
    - Si debe_funcionar es True: valida que el login sea exitoso.
    - Si debe_funcionar es False: valida que aparezca mensaje de error.
    """
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login_completo(usuario, clave)
    time.sleep(1)

    if debe_funcionar:
        # Esperamos que el login sea exitoso
        assert "/inventory.html" in driver.current_url, \
            f"❌ Se esperaba login exitoso para {usuario}, pero no se redirigió al inventario."
        assert not login_page.esta_error_visible(), \
            f"❌ Apareció un error inesperado para el usuario {usuario}."
        print(f"✅ Login exitoso con usuario: {usuario}")
    else:
        # Esperamos que falle el login
        assert login_page.esta_error_visible(), \
            f"❌ Se esperaba un error de login para {usuario}, pero no se mostró mensaje de error."
        mensaje = login_page.obtener_mensaje_error()
        print(f"⚠️ Login inválido para usuario {usuario}. Mensaje: {mensaje}")
        assert mensaje != "", "❌ No se obtuvo mensaje de error."