import allure
from locators.account_page_locators import AccountPageLocators
from locators.feed_page_locators import FeedPageLocators
from pages.feed_page import FeedPage
from pages.account_page import AccountPage
from pages.main_page import MainPage
from methods import create_order
from urls import URL_HOME, URL_ACCOUNT_PROFILE, URL_ACCOUNT_ORDERS_HISTORY, URL_ORDERS_FEED


class TestOrdersFeed:

    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_by_order_opens_the_order_details(self, feed_page):
        feed_page.get_first_order_link().click()
        assert feed_page.is_visible(5, FeedPageLocators.DIV_MODAL_CONTAINER)
        assert feed_page.is_visible(5, FeedPageLocators.BUTTON_MODAL_CLOSE)

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_from_orders_history_presented_in_the_orders_feed(self, authorize_user):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        order_id = create_order(credentials, main_page)['order_id']
        main_page.get_account_link().click()
        main_page.wait_for_url(5, URL_ACCOUNT_PROFILE)
        account_page = AccountPage(main_page.get_driver())
        account_page.get_orders_history_link().click()
        account_page.wait_for_url(5, URL_ACCOUNT_ORDERS_HISTORY)
        account_page.wait_until_visible(5, AccountPageLocators.TEXT_ORDER_ID)
        history_orders_ids = account_page.get_orders_ids()
        account_page.get_orders_feed_link().click()
        account_page.wait_for_url(5, URL_ORDERS_FEED)
        orders_feed = FeedPage(account_page.get_driver())
        feed_orders_ids = orders_feed.get_orders_ids()
        assert len(set(history_orders_ids) - set(feed_orders_ids))

    @allure.title('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('При создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_create_new_order_updates_done_by_all_time_counter(self, authorize_user):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_until_visible(5, FeedPageLocators.TEXT_COUNTER_DONE_BY_ALL_TIME)
        done_by_all_time_counter_before = feed_page.get_done_by_all_time_counter()
        feed_page.get_constructor_link().click()
        feed_page.wait_for_url(5, URL_HOME)
        main_page = MainPage(feed_page.get_driver())
        order_id = create_order(credentials, main_page)['order_id']
        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_for_text_not_equals(5, FeedPageLocators.TEXT_COUNTER_DONE_BY_ALL_TIME, done_by_all_time_counter_before)
        done_by_all_time_counter_after = feed_page.get_done_by_all_time_counter()
        assert int(done_by_all_time_counter_before) < int(done_by_all_time_counter_after)

    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    @allure.description('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_create_new_order_updates_done_by_today_counter(self, authorize_user):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_until_visible(5, FeedPageLocators.TEXT_COUNTER_DONE_BY_TODAY)
        done_by_today_counter_before = feed_page.get_done_by_today_counter()
        feed_page.get_constructor_link().click()
        feed_page.wait_for_url(5, URL_HOME)
        main_page = MainPage(feed_page.get_driver())
        order_id = create_order(credentials, main_page)['order_id']
        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_for_text_not_equals(5, FeedPageLocators.TEXT_COUNTER_DONE_BY_TODAY, done_by_today_counter_before)
        done_by_today_counter_after = feed_page.get_done_by_today_counter()
        assert int(done_by_today_counter_before) < int(done_by_today_counter_after)

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    @allure.description('После оформления заказа его номер появляется в разделе В работе')
    def test_create_new_order_updates_list_of_in_work_orders(self, authorize_user):
        credentials = authorize_user['credentials']
        main_page = authorize_user['main_page']
        order_id = create_order(credentials, main_page)['order_id']
        main_page.get_orders_feed_link().click()
        main_page.wait_for_url(5, URL_ORDERS_FEED)
        feed_page = FeedPage(main_page.get_driver())
        feed_page.wait_for_text_not_equals(5, FeedPageLocators.TEXT_ORDER_ID_IN_WORK, "Все текущие заказы готовы!")
        order_ids = feed_page.get_in_work_orders_ids()
        assert order_id in order_ids
