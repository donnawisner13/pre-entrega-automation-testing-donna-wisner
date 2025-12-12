import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# conftest.py (fragmento - NO reemplaces tu código anterior)
def pytest_html_results_table_header(cells):
    """Añade una columna 'URL' justo después de 'Test ID'."""
    cells.insert(2, 'URL')
def pytest_html_results_table_row(report, cells):
    """Rellena la columna con la URL almacenada en el atributo
    'page_url'."""
    cells.insert(2, getattr(report, 'page_url', '-'))

@pytest.fixture
def driver():
    """Crea y cierra el navegador para cada test."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.implicitly_wait(5)

    yield driver
    driver.quit()


@pytest.fixture
def credenciales_validas():
    """Fixture para login exitoso."""
    return {
        "usuario": "standard_user",
        "password": "secret_sauce"
    }

# 📸 Guardar screenshot al fallar
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook de Pytest que se ejecuta después de cada test.
    Si un test falla y tiene fixture 'driver', se toma screenshot.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver:
            # Crear carpeta si no existe
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Nombre del archivo
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            test_name = item.name.replace(" ", "_")
            filename = f"{screenshots_dir}/{test_name}_{timestamp}.png"

            # Guardar screenshot
            driver.save_screenshot(filename)

            # Adjuntar al reporte HTML
            if hasattr(report, "extra"):
                from pytest_html import extras
                report.extra.append(extras.image(filename))