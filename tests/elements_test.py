# elements_test.py
import time
import random
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage


@pytest.mark.usefixtures("driver")
class TestElements:
    class TestTextBox:
        def test_fill_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_add, output_perm_addr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_curr_add, "the current address does not match"
            assert permanent_address == output_perm_addr, "the permanent address does not match"

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'


class TestRadioButton:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
        radio_button_page.open()
        radio_button_page.click_on_the_radio_button('yes')
        output_yes = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('impressive')
        output_impressive = radio_button_page.get_output_result()
        radio_button_page.click_on_the_radio_button('no')
        output_no = radio_button_page.get_output_result()
        assert output_yes == 'Yes', "'Yes' button has not been selected"
        assert output_impressive == 'Impressive', "'Impressive' button has not been selected"
        assert output_no == 'No', "'No' button has not been selected"


class TestWebTable:
    def test_web_table_add_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        # web_table_page.add_new_person()
        new_person = web_table_page.add_new_person()
        table_result = web_table_page.check_new_added_person()
        print(new_person)
        print(table_result)
        assert new_person in table_result

    def test_web_table_search_person(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        keyword = web_table_page.add_new_person()[random.randint(0, 5)]
        web_table_page.search_person_by_keyword(keyword)
        table_result = web_table_page.check_found_person()
        print(keyword)
        print(table_result)
        assert keyword in table_result, "Person has not found in the table"

    def test_web_table_update_person_info(self,driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        time.sleep(3)
        web_table_page.search_person_by_keyword(lastname)
        time.sleep(3)
        age = web_table_page.update_person_info()
        time.sleep(3)
        row = web_table_page.check_found_person()
        time.sleep(3)
        print(age)
        print(row)
        assert age in row, "The Person card has not been changed"
