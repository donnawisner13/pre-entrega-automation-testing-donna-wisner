from selenium.webdriver.common.by import By


def login(driver):
    """
    Realiza el login en saucedemo.com con credenciales válidas.
    """
    # Completar usuario
    username_input = driver.find_element(By.ID, "user-name")
    username_input.clear()
    username_input.send_keys("standard_user")

    # Completar contraseña
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("secret_sauce")

    # Click en el botón de login
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()
    