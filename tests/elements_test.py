# elements_test.py

import pytest
from pages.elements_page import TextBoxPage


@pytest.mark.usefixtures("driver")
class TestElements:
    class TestTextBox:
        def test_fill_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_add, output_perm_addr = text_box_page.check_filled_form()

            assert full_name == output_name
            assert email == output_email
            assert current_address == output_curr_add
            assert permanent_address == output_perm_addr
