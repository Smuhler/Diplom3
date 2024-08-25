from selenium.webdriver.common.by import By

account_logout_button_xpath = (By.XPATH, './/button[text()="Выход"]')  # путь до кнопки "Выход"
account_order_history_button_xpath = (By.XPATH, './/a[text()="История заказов"]')  # путь до кнопки "Выход"
account_profile_link_xpath = (By.XPATH, './/a[text()="Профиль"]')  # путь до ссылки "Профиль"
order_history_item_id_xpath = (By.XPATH, './/p[@class="text text_type_digits-default"]')
