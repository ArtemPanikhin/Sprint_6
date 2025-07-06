import pytest
from selenium import webdriver
from curl import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    main_page_url = "https://qa-scooter.praktikum-services.ru/"
    driver.get(main_page_url)
    yield driver
    driver.quit()