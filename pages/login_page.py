from pages.main_page import *
from urls import *
from locators.login_page_locators import *
from data import *


class LoginPage(MainPage):

    @allure.step(f'Открываем страницу {login_url}')
    def open_login_page(self):
        self.driver.get(login_url)

    @allure.step('Кликаем на восстановить пароль')
    def click_forgot_password(self):
        self.click_element(login_forgot_password_link_xpath)

    @allure.step('Заполняем почту')
    def input_email_by_text(self, text):
        self.input_text(login_email_input_xpath, text)

    @allure.step('Заполняем пароль')
    def input_password_by_text(self, text):
        self.input_text(login_password_input_xpath, text)

    @allure.step('Клик по кнопке отображения пароля в строке ввода')
    def click_password_visible(self):
        self.click_element(login_password_visible_xpath)

    @allure.step('Проверяем активно ли поле ввода пароля')
    def is_password_active(self):
        return 'input_status_active' in self.get_attribute_of_element(login_password_xpath, 'class')

    @allure.step('Нажимаем "войти"')
    def click_sign_in(self):
        self.click_element(login_button_xpath)

    @allure.step('Проверяем, что находимся на странице авторизации')
    def is_login_page(self):
        return self.is_visible_element(login_header_xpath)

    @allure.step('Авторизуемся статичным пользователем')
    def login(self):
        self.open_main_page()
        self.click_account_link()
        self.input_email_by_text(static_user_login)
        self.input_password_by_text(static_user_password)
        self.click_sign_in()
        self.is_main_page()
