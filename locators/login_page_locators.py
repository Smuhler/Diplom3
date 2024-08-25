from selenium.webdriver.common.by import By

login_email_xpath = (By.XPATH, './/label[text()="Email"]/..')  # путь до элемента ввода почты
login_email_input_xpath = (By.XPATH, './/input[@name="name"]')  # путь до импута почты
login_password_xpath = (By.XPATH, './/label[text()="Пароль"]/..')  # путь до элемента ввода пароля
login_password_input_xpath = (By.XPATH, './/input[@name="Пароль"]')  # путь до импута пароля
login_password_visible_xpath = (By.XPATH, './/div[@class="input__icon input__icon-action"]')  # путь до глазика
login_button_xpath = (By.XPATH, './/button[text()="Войти"]')  # путь до кнопки входа
login_header_xpath = (By.XPATH, './/h2[text()="Вход"]')  # путь до заголовка страницы авторизации
login_register_link_xpath = (By.XPATH, './/a[text()="Зарегистрироваться"]')  # путь до ссылки регистрации
login_forgot_password_link_xpath = (By.XPATH, './/a[text()="Восстановить пароль"]/../a')  # путь до ссылки восстановления пароля
