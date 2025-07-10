import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Надпись "Для кого самокат"
    title_page_personal = (By.XPATH, "//div[text()='Для кого самокат' and contains(@class, 'Order_Header')]")

    # Поле "Имя"
    name = (By.XPATH, "//input[@placeholder='* Имя']")

    # Поле "Фамилия"
    lastname = (By.XPATH, "//input[@placeholder='* Фамилия']")

    # Поле "Адрес"
    address = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")

    # Поле "Метро"
    metro = (By.XPATH, "//input[@placeholder='* Станция метро']")

    # Выбор станции метро
    select_item_in_dropdown_metro = (By.XPATH, ".//li[@class='select-search__row']")

    # Поле "Телефон"
    phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # Кнопка "Далее"
    button_next = (By.XPATH, "//button[text()='Далее']")

    # Надпись "Про аренду"
    title_page_rent = (By.XPATH, "//div[text()='Про аренду' and contains(@class, 'Order_Header')]")

    # Выбор даты
    date = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    calendar = (By.XPATH, "//div[@class='react-datepicker-popper']")
    calendar_item = (By.XPATH, "//div[contains(@class, 'react-datepicker') and @tabindex='0']")

    # Поле "Срок аренды"
    field_rental_period = (By.XPATH, "//div[text()='* Срок аренды']")
    dropdown_item_rental_period = (By.XPATH, "//div[@class='Dropdown-menu']/div[text()='сутки']")

    # Чекбокс "Цвет самоката"
    checkbox_color_scooter = (By.XPATH, "//label[contains(@class, 'Checkbox_Label')]")

    # Поле "Комментарии для курьера"
    comment = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

    # Кнопка "Заказать"
    button_make_order = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    # Кнопка "Да"
    button_yes_confirm_order = (By.XPATH, "//button[text()='Да']")

    # Кнопка "Нет"
    button_no_confirm_order = (By.XPATH, "//button[text()='Нет']")

    # Кнока "Статус заказа"
    button_check_status_of_order = (By.XPATH, "//button[text()='Посмотреть статус']")

