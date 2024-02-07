import allure
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Найти поле ввода "Email"')
    def get_email_input(self):
        return self.find_element(ForgotPasswordPageLocators.INPUT_EMAIL)

    @allure.step('Найти кнопку "Восстановить"')
    def get_recover_button(self):
        return self.find_element(ForgotPasswordPageLocators.BUTTON_RECOVER)
