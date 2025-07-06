import allure
import pytest

from data import TestData
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Подождать прогрузки поля "Имя"')
    def wait_visibility_field_name(self):
        self.wait_visibility_of_element(OrderPageLocators.name)

    @allure.step('Кликнуть по полю "Имя"')
    def click_field_name(self):
        self.click_on_element(OrderPageLocators.name)

    @allure.step('Заполнить поле "Имя"')
    def data_entry_name(self, test_data):
        self.send_keys_to_input(OrderPageLocators.name, test_data[0])

    @allure.step('Кликнуть по полю "Фамилия"')
    def click_field_lastname(self):
        self.click_on_element(OrderPageLocators.lastname)

    @allure.step('Заполнить поле "Фамилия"')
    def data_entry_lastname(self, test_data):
        self.send_keys_to_input(OrderPageLocators.lastname, test_data[1])

    @allure.step('Кликнуть по полю "Адрес"')
    def click_field_address(self):
        self.click_on_element(OrderPageLocators.address)

    @allure.step('Заполнить поле "Адрес"')
    def data_entry_address(self, test_data):
        self.send_keys_to_input(OrderPageLocators.address, test_data[2])

    @allure.step('Кликнуть по полю "Метро"')
    def click_field_metro(self):
        self.click_on_element(OrderPageLocators.metro)

    @allure.step('Заполнить поле "Метро"')
    def data_entry_metro(self, test_data):
        self.send_keys_to_input(OrderPageLocators.metro, test_data[3])
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)

    @allure.step('Кликнуть по полю "Телефон"')
    def click_field_phone(self):
        self.click_on_element(OrderPageLocators.phone)

    @allure.step('Заполнить поле "Телефон"')
    def data_entry_phone(self, test_data):
        self.send_keys_to_input(OrderPageLocators.phone, test_data[4])

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, test_data):

        self.wait_visibility_field_name()
        self.click_field_name()
        self.data_entry_name(test_data)
        self.click_field_lastname()
        self.data_entry_lastname(test_data)
        self.click_field_address()
        self.data_entry_address(test_data)
        self.click_field_metro()
        self.data_entry_metro(test_data)
        self.click_field_phone()
        self.data_entry_phone(test_data)
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Подождать прогрузки поля "Когда привезти самокат"')
    def wait_visibility_field_date(self):
        self.wait_visibility_of_element(OrderPageLocators.date)

    @allure.step('Кликнуть по полю "Когда привезти самокат"')
    def click_date(self):
        self.click_on_element(OrderPageLocators.date)

    @allure.step('Заполнить поле "Когда привезти самокат"')
    def data_entry_date(self, test_data):
        self.send_keys_to_input(OrderPageLocators.date, test_data[5])

    @allure.step('Кликнуть по чекбоксу "Цвет самоката"')
    def click_checkbox_color_scooter(self):
        self.click_on_element(OrderPageLocators.checkbox_color_scooter)

    @allure.step('Кликнуть по списку "Срок аренды"')
    def click_rental_period(self):
        self.click_on_element(OrderPageLocators.field_rental_period)

    @allure.step('Выбрать из выпадающего списка "Срок аренды"')
    def data_entry_rental_period(self):
        self.click_on_element(OrderPageLocators.dropdown_item_rental_period)

    @allure.step('Кликнуть по полю "Комментарии для курьера"')
    def click_comment(self):
        self.click_on_element(OrderPageLocators.comment)

    @allure.step('Заполнить поле "Комментарии для курьера"')
    def data_entry_comment(self, test_data):
        self.send_keys_to_input(OrderPageLocators.comment, test_data[6])

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, test_data):

        self.wait_visibility_field_date()
        self.click_date()
        self.data_entry_date(test_data)
        self.click_checkbox_color_scooter()
        self.click_rental_period()
        self.data_entry_rental_period()
        self.click_comment()
        self.data_entry_date(test_data)
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)

    @allure.step('Кликнуть по предлагаемому варианту в выпадающем списке станций метро')
    def select_station(self):
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)

    @allure.step('Ввести дату заказа в "Когда привезти самокат"')
    def send_keys_date_by_keyboard_input(self):
        self.send_keys_to_input(OrderPageLocators.date).send_keys(TestData.test_data_user1[5])


    @allure.step('Кликнуть по выбранной дате в выпадающем календаре поля ввода даты начала аренды')
    def click_date_in_calendar(self):
        self.click_on_element(OrderPageLocators.calendar_item)

    @allure.step('Проверить отображение кнопки "Посмотреть статус" после создания заказа')
    def check_displaying_of_button_check_status_of_order(self):
        return self.check_displaying_element(OrderPageLocators.button_check_status_of_order)
