import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By

class MainPageLocators:

    # Кнопка "Заказать" в хэдере
    order_button_in_header = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    # Лого "Самокат"
    header_logo_scooter = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')

    # Лого "Яндекс"
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')

    # Кнопка "Заказать" в мейн
    order_button_in_main = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button')

    # Хэдер
    main_header = (By.XPATH, '//div[contains(@class, "Home_Header")]')

    # FAQ
    faq_section = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')

    # Вопросы
    faq_question = (By.XPATH, "//div[@data-accordion-component='AccordionItem']")

    #Ответы
    faq_answer = (By.XPATH, "//div[@data-accordion-component='AccordionItemPanel']")

    #Заголовок Дзен
    title_dzen = (By.TAG_NAME, 'title')