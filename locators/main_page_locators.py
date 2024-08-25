from selenium.webdriver.common.by import By

main_login_button_xpath = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')  # путь до кнопки "Войти в аккаунт"
main_page_header_xpath = (By.XPATH, './/h1[text()="Соберите бургер"]')
main_bun_xpath = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]')
main_bun_modal_header_xpath = (By.XPATH, './/h2[text()="Детали ингредиента"]')
main_bun_modal_close_xpath = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
main_bun_modal_xpath = (By.XPATH, './/div[@class="Modal_modal__container__Wo2l_"]/..')
main_bun_span_xpath = (By.XPATH, './/span[text()="Булки"]')  # путь до кнопки навигации "Булки"
main_bun_span_selected_xpath = (By.XPATH, './/span[text()="Булки"]/parent::div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')  # путь отображения выбранной кнопки навигации "Булки"
main_sauce_span_xpath = (By.XPATH, './/span[text()="Соусы"]')  # путь до кнопки навигации "Соусы"
main_sauce_span_selected_xpath = (By.XPATH, './/span[text()="Соусы"]/parent::div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')  # путь отображения выбранной кнопки навигации "Соусы"
main_filling_span_xpath = (By.XPATH, './/span[text()="Начинки"]')  # путь до кнопки навигации "Начинки"
main_filling_span_selected_xpath = (By.XPATH, './/span[text()="Начинки"]/parent::div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')  # путь отображения выбранной кнопки навигации "Начинки"
main_burger_constructor_basket_xpath = (By.XPATH, './/li[@class="BurgerConstructor_basket__listItem__aWMu1 mr-4"]')
main_burger_constructor_basket2 = (By.XPATH, './/span[text()="Перетяните булочку сюда (низ)"]')
main_bun_counter_xpath = (By.XPATH, './/p[@class="counter_counter__num__3nue1"]')
main_basket_added_bun_xpath = (By.XPATH, './/span[text()="Флюоресцентная булка R2-D3 (верх)"]')
main_order_create_button_xpath = (By.XPATH, './/button[text()="Оформить заказ"]')
main_order_modal_ready_text_xpath = (By.XPATH, './/p[@class="undefined text text_type_main-small mb-2"]')
