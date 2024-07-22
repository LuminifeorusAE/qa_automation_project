import time

from pages.widgets_test_page import AccordianPage, DatePickerPage, SliderPage, ProgressBarPage
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


class TestDatePickerPage:
    def test_change_data(self, driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        value_date_before, valuer_date_after = date_picker_page.select_date()
        assert value_date_before != valuer_date_after, "Date and time has not been changed"

    def test_change_date_and_time(self, driver):
        date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
        date_picker_page.open()
        value_date_before, value_date_after = date_picker_page.select_date_and_time()
        print(value_date_before)
        print(value_date_after)
        assert value_date_before != value_date_after,  'the date and time have not been changed'


class TestSliderPage:

    def test_slider(self, driver):
        slider_page = SliderPage(driver, "https://demoqa.com/slider")
        slider_page.open()
        value_before, value_after = slider_page.change_slider_value()
        assert value_before != value_after, "slider value has not been changed"


class TestProgressBarPage:

    def test_progress_bar(self, driver):
        progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
        progress_bar_page.open()
        value_before, value_after = progress_bar_page.change_progress_bar_value()
        assert value_before != value_after , "progress bar value has not been changed"



