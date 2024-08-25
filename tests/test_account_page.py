from conftest import *
from pages.account_page import *
from data import *


class TestAccountPage:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    def test_login_click_account(self, driver):
        page = AccountPage(driver)
        page.open_main_page()
        page.click_account_link()
        page.input_email_by_text(static_user_login)
        page.input_password_by_text(static_user_password)
        page.click_sign_in()
        page.is_main_page()
        page.click_account_link()
        assert page.is_profile_page() and page.check_current_url() == account_profile_url

    @allure.title('Проверяем переход в раздел «История заказов»')
    def test_login_click_feed(self, driver):
        page = AccountPage(driver)
        page.open_main_page()
        page.click_account_link()
        page.input_email_by_text(static_user_login)
        page.input_password_by_text(static_user_password)
        page.click_sign_in()
        page.is_main_page()
        page.click_feed_link()
        assert page.check_current_url() == feed_url

    @allure.title('Проверяем выход из аккаунта')
    def test_login_click_quit(self, driver):
        page = AccountPage(driver)
        page.open_main_page()
        page.click_account_link()
        page.input_email_by_text(static_user_login)
        page.input_password_by_text(static_user_password)
        page.click_sign_in()
        page.is_main_page()
        page.click_account_link()
        page.is_profile_page()
        page.click_quit()
        assert page.is_login_page() and page.check_current_url() == login_url
