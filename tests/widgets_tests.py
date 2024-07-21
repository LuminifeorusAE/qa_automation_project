import time

from pages.widgets_test_page import AccordianPage
from pages.widgets_test_page import AutoCompletePage


class TestWidgets:
    class TestAccordianPage:

        def test_accordian_widgets(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content_length = accordian_page.check_accordian('first')
            assert first_title == "What is Lorem Ipsum?" and first_content_length > 0, 'Incorrect title or missing text'
            second_title, second_content_length = accordian_page.check_accordian('second')
            assert second_title == "Where does it come from?" and second_content_length > 0, \
                'Incorrect title or missing text'
            last_title, last_content_length = accordian_page.check_accordian('last')
            assert last_title == "Why do we use it?" and last_content_length > 0, 'Incorrect title or missing text'


class TestAutoCompletePage:

    def test_auto_complete(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        colors = auto_complete_page.fill_multi_input()
        colors_result = auto_complete_page.check_color_in_multi()
        assert colors == colors_result, "added colors are missing in the input"

    def test_remove_value_from_multi(self, driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        auto_complete_page.fill_multi_input()
        count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()
        assert count_value_before != count_value_after, "value was not deleted"

    def test_fill_single_autocomplete(self,driver):
        auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
        auto_complete_page.open()
        color = auto_complete_page.fill_single_input()
        color_result = auto_complete_page.check_color_in_single()
        assert color == color_result, "added colors are missing in the input"



