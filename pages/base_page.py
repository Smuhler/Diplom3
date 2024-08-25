import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверяем на какой странице находимся')
    def check_current_url(self):
        return self.driver.current_url

    @allure.step('Кликаем на элемент по локатору {locator}')
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получаем текст элемента по локатору {locator}')
    def get_text_from_visible_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step('Заполняем поле {locator} текстом {text}')
    def input_text(self, locator, text):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator)).send_keys(text)

    @allure.step('Проверяем отображение элемента на экране')
    def is_visible_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Проверяем что на элемент можно нажать')
    def is_clickable_element(self, locator):
        return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Получаем атрибут элемента')
    def get_attribute_of_element(self, locator, attribute):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute)

    @allure.step('Находим все элементы по локатору')
    def get_list_of_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Находим элемент по локатору')
    def get_element(self, locator):
        return self.driver.find_element(*locator)
