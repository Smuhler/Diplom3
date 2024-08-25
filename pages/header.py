from pages.base_page import *
from locators.header_locators import *


class Header(BasePage):

    @allure.step('Переходим в конструктор')
    def click_constructor_link(self):
        self.click_element(header_constructor_link_xpath)

    @allure.step('Переходим в ленту заказов')
    def click_feed_link(self):
        self.click_element(header_feed_link_xpath)

    @allure.step('Кликаем по лого Stelar Burger')
    def click_logo_link(self):
        self.click_element(header_logo_xpath)

    @allure.step('Переходим в личный кабинет')
    def click_account_link(self):
        self.click_element(header_account_link_xpath)
