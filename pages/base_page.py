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