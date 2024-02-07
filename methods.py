import allure
import random
import requests
import string

from locators.main_page_locators import MainPageLocators


@allure.step('Генерируем учётные данные пользоваться')
def generate_user_credentials(exclude_email=False, exclude_password=False, exclude_name=False) -> dict:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    credentials = {}

    if not exclude_email:
        credentials['email'] = generate_random_string(8) + '@ya.ru'

    if not exclude_password:
        credentials['password'] = generate_random_string(12)

    if not exclude_name:
        credentials['name'] = generate_random_string(8)

    return credentials


@allure.step('Регистрируем пользователя')
def register_user(credentials) -> requests.Response:
    return requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', json=credentials)


@allure.step('Создаём заказ')
def create_order(credentials, main_page):
    main_page.drag_and_drop_first_ingredient_onto_top_slot()
    main_page.get_create_order_button().click()
    assert main_page.is_visible(5, MainPageLocators.TEXT_MODAL_ORDER_NUMBER)
    order_id = main_page.wait_for_text_not_equals(15, MainPageLocators.TEXT_MODAL_ORDER_NUMBER, '9999')
    assert order_id is not None
    main_page.get_modal_close_button().click()
    return {
        'credentials': credentials,
        'main_page': main_page,
        'order_id': order_id
    }
