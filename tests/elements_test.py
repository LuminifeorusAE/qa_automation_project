# elements_test.py
import time
import random

import allure
from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    DownloadAndUploadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.title('fill the test box')
        def test_fill_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            # driver.execute_script(f"document.body.style.zoom='75%'")
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_curr_add, output_perm_addr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_curr_add, "the current address does not match"
            assert permanent_address == output_perm_addr, "the permanent address does not match"

    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'checkboxes have not been selected'

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.title('Check RadioButton')
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

    @allure.feature('WebTable')
    class TestWebTable:
        @allure.title('Check to add a person to the table')
        def test_web_table_add_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            table_result = web_table_page.check_new_added_person()
            print(new_person)
            print(table_result)
            assert new_person in table_result

        @allure.title('Check human search in table')
        def test_web_table_search_person(self, driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            keyword = web_table_page.add_new_person()[random.randint(0, 5)]
            web_table_page.search_person_by_keyword(keyword)
            table_result = web_table_page.check_found_person()
            print(keyword)
            print(table_result)
            assert keyword in table_result, "Person has not found in the table"

        @allure.title('Checking to update the persons info in the table')
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

        @allure.title('Checking to remove a person from the table')
        def test_web_table_delete_person(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            time.sleep(3)  # need to delete sleep to test pass without it later
            web_table_page.search_person_by_keyword(email)
            web_table_page.delete_person_info()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found"

        @allure.title('Check the change in the number of rows in the table')
        def test_change_row_count(self, driver):
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_row()
            assert count == [5, 10, 20, 25, 100], \
                "Number of rows in the table has not been changed or has changed incorrectly"

    @allure.feature('ButtonPage')
    class TestButtonPage:
        @allure.title('Checking clicks of different types')
        def test_buttons_clicks(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()

            double = buttons_page.button_clicks('double')
            right = buttons_page.button_clicks('right')
            click = buttons_page.button_clicks('dynamic')

            assert double == "You have done a double click" "The double click button has not pressed"
            assert right == "You have done a right click" "The right click button has not pressed"
            assert click == "You have done a dynamic click" "The click button has not pressed"

    @allure.feature('Links page')
    class TestLinksPage:
        @allure.title('Checking the link')
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title('Checking the broken link')
        def test_check_dynamic_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_dynamic_link()
            assert href_link == current_url, "The link is broken or url is incorrect"

        @allure.title('Check the Created Link')
        def test_created_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_created_link('https://demoqa.com/created')
            assert response_code == 201, "the link work or status code is 201"

        @allure.title('Check the No Content')
        def test_no_content(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_no_content_link('https://demoqa.com/no-content')
            assert response_code == 204, "the link work or status code is 204"

        @allure.title('Check Moved link')
        def test_moved(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_moved_link('https://demoqa.com/moved')
            assert response_code == 301, "the link work or status code is 301"

        @allure.title('Check Forbidden link')
        def test_forbidden(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_forbidden_link('https://demoqa.com/forbidden')
            assert response_code == 403, "the link work or status code is 403"

        @allure.title('Check Not Found Link')
        def test_not_found(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_not_found_link('https://demoqa.com/invalid-url')
            assert response_code == 404, "the link work or status code is 404"

        @allure.title('Check Bad Request Link')
        def test_bad_request_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
            assert response_code == 400, "the link work or status code is 400"

    @allure.feature('Upload and Download page')
    class TestDownloadAndUpload:
        @allure.title('Check upload file')
        def test_upload_file(self, driver):
            upload_and_download_page = DownloadAndUploadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            upload_and_download_page.upload_file()
            file_name, result = upload_and_download_page.upload_file()
            assert file_name == result, "The file has not ben uploaded"

        @allure.title('Check download file')
        def test_download_file(self, driver):
            upload_and_download_page = DownloadAndUploadPage(driver, 'https://demoqa.com/upload-download')
            upload_and_download_page.open()
            check = upload_and_download_page.download_file()
            assert check is True, "The file has not been downloaded"

    @allure.feature('Dynamic properties page')
    class TestDynamicProperties:

        @allure.title('Check dynamic properties')
        def test_test_dynamic_properties(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            time.sleep(5)  # fix method to work without time sleep
            color_before, color_after = dynamic_properties_page.check_button_color_change()
            assert color_before != color_after, "color button has not been change"

        @allure.title('Check EnableButton')
        def test_enable_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            enable_button = dynamic_properties_page.check_enable_button()
            assert enable_button is True, "button is not enabled after five seconds"

        @allure.title('Check VisibleButton')
        def test_visible_button(self, driver):
            dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
            dynamic_properties_page.open()
            visible_button = dynamic_properties_page.check_visible_button()
            assert visible_button is True, "enable button is not visible after second"
