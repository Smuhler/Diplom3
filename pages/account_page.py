from pages.login_page import *
from urls import *
from locators.account_page_locators import *


class AccountPage(LoginPage):

    @allure.step(f'Открываем страницу {account_url}')
    def open_account_page(self):
        self.driver.get(account_url)

    @allure.step(f'Открываем страницу истории заказов')
    def open_order_history_page(self):
        self.open_account_page()
        self.click_element(account_order_history_button_xpath)

    @allure.step('Получаем номер последнего заказа в истории заказов')
    def get_user_last_order_id(self):
        self.is_visible_element(order_history_item_id_xpath)
        return self.get_list_of_elements(order_history_item_id_xpath)[-1].text

    @allure.step('Проверяем, что это страница профиля')
    def is_profile_page(self):
        return self.is_visible_element(account_profile_link_xpath)

    @allure.step('Нажимаем кнопку выход')
    def click_quit(self):
        self.click_element(account_logout_button_xpath)
