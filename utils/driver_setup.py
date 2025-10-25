from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_driver():
    """Crea una instancia simple de Chrome en modo incógnito."""
    chrome_options = Options()
    chrome_options.add_argument("--incognito")       #  modo incógnito para saltear la advertencia de seguridad de contraseña
    chrome_options.add_argument("--start-maximized") #  ventana completa
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.implicitly_wait(5)
    return driver