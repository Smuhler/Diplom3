from conftest import *
from pages.feed_page import *
from helpers import *


class TestFeedPage:

    @allure.title('Проверяем модальное окно в истории заказов')
    def test_click_feed_open_modal(self, driver):
        page = FeedPage(driver)
        page.open_feed_page()
        page.click_feed_item()
        assert page.is_feed_modal_open()

    @allure.title('Проверяем, что заказы пользователя отображатся в истории заказов')
    @allure.description('Создаем новый заказ, получаем его номер из заказов пользователя и ищем этот заказ на странице истории заказов')
    def test_order_user_shown_in_feed(self, driver):
        page = FeedPage(driver)
        page.login()
        page.add_bun_to_basket()
        page.click_create_order()
        page.open_order_history_page()
        order_id = page.get_user_last_order_id()
        page.click_feed_link()
        assert page.does_order_id_in_feed(order_id)

    @allure.title('Проверяем счетчик всех заказов')
    def test_feed_all_orders_counter(self, driver):
        page = FeedPage(driver)
        page.open_feed_page()
        count = page.get_feed_count_all()
        create_order()
        assert int(page.get_feed_count_all()) > int(count)

    @allure.title('Проверяем счетчик заказов за сегодня')
    def test_feed_today_orders_counter(self, driver):
        page = FeedPage(driver)
        page.open_feed_page()
        count = page.get_feed_count_today()
        create_order()
        assert int(page.get_feed_count_today()) > int(count)

    @allure.title('Проверяем что заказы в работе корректно отображатся')
    def test_feed_in_work_id(self, driver):
        page = FeedPage(driver)
        page.open_feed_page()
        order_id = create_order()
        assert order_id == int(page.get_feed_in_work_id())
