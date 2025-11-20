import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

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