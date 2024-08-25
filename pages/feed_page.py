from pages.account_page import *
from urls import *
from locators.main_page_locators import *
from locators.feed_page_locators import *
from seletools.actions import drag_and_drop


class FeedPage(AccountPage):

    @allure.step(f'Открываем страницу {feed_url}')
    def open_feed_page(self):
        self.driver.get(feed_url)

    @allure.step('Нажимаем на заказ')
    def click_feed_item(self):
        self.click_element(feed_item_xpath)

    @allure.step('Проверяем, что модальное окно открыто')
    def is_feed_modal_open(self):
        return self.is_visible_element(feed_item_modal_xpath)

    @allure.step('Проверяем, есть ли заказ в общем списке')
    def does_order_id_in_feed(self, order_id):
        self.is_visible_element(feed_item_xpath)
        return self.get_element((By.XPATH, f'.//p[text()="{order_id}"]'))

    @allure.step('Получаем общее количество заказов')
    def get_feed_count_all(self):
        return self.is_visible_element(feed_counter_all_xpath).text

    @allure.step('Получаем количество заказов за сегодня')
    def get_feed_count_today(self):
        return self.is_visible_element(feed_counter_today_xpath).text

    @allure.step('Получаем номер заказа в работе')
    def get_feed_in_work_id(self):
        return self.is_visible_element(feed_in_work_xpath).text
