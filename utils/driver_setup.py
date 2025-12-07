from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def create_driver():
    """
    Crea una instancia del navegador Chrome usando webdriver-manager.
    """
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.saucedemo.com")
    return driver