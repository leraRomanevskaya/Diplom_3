from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    """Класс с локаторами страницы для ввода нового пароля."""
    DIV_HIDE_SHOW_PASSWORD = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
    INPUT_PASSWORD = (By.XPATH, './/input[@name="Введите новый пароль"]')
