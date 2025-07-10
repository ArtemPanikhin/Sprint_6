import pytest
import allure
from data import TestData
from pages.main_page import MainPage


class TestMainPageFaq:
    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка соответствия ответов в разделе FAQ')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answer)
    def test_faq_answers_correctness(self,main_page, question_number, expected_answer):
        main_page.scroll_to_faq_section()
        main_page.click_faq_question(question_number)
        actual_answer = main_page.get_faq_answer_text(question_number)
        assert actual_answer == expected_answer