import pytest

from api_methods import generate_user_credentials
from api_methods import register_user as api_register_user
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from pages.forgot_password_page import ForgotPasswordPage
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FS
from urls import URL_HOME, URL_LOGIN, URL_RESET_PASSWORD, URL_FORGOT_PASSWORD, URL_ORDERS_FEED
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['firefox', 'chrome'])  # драйвер для setup и teardown браузера
def driver(request):
    if request.param == 'firefox':
        firefox_driver = GeckoDriverManager().install()
        service = FS(firefox_driver)
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    driver.get(URL_HOME)
    return MainPage(driver)


@pytest.fixture()
def login_page(driver):
    driver.get(URL_LOGIN)
    return LoginPage(driver)


@pytest.fixture()
def reset_password_page(driver):
    driver.get(URL_RESET_PASSWORD)
    return ResetPasswordPage(driver)


@pytest.fixture()
def forgot_password_page(driver):
    driver.get(URL_FORGOT_PASSWORD)
    return ForgotPasswordPage(driver)


@pytest.fixture()
def feed_page(driver):
    driver.get(URL_ORDERS_FEED)
    return FeedPage(driver)


@pytest.fixture()
def register_user(driver):
    credentials = generate_user_credentials()
    api_register_user(credentials)
    return {
        'credentials': credentials
    }


@pytest.fixture()
def authorize_user(driver, register_user, main_page):
    credentials = register_user['credentials']
    main_page.get_account_link().click()
    main_page.wait_for_url(5, URL_LOGIN)
    login_page = LoginPage(main_page.get_driver())
    login_page.get_email_input().send_keys(credentials['email'])
    login_page.get_password_input().send_keys(credentials['password'])
    login_page.get_enter_button().click()
    login_page.wait_for_url(5, URL_HOME)
    main_page = MainPage(login_page.get_driver())
    return {
        'credentials': credentials,
        'main_page': main_page
    }
