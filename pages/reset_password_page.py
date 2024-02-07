import allure
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Найти иконку "Скрыть/Показать пароль"')
    def get_hide_show_password_icon(self):
        return self.find_element(ResetPasswordPageLocators.DIV_HIDE_SHOW_PASSWORD)

    @allure.step('Найти поле ввода "Пароль"')
    def get_password_input(self):
        return self.find_element(ResetPasswordPageLocators.INPUT_PASSWORD)
