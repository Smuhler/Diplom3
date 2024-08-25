from pages.header import *
from urls import *
from locators.main_page_locators import *
from locators.feed_page_locators import *
from seletools.actions import drag_and_drop


class MainPage(Header):

    @allure.step(f'Открываем страницу {main_url}')
    def open_main_page(self):
        self.driver.get(main_url)

    @allure.step('Проверяем, что находимся на главной странице')
    def is_main_page(self):
        return self.is_visible_element(main_page_header_xpath)

    @allure.step('Проверяем, что находимся на странице истории заказов')
    def is_feed_page(self):
        return self.is_visible_element(feed_page_header_xpath)

    @allure.step('Нажимаем на булочку')
    def click_bun(self):
        self.click_element(main_bun_xpath)

    @allure.step('Проверяем, открыто ли модальное окно')
    def is_ingredient_modal_open(self):
        return 'Modal_modal_opened__3ISw4' in self.get_attribute_of_element(main_bun_modal_xpath, 'class')

    @allure.step('Закрываем модальное окно')
    def click_close_modal(self):
        self.click_element(main_bun_modal_close_xpath)

    @allure.step('Добавляем булочку в корзину')
    def add_bun_to_basket(self):
        source_element = self.is_clickable_element(main_bun_xpath)
        target_element = self.is_clickable_element(main_burger_constructor_basket2)
        drag_and_drop(self.driver, source_element, target_element)

    @allure.step('Проверяем количество булочек в корзине')
    def get_count_buns_in_basket(self):
        return self.get_text_from_visible_element(main_bun_counter_xpath)

    @allure.step('Создаем заказ')
    def click_create_order(self):
        self.click_element(main_order_create_button_xpath)

    @allure.step('Проверяем, что заказ создан')
    def is_order_created(self):
        return 'Ваш заказ начали готовить' in self.get_text_from_visible_element(main_order_modal_ready_text_xpath)
