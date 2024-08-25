from selenium.webdriver.common.by import By

register_name_input_xpath = (By.XPATH, './/label[text()="Имя"]/parent::div/input')  # путь до элемента ввода имени
register_email_input_xpath = (By.XPATH, './/label[text()="Email"]/parent::div/input')  # путь до элемента ввода почты
register_password_input_xpath = (By.XPATH, './/label[text()="Пароль"]/parent::div/input')  # путь до элемента ввода пароля
register_button_xpath = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # путь до кнопки регистрации
register_incorrect_password_text_xpath = (By.XPATH, './/label[text()="Пароль"]/parent::div/parent::div/p')  # путь до текста ошибки "Некорректный пароль"
register_password_div_xpath = (By.XPATH, './/label[text()="Пароль"]/parent::div')  # путь до блока ввода пароля
register_login_link_xpath = (By.XPATH, './/a[text()="Войти"]')  # путь до ссылки "Профиль"
