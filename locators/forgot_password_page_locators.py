from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    """Класс с локаторами страницы восстановления пароля."""
    INPUT_EMAIL = (By.XPATH, './/input[@name="name"]')
    BUTTON_RECOVER = (By.XPATH, './/form/button')
