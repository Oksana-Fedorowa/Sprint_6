import allure
from data import TestData
from page_objects.main_page import MainPage
import pytest
from conftest import driver


class TestMainPageFAQ:

    @allure.title('Проверка ответа на вопрос {question_number}')
    @allure.description('Проверка появления текста при нажатии на стрелочку для вопроса {question_number}')
    @pytest.mark.parametrize("question_number, expected_answer", TestData.test_data_expected_answer_faq)
    def test_faq_answer(self, main_page, question_number, expected_answer):
        main_page.scroll_to_faq_section()
        main_page.wait_visibility_of_faq_items(question_number)
        main_page.click_on_faq_items(question_number)
        main_page.wait_visibility_of_faq_answer(question_number)
        assert main_page.get_displayed_text_from_faq_answer(question_number) == expected_answer