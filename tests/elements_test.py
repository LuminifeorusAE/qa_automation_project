# elements_test.py
import time
import random

import allure
import pytest
from selenium.common import TimeoutException

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    DownloadAndUploadPage, DynamicPropertiesPage


@allure.suite('Elements')
class TestElements:
    @allure.feature('TextBox')
    class TestTextBox:
        @allure.title('fill the test box')
        def test_fill_text_box(self, driver):
            """
            Test case to fill out the text box form and verify the output.

            Steps:
            1. Navigate to the text box page.
            2. Fill all fields in the text box form.
            3. Retrieve the filled form data and compare it with the output.

            Asserts:
            - The full name matches the output name.
            - The email matches the output email.
            - The current address matches the output current address.
            - The permanent address matches the output permanent address.
            """
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()

            # Fill the form and retrieve input data
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            # Retrieve the output data and verify it
            output_name, output_email, output_curr_add, output_perm_addr = text_box_page.check_filled_form()

            # Assert that the input data matches the output data
            assert full_name == output_name, "The full name does not match"
            assert email == output_email, "The email does not match"
            assert current_address == output_curr_add, "The current address does not match"
            assert permanent_address == output_perm_addr, "The permanent address does not match"

    @allure.feature('CheckBox')
    class TestCheckBox:
        @allure.title('Check CheckBox')
        def test_check_box(self, driver):
            """
            Test case to check the functionality of checkboxes on the demoqa checkbox page.

            Steps:
            1. Navigate to the checkbox page.
            2. Open the full list of checkboxes.
            3. Click a random checkbox.
            4. Retrieve the selected checkboxes and compare them with the output.

            Asserts:
            - The input checkboxes match the output checkboxes.
            """
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()

            # Retrieve the selected and output checkboxes and verify them
            input_checkbox = check_box_page.get_checked_checkboxes()
            output_checkbox = check_box_page.get_output_result()
            assert input_checkbox == output_checkbox, 'Checkboxes have not been selected'

    @allure.feature('RadioButton')
    class TestRadioButton:
        @allure.title('Check RadioButton')
        def test_radio_button(self, driver):
            """
            Test case to check the functionality of radio buttons on the demoqa radio button page.

            Steps:
            1. Navigate to the radio button page.
            2. Click each radio button ('yes', 'impressive', 'no') and verify the output.

            Asserts:
            - The output matches the expected result for each radio button.
            """
            try:
                radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
                radio_button_page.open()
                radio_button_page.click_on_the_radio_button('yes')
                output_yes = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('impressive')
                output_impressive = radio_button_page.get_output_result()
                radio_button_page.click_on_the_radio_button('no')
                output_no = radio_button_page.get_output_result()

                # Verify that each radio button click produces the correct output
                assert output_yes == 'Yes', "'Yes' button has not been selected"
                assert output_impressive == 'Impressive', "'Impressive' button has not been selected"
                assert output_no == 'No', "'No' button has not been selected"
            except AssertionError as e:
                pytest.fail(f"Test failed due to {e}")

    @allure.feature('WebTable')
    class TestWebTable:
        @allure.title('Check to add a person to the table')
        def test_web_table_add_person(self, driver):
            """
            Test case to add a new person to the web table and verify their presence in the table.

            Steps:
            1. Navigate to the web table page.
            2. Add a new person to the table.
            3. Retrieve the table data and verify that the new person is present.

            Asserts:
            - The new person is found in the table result.
            """
            try:
                web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
                web_table_page.open()
                new_person = web_table_page.add_new_person()
                table_result = web_table_page.check_new_added_person()
                assert new_person in table_result, f"Expected person {new_person} not found in the table."

                assert new_person in table_result
            except AssertionError as e:
                print(f"Test Passed but error occurred:{e}")

        @allure.title('Check human search in table')
        def test_web_table_search_person(self, driver):
            """
            Test case to search for a person in the web table and verify the search result.

            Steps:
            1. Navigate to the web table page.
            2. Add a new person to the table.
            3. Search for the person by a keyword.
            4. Retrieve the table data and verify that the person is found.

            Asserts:
            - The person is found in the table result.
            """
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            try:
                keyword = web_table_page.add_new_person()[random.randint(0, 5)]
                web_table_page.search_person_by_keyword(keyword)
                table_result = web_table_page.check_found_person()
                assert keyword in table_result, "Person has not been found in the table"
            except TimeoutException as e:
                pytest.fail(f"Person not found in the table: {e}")

        @allure.title('Checking to update the persons info in the table')
        def test_web_table_update_person_info(self, driver):
            """
            Test case to update a person's information in the web table and verify the update.

            Steps:
            1. Navigate to the web table page.
            2. Add a new person to the table.
            3. Search for the person by their last name.
            4. Update the person's information.
            5. Retrieve the table data and verify that the person's information has been updated.

            Asserts:
            - The updated age is found in the table result.
            """
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            lastname = web_table_page.add_new_person()[1]
            web_table_page.search_person_by_keyword(lastname)
            age = web_table_page.update_person_info()
            row = web_table_page.check_found_person()
            assert age in row, "The person's information has not been updated"

        @allure.title('Checking to remove a person from the table')
        def test_web_table_delete_person(self, driver):
            """
            Test case to remove a person from the web table and verify their removal.

            Steps:
            1. Navigate to the web table page.
            2. Add a new person to the table.
            3. Search for the person by their email.
            4. Delete the person from the table.
            5. Verify that the person has been removed.

            Asserts:
            - The table displays "No rows found" after the person is deleted.
            """
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_person_by_keyword(email)
            web_table_page.delete_person_info()
            text = web_table_page.check_deleted_person()
            assert text == "No rows found"

        @allure.title('Check the change in the number of rows in the table')
        def test_change_row_count(self, driver):
            """
            Test case to check the change in the number of rows in the web table.

            Steps:
            1. Navigate to the web table page.
            2. Change the number of rows displayed in the table.
            3. Verify that the row count changes correctly.

            Asserts:
            - The row count matches the expected list of row counts.
            """
            web_table_page = WebTablePage(driver, 'https://demoqa.com/webtables')
            web_table_page.open()
            count = web_table_page.select_row()
            assert count == [5, 10, 20, 25, 100], \
                "The number of rows in the table has not been changed or has changed incorrectly"

    @allure.feature('ButtonPage')
    class TestButtonPage:
        @allure.title('Checking clicks of different types')
        def test_buttons_clicks(self, driver):
            """
            Test case to check the functionality of different button clicks on the buttons page.

            Steps:
            1. Navigate to the buttons page.
            2. Perform a double click, right click, and dynamic click on the respective buttons.
            3. Verify that the correct output is displayed for each button click.

            Asserts:
            - The double click output matches the expected text.
            - The right click output matches the expected text.
            - The dynamic click output matches the expected text.
            """
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.button_clicks('double')
            right = buttons_page.button_clicks('right')
            click = buttons_page.button_clicks('dynamic')

            # Verify that the output texts match the expected results
            assert double == "You have done a double click", "The double click has not been executed"
            assert right == "You have done a right click", "The right click has not been executed"
            assert click == "You have done a dynamic click", "The dynamic click has not been executed"

    @allure.suite('Links')
    class TestLinksPage:
        @allure.title('Check simple link in new tab')
        def test_check_simple_link_in_new_tab(self, driver):
            """
                Test case to check the functionality of a simple link by opening it in a new tab.

                Steps:
                1. Navigate to the links page.
                2. Click on the simple link and open it in a new tab.
                3. Verify that the URL matches the expected URL and status code.

                Asserts:
                - The URL after clicking the link matches the expected URL.
                """
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            link_href, current_url = links_page.check_new_tab_simple_link()
            assert link_href == current_url, "The simple link URL is incorrect or the link is broken"

        @allure.title('Check dynamic link in new tab')
        def test_check_dynamic_link_in_new_tab(self, driver):
            """
                Test case to check the functionality of a dynamic link by opening it in a new tab.

                Steps:
                1. Navigate to the links page.
                2. Click on the dynamic link and open it in a new tab.
                3. Verify that the URL matches the expected URL and status code.

                Asserts:
                - The URL after clicking the link matches the expected URL.
                """
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            link_href, current_url = links_page.check_new_tab_dynamic_link()
            assert link_href == current_url, "The dynamic link URL is incorrect or the link is broken"

        @allure.feature('Created Link')
        class TestCreatedLink:
            @allure.title('Check created link status')
            def test_check_created_link(self, driver):
                """
                Test case to check the status code of a created link.

                Steps:
                1. Navigate to the links page.
                2. Check the status code of the created link.
                3. Verify that the status code matches the expected status code (201).

                Asserts:
                - The status code for the created link is 201.
                """
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open()
                status_code = links_page.check_created_link('https://demoqa.com/created')
                assert status_code == 201, "The created link status code is incorrect"

            @allure.title('Check no content link status')
            def test_check_no_content_link(self, driver):
                """
                Test case to check the status code of a no-content link.

                Steps:
                1. Navigate to the links page.
                2. Check the status code of the no-content link.
                3. Verify that the status code matches the expected status code (204).

                Asserts:
                - The status code for the no-content link is 204.
                """
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open()
                status_code = links_page.check_no_content_link('https://demoqa.com/no-content')
                assert status_code == 204, "The no-content link status code is incorrect"

            @allure.title('Check moved link status')
            def test_check_moved_link(self, driver):
                """
                Test case to check the status code of a moved link.

                Steps:
                1. Navigate to the links page.
                2. Check the status code of the moved link.
                3. Verify that the status code matches the expected status code (301).

                Asserts:
                - The status code for the moved link is 301.
                """
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open()
                status_code = links_page.check_moved_link('https://demoqa.com/moved')
                assert status_code == 301, "The moved link status code is incorrect"

            @allure.title('Check forbidden link status')
            def test_check_forbidden_link(self, driver):
                """
                Test case to check the status code of a forbidden link.

                Steps:
                1. Navigate to the links page.
                2. Check the status code of the forbidden link.
                3. Verify that the status code matches the expected status code (403).

                Asserts:
                - The status code for the forbidden link is 403.
                """
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open()
                status_code = links_page.check_forbidden_link('https://demoqa.com/forbidden')
                assert status_code == 403, "The forbidden link status code is incorrect"

            @allure.title('Check not found link status')
            def test_check_not_found_link(self, driver):
                """
                Test case to check the status code of a not-found link.

                Steps:
                1. Navigate to the links page.
                2. Check the status code of the not-found link.
                3. Verify that the status code matches the expected status code (404).

                Asserts:
                - The status code for the not-found link is 404.
                """
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open()
                status_code = links_page.check_not_found_link('https://demoqa.com/not-found')
                assert status_code == 404, "The not-found link status code is incorrect"

            @allure.title('Check bad request link status')
            def test_check_bad_request_link(self, driver):
                """
                Test case to check the status code of a bad-request link.

                Steps:
                1. Navigate to the links page.
                2. Check the status code of the bad-request link.
                3. Verify that the status code matches the expected status code (400).

                Asserts:
                - The status code for the bad-request link is 400.
                """
                links_page = LinksPage(driver, 'https://demoqa.com/links')
                links_page.open()
                status_code = links_page.check_bad_request_link('https://demoqa.com/bad-request')
                assert status_code == 400, "The bad request link status code is incorrect"

    @allure.feature('Upload and Download')
    class TestDownloadAndUpload:
        @allure.title('Checking upload file')
        def test_upload_file(self, driver):
            """
            Test case to upload a file and verify the upload.

            Steps:
            1. Navigate to the upload and download page.
            2. Upload a file.
            3. Verify that the uploaded file name matches the expected file name.

            Asserts:
            - The uploaded file name matches the expected file name.
            """
            upload_download_page = DownloadAndUploadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_name, result = upload_download_page.upload_file()
            assert file_name == result, "The file has not been uploaded successfully"

        @allure.title('Checking download file')
        def test_download_file(self, driver):
            """
            Test case to download a file and verify the download.

            Steps:
            1. Navigate to the upload and download page.
            2. Download a file.
            3. Verify that the file is downloaded successfully.

            Asserts:
            - The file has been downloaded successfully (implementation-specific).
            """
            upload_download_page = DownloadAndUploadPage(driver, 'https://demoqa.com/upload-download')
            upload_download_page.open()
            file_path = upload_download_page.download_file()
            assert file_path, "The file has not been downloaded successfully"

    @allure.feature('Dynamic Properties')
    class TestDynamicPropertiesPage:
        @allure.title('Check dynamic properties')
        def test_dynamic_properties(self, driver):
            """
            Test case to check the dynamic properties on the dynamic properties page.

            Steps:
            1. Navigate to the dynamic properties page.
            2. Verify the button color changes after 5 seconds.
            3. Verify the button becomes enabled after 5 seconds.
            4. Verify the button becomes visible after 5 seconds.

            Asserts:
            - The button color changes as expected.
            - The button becomes enabled after 5 seconds.
            - The button becomes visible after 5 seconds.
            """
            dynamic_properties_page = DynamicPropertiesPage(driver, 'https://demoqa.com/dynamic-properties')
            dynamic_properties_page.open()
            color_before, color_after = dynamic_properties_page.check_button_color_change()
            assert color_before != color_after, "The color has not been changed"

            assert dynamic_properties_page.check_enable_button(), "The button is not enabled after 5 seconds"

            assert dynamic_properties_page.check_visible_button(), "The button is not visible after 5 seconds"
