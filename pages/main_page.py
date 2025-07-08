from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):  # 5 usages

    @allure.step('Подождать прогрузки кнопки "Заказать" в хэдере')
    def wait_visibility_of_order_button_in_header(self):
        self.wait_visibility_of_element(MainPageLocators.order_button_in_header)

    @allure.step('Кликнуть по кнопке "Заказать" в хэдере')
    def click_on_order_button_in_header(self):
        self.click_on_element(MainPageLocators.order_button_in_header)

    @allure.step('Подождать прогрузки части лого с надписью "Самокат" в хэдере')
    def wait_visibility_of_header_logo_scooter(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_scooter)

    @allure.step('Подождать прогрузки части лого с надписью "Яндекс" в хэдере')
    def wait_visibility_of_header_logo_yandex(self):
        self.wait_visibility_of_element(MainPageLocators.header_logo_yandex)

    @allure.step('Кликнуть по части лого с надписью "Самокат" в хэдере')
    def click_on_header_logo_scooter(self):
        self.click_on_element(MainPageLocators.header_logo_scooter)

    @allure.step('Кликнуть по части лого с надписью "Яндекс" в хэдере')
    def click_on_header_logo_yandex(self):
        self.click_on_element(MainPageLocators.header_logo_yandex)

    @allure.step('Подождать прогрузки отображения заголовка главной страницы')
    def wait_visibility_of_main_header(self):
        self.wait_visibility_of_element(MainPageLocators.main_header)

    @allure.step('Проверить отображение заголовка главной страницы')
    def check_displaying_of_main_header(self):
        return self.check_displaying_element(MainPageLocators.main_header)

    @allure.step('Проскролить до секции "Вопросы о важном"')
    def scroll_to_faq_section(self):
        self.scroll_to_element(MainPageLocators.faq_section)
        self.scroll_to_faq_element()

    @allure.step('Подождать прогрузки нужного номера вопроса в "Вопросы о важном"')
    def wait_visibility_of_faq_items(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_question.items(data))

    @allure.step('Подождать прогрузки нужного номера ответа в "Вопросы о важном"')
    def wait_visibility_of_faq_answer(self, data):
        self.wait_visibility_of_element(MainPageLocators.faq_answer.items(data))

    @allure.step('Кликнуть на вопрос FAQ №{question_number}')
    def click_faq_question(self, question_number):
        questions = self.find_elements(MainPageLocators.faq_question)
        questions[question_number - 1].click()

    @allure.step('Получить текст ответа FAQ №{question_number}')
    def get_faq_answer_text(self, question_number):
         answers = self.find_elements(MainPageLocators.faq_answer)
         return answers[question_number - 1].text

    @allure.step('Ожидание тайтла Дзен')
    def wait_for_dzen_title(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(MainPageLocators.title_dzen))

    @allure.step('Проверка соответствия url')
    def is_dzen_page(self):
        return "dzen.ru" in self.driver.current_url
