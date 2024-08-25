from selenium.webdriver.common.by import By

feed_page_header_xpath = (By.XPATH, './/h1[text()="Лента заказов"]')
feed_item_xpath = (By.XPATH, './/h2[@class="text text_type_main-medium mb-2"][1]')
feed_item_modal_xpath = (By.XPATH, './/p[text()="Cостав"]')
feed_items_ids_xpath = (By.XPATH, './/p[@class="text text_type_digits-default"]')
feed_counter_all_xpath = (By.XPATH, './/p[text()="Выполнено за все время:"]/..//p[2]')
feed_counter_today_xpath = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/..//p[2]')
feed_in_work_xpath = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li')
