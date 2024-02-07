import allure
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Найти ссылку на "Конструктор"')
    def get_constructor_link(self):
        return self.find_element(FeedPageLocators.LINK_CONSTRUCTOR)

    @allure.step('Найти ссылку на "Восстановить пароль"')
    def get_orders_feed_link(self):
        return self.find_element(FeedPageLocators.LINK_ORDERS_FEED)

    @allure.step('Найти заголовок "Лента заказов"')
    def get_orders_feed_title(self):
        return self.find_element(FeedPageLocators.HEADING_ORDERS_FEED)

    @allure.step('Найти ссылку на первый заказ')
    def get_first_order_link(self):
        return self.find_element(FeedPageLocators.LINK_FIRST_ORDER)

    @allure.step('Получить значение счётчика "Выполнено за все время"')
    def get_done_by_all_time_counter(self):
        return self.find_element(FeedPageLocators.TEXT_COUNTER_DONE_BY_ALL_TIME).text

    @allure.step('Получить значение счётчика "Выполнено за сегодня"')
    def get_done_by_today_counter(self):
        return self.find_element(FeedPageLocators.TEXT_COUNTER_DONE_BY_TODAY).text

    @allure.step('Получить список номеров заказов из ленты')
    def get_orders_ids(self):
        orders = self.find_elements(FeedPageLocators.TEXT_ORDER_ID)
        return [order.text.lstrip('#').lstrip('0') for order in orders]

    @allure.step('Получить список номеров заказов из "В работе"')
    def get_in_work_orders_ids(self):
        orders = self.find_elements(FeedPageLocators.TEXT_ORDER_ID_IN_WORK)
        return [order.text.lstrip('#').lstrip('0') for order in orders]
