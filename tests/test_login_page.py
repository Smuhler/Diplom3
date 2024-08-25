from conftest import *
from pages.login_page import *


class TestLoginPage:

    @allure.title('Проверяем диплинк восстановления пароля')
    def test_login_click_forgot_password_link(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.click_forgot_password()
        assert page.check_current_url() == forgot_password_url

    @allure.title('Проверяем диплинк восстановления пароля с заполненной почтой')
    def test_login_click_forgot_password_link_after_input_email(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.input_email_by_text('vsem_privet')
        page.click_forgot_password()
        assert page.check_current_url() == forgot_password_url

    @allure.title('Проверяем кнопку отображения пароля')
    def test_login_click_password_visible(self, driver):
        page = LoginPage(driver)
        page.open_login_page()
        page.input_password_by_text('vsem_privet')
        page.click_password_visible()
        assert page.is_password_active()
