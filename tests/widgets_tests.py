from pages.widgets_test_page import AccordianPage


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
