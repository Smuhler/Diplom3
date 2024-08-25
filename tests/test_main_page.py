from conftest import *
from pages.account_page import *
from data import *


class TestMainPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_click_constructor(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_account_link()
        page.click_constructor_link()
        assert page.is_main_page() and page.check_current_url() == constructor_url

    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_click_feed(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_feed_link()
        assert page.is_feed_page() and page.check_current_url() == feed_url

    @allure.title('Проверяем модальное окно ингредиента')
    def test_click_bun_open_modal(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_bun()
        assert page.is_ingredient_modal_open() and page.check_current_url() == bun_modal_url

    @allure.title('Проверяем закрытие модального окна ингредиента')
    def test_close_modal_bun(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.click_bun()
        page.click_close_modal()
        page.is_main_page()
        assert not page.is_ingredient_modal_open() and page.check_current_url() == bun_modal_url

    @allure.title('Проверяем счетчик количества игредиента в корзине')
    def test_count_in_basket(self, driver):
        page = MainPage(driver)
        page.open_main_page()
        page.add_bun_to_basket()
        assert page.get_count_buns_in_basket() == '2'

    @allure.title('Проверяем создание заказа')
    def test_create_order(self, driver):
        page = AccountPage(driver)
        page.open_main_page()
        page.click_account_link()
        page.input_email_by_text(static_user_login)
        page.input_password_by_text(static_user_password)
        page.click_sign_in()
        page.is_main_page()
        page.add_bun_to_basket()
        page.click_create_order()
        assert page.is_order_created()
