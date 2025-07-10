from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from locators.main_page_locators import MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Ожидание отображения элемента')
    def wait_visibility_of_element(self, locator, timeout=6):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста')
    def send_keys_to_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Сменить вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверить отображение элемента')
    def check_displaying_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Ждем получения всех элементов')
    def wait_visibility_of_all_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Найти элементы по локатору')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Ожидание элемента по локатору')
    def wait_for_element(self, locator, timeout=10, condition=EC.presence_of_element_located):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator, offset=100):
        element = self.driver.find_element(*locator)
        y = element.location['y'] - offset
        self.driver.execute_script(f"window.scrollTo(0, {y});")
        return element

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проверить соответствие URL')
    def url_contains(self, url_part):
        return url_part in self.get_current_url()