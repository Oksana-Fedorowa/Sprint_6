import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from page_objects.main_page import MainPage

@pytest.fixture()
def driver():
    firefox_options = Options()
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)