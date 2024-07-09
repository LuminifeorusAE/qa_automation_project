# elements_test.py
import time
import random
import pytest
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage


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

    def test_web_table_update_person_info(self, driver):
        web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
        web_table_page.open()
        lastname = web_table_page.add_new_person()[1]
        web_table_page.search_person_by_keyword(lastname)
        age = web_table_page.update_person_info()
        row = web_table_page.check_found_person()
        print(age)
        print(row)
        assert age in row, "The Person card has not been changed"

    def test_web_table_delete_person(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        email = web_table_page.add_new_person()[3]
        time.sleep(3)  # need to delete sleep to test pass without it later
        web_table_page.search_person_by_keyword(email)
        web_table_page.delete_person_info()
        text = web_table_page.check_deleted_person()
        assert text == "No rows found"

    def test_change_row_count(self, driver):
        web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        count = web_table_page.select_row()
        assert count == [5, 10, 20, 25, 100], \
            "Number of rows in the table has not been changed or has changed incorrectly"


class TestButtonPage:
    def test_buttons_clicks(self, driver):
        buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
        buttons_page.open()

        double = buttons_page.button_clicks('double')
        right = buttons_page.button_clicks('right')
        click = buttons_page.button_clicks('dynamic')

        assert double == "You have done a double click" "The double click button has not pressed"
        assert right == "You have done a right click" "The right click button has not pressed"
        assert click == "You have done a dynamic click" "The click button has not pressed"


class TestLinksPage:
    def test_check_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        href_link, current_url = links_page.check_new_tab_simple_link()
        assert href_link == current_url, "The link is broken or url is incorrect"

    def test_created_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_created_link('https://demoqa.com/created')
        assert response_code == 201, "the link work or status code is 201"

    def test_no_content(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_no_content_link('https://demoqa.com/no-content')
        assert response_code == 204, "the link work or status code is 204"

    def test_moved(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_moved_link('https://demoqa.com/moved')
        assert response_code == 301, "the link work or status code is 301"

    def test_forbidden(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_forbidden_link('https://demoqa.com/forbidden')
        assert response_code == 403, "the link work or status code is 403"

    def test_not_found(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_not_found_link('https://demoqa.com/invalid-url')
        assert response_code == 404, "the link work or status code is 404"

    def test_bad_request_link(self, driver):
        links_page = LinksPage(driver, 'https://demoqa.com/links')
        links_page.open()
        response_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
        assert response_code == 400, "the link work or status code is 400"
