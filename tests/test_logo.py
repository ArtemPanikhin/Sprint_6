from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
import pytest
import allure

class TestLogo:

    @allure.title('Проверка перехода на главную страницу сервиса при клике на лого "Самокат" в шапке')
    def test_logo_main_page(self,main_page):
        main_page.wait_visibility_of_order_button_in_header()
        main_page.click_on_order_button_in_header()
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        main_page.wait_visibility_of_main_header()
        assert main_page.check_displaying_of_main_header()

    @allure.title('Проверка перехода на страницу "Дзен" при клике на лого "Яндекс"')
    def test_logo_dzen(self,main_page):
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        main_page.wait_for_dzen_title()
        assert main_page.dzen_page()