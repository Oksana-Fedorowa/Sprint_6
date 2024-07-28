import allure
import pytest
from conftest import driver
from page_objects.main_page import MainPage

class TestLogos:
    @allure.title('Проверка редиректа при нажатии на логотип "Самокат"')
    @allure.description('Проверяем, что при нажатии на логотип "Самокат" в хэдере происходит переход на главную страницу "Самоката"')
    def test_scooter_logo_redirection(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_scooter()
        main_page.click_on_header_logo_scooter()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title('Проверка редиректа при нажатии на логотип "Яндекс"')
    @allure.description('Проверяем, что при нажатии на логотип "Яндекс" в хэдере происходит переход на главную страницу Дзена в новой вкладке')
    def test_yandex_logo_redirection(self, driver):
        main_page = MainPage(driver)
        main_page.wait_visibility_of_header_logo_yandex()
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        assert main_page.get_page_title() == 'Дзен'
