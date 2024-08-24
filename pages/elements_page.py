import base64
import os
import time

import allure
import requests
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from generator.generator import generated_person, generated_file
from locators.elements_page_locators import (
    TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators,
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators,
    DownloadAndUploadPageLocators, DynamicPropertiesPageLocators
)
from pages.base_page import BasePage
import random


class TextBoxPage(BasePage):
    """
    Page Object Model for handling the TextBox page actions.
    """

    locators = TextBoxPageLocators()

    @allure.step("Fill All Fields")
    def fill_all_fields(self):
        """
        Fills all the fields in the text box page with randomly generated data.

        Returns:
            tuple: A tuple containing the full name, email, current address,
                   and permanent address after filling the form.
        """
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace('\n', ' ')
        permanent_address = person_info.permanent_address.replace('\n', ' ')

        with allure.step('Filling fields'):
            self.visible_element(self.locators.FULL_NAME).send_keys(full_name)
            self.visible_element(self.locators.EMAIL).send_keys(email)
            self.visible_element(self.locators.CURRENT_ADDRESS).send_keys(current_address)
            self.visible_element(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
            submit_button = self.visible_element(self.locators.SUBMIT)
            self.go_to_element(submit_button)

            with allure.step('Click submit button'):
                try:
                    submit_button.click()
                except ElementClickInterceptedException:
                    self.driver.execute_script("arguments[0].click();", submit_button)

        return full_name, email, current_address, permanent_address

    @allure.step("Check filled forms")
    def check_filled_form(self):
        """
        Verifies the data entered in the form by extracting the filled data.

        Returns:
            tuple: A tuple of full name, email, current address, and permanent address from the form.
        """
        full_name = self.element_present(self.locators.CREATED_FULL_NAME).text.split(":")[1].strip()
        email = self.element_present(self.locators.CREATED_EMAIL).text.split(":")[1].strip()
        current_address = self.element_present(
            self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1].replace('\n',
                                                                              ' ').strip()
        permanent_address = self.element_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1].replace(
            '\n', ' ').strip()

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    """
    Page Object Model for handling actions on the CheckBox page.
    """

    locators = CheckBoxPageLocators

    @allure.step('Open full list')
    def open_full_list(self):
        """
        Expands the full list of checkboxes by clicking the expand button.
        """
        self.visible_element(self.locators.EXPAND_ALL_BUTTON).click()

    @allure.step('Click random checkbox')
    def click_random_checkbox(self):
        """
        Randomly clicks a checkbox from a list of available checkboxes.
        """
        item_list = self.every_visible_element(self.locators.ITEM_LIST)
        count = 21  # Number of checkboxes to click
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
                print(item.text)
            else:
                break

    @allure.step('Get checked checkboxes')
    def get_checked_checkboxes(self):
        """
        Retrieves and formats the text of all checked checkboxes.

        Returns:
            str: A formatted string of checked checkboxes' titles.
        """
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = [box.find_element(*self.locators.TITLE_ITEM).text for box in checked_list]

        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    @allure.step('Get output result')
    def get_output_result(self):
        """
        Retrieves and formats the result output from the checkboxes.

        Returns:
            str: A formatted string of output results.
        """
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = [item.text for item in result_list]
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    """
    Page Object Model for handling actions on the Radio Button page.
    """

    locators = RadioButtonPageLocators()

    @allure.step('Click on the radio button')
    def click_on_the_radio_button(self, choice):
        """
        Clicks a radio button based on the provided choice.

        Args:
            choice (str): The choice of radio button ('yes', 'impressive', 'no').
        """
        choices = {'yes': self.locators.YES_BUTTON, 'impressive': self.locators.IMPRESSIVE_BUTTON,
                   'no': self.locators.NO_BUTTON}
        self.visible_element(choices[choice]).click()

    @allure.step('Get output result')
    def get_output_result(self):
        """
        Retrieves the output result after a radio button click.

        Returns:
            str: The text of the output result.
        """
        return self.element_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    """
    Page Object Model for handling actions on the Web Table page.
    """

    locators = WebTablePageLocators()

    @allure.step('Add new person')
    def add_new_person(self):
        """
        Adds a new person to the web table by filling the form with random data.

        Returns:
            list: A list containing details of the newly added person.
        """
        person_info = next(generated_person())
        first_name, last_name = person_info.first_name, person_info.last_name
        email, age, salary, department = person_info.email, person_info.age, person_info.salary, person_info.department

        self.visible_element(self.locators.ADD_BUTTON).click()
        self.visible_element(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
        self.visible_element(self.locators.LASTNAME_INPUT).send_keys(last_name)
        self.visible_element(self.locators.EMAIL_INPUT).send_keys(email)
        self.visible_element(self.locators.AGE_INPUT).send_keys(age)
        self.visible_element(self.locators.SALARY_INPUT).send_keys(salary)
        self.visible_element(self.locators.DEPARTMENT_INPUT).send_keys(department)
        self.visible_element(self.locators.SUBMIT_BUTTON).click()

        return [first_name, last_name, str(age), email, str(salary), department]

    @allure.step('Check new added person')
    def check_new_added_person(self):
        """
        Retrieves data of all people listed in the web table.

        Returns:
            list: A list of people, each represented by their details.
        """
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = [item.text.splitlines() for item in people_list]
        return data

    @allure.step('Search person by keyword')
    def search_person_by_keyword(self, key_word):
        """
        Searches for a person in the web table using the provided keyword.

        Args:
            key_word (str): The keyword to search for.
        """
        self.visible_element(self.locators.SEARCH_INPUT).send_keys(key_word)

    @allure.step('Check found person')
    def check_found_person(self):
        """
        Retrieves data of the person found after performing a search.

        Returns:
            list: A list containing the found person's details.
        """
        delete_button = self.element_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    @allure.step('Update person info')
    def update_person_info(self):
        """
        Updates the age of a person in the web table with a randomly generated age.

        Returns:
            str: The updated age.
        """
        person_info = next(generated_person())
        age = person_info.age
        self.visible_element(self.locators.UPDATE_BUTTON).click()
        self.visible_element(self.locators.AGE_INPUT).clear()
        self.visible_element(self.locators.AGE_INPUT).send_keys(age)
        self.visible_element(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    @allure.step('Delete person')
    def delete_person_info(self):
        """
        Deletes a person from the web table by clicking the delete button.
        """
        self.visible_element(self.locators.DELETE_BUTTON).click()

    @allure.step('Check deleted person')
    def check_deleted_person(self):
        """
        Verifies that the person has been deleted from the web table.

        Returns:
            str: The text indicating that no rows were found.
        """
        return self.element_present(self.locators.NO_ROWS_FOUND_TEXT).text

    @allure.step('Select row')
    def select_row(self):
        """
        Selects a row from the web table based on different row count options.

        Returns:
            list: A list of row counts for different options.
        """
        count = [5, 10, 20, 25, 100]
        data = []
        for x in count:
            count_row_button = self.visible_element(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.visible_element((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    @allure.step('Check count rows')
    def check_count_rows(self):
        """
        Checks and returns the number of rows currently present in the web table.

        Returns:
            int: The count of rows in the table.
        """
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    """
    Page Object Model for handling button clicks on the Buttons page.
    """

    locators = ButtonsPageLocators()

    @allure.step('Check button clicks')
    def button_clicks(self, type_click):
        """
        Clicks a button based on the specified click type (double, right, or dynamic).

        Args:
            type_click (str): The type of click to perform (double, right, or dynamic).

        Returns:
            str: The success message for the click action.
        """
        if type_click == "double":
            self.action_double_click(self.visible_element(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_buttons(self.locators.DOUBLE_CLICK_BUTTON_SUCCESS)

        if type_click == "right":
            self.action_right_click(self.visible_element(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_buttons(self.locators.RIGHT_CLICK_BUTTON_SUCCESS)

        if type_click == "dynamic":
            self.visible_element(self.locators.CLICK_BUTTON).click()
            return self.check_clicked_buttons(self.locators.CLICK_BUTTON_SUCCESS)

    @allure.step('Check clicked buttons')
    def check_clicked_buttons(self, locator):
        """
        Checks and retrieves the success message after a button is clicked.

        Args:
            locator: Locator for the success message element.

        Returns:
            str: The success message text.
        """
        return self.element_present(locator).text


class LinksPage(BasePage):
    """
    Page Object Model for handling links and HTTP request actions on the Links page.
    """

    locators = LinksPageLocators()

    @allure.step('Check new tab simple link')
    def check_new_tab_simple_link(self):
        """
        Opens a new tab and navigates to a simple link to verify its URL and status code.

        Returns:
            tuple: A tuple containing the link's href and the current URL or status code.
        """
        simple_link = self.visible_element(self.locators.HOME_LINK)
        link_href = simple_link.get_attribute('href')
        request = requests.get(f"{link_href}")
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    @allure.step('New tab dynamic link')
    def check_new_tab_dynamic_link(self):
        """
        Opens a new tab and navigates to a dynamic link to verify its URL and status code.

        Returns:
            tuple: A tuple containing the link's href and the current URL or status code.
        """
        dynamic_link = self.visible_element(self.locators.HOME_LINK)
        link_href = dynamic_link.get_attribute('href')
        request = requests.get(f"{link_href}")
        if request.status_code == 200:
            dynamic_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    @allure.step('Check created link')
    def check_created_link(self, url):
        """
        Checks the status code of a created link.

        Args:
            url (str): The URL to check.

        Returns:
            int: The HTTP status code of the request.
        """
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")
        self.element_present(self.locators.CREATED_LINK).click()

        if request.status_code == 201:
            return request.status_code
        else:
            print(request.status_code)

    @allure.step('Check no content link')
    def check_no_content_link(self, url):
        """
        Checks the status code of a no-content link.

        Args:
            url (str): The URL to check.

        Returns:
            int: The HTTP status code of the request.
        """
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")
        self.element_present(self.locators.NO_CONTENT_LINK).click()

        if request.status_code == 204:
            return request.status_code
        else:
            print(request.status_code)

    @allure.step('Check moved link')
    def check_moved_link(self, url):
        """
        Checks the status code of a moved link.

        Args:
            url (str): The URL to check.

        Returns:
            int: The HTTP status code of the request.
        """
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")
        self.element_present(self.locators.MOVED_LINK).click()

        if request.status_code == 301:
            return request.status_code
        else:
            print(request.status_code)

    @allure.step('Check forbidden link')
    def check_forbidden_link(self, url):
        """
        Checks the status code of a forbidden link.

        Args:
            url (str): The URL to check.

        Returns:
            int: The HTTP status code of the request.
        """
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")

        forbidden_link = self.element_present(self.locators.FORBIDDEN_LINK)
        self.go_to_element(forbidden_link)
        return request.status_code

    @allure.step('Check random checkbox')
    def check_not_found_link(self, url):
        """
        Checks the status code of a not-found link.

        Args:
            url (str): The URL to check.

        Returns:
            int: The HTTP status code of the request.
        """
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")

        not_found = self.element_present(self.locators.NOT_FOUND_LINK)
        self.go_to_element(not_found)
        return request.status_code

    @allure.step('Check bad request link')
    def check_bad_request_link(self, url):
        """
        Checks the status code of a bad-request link.

        Args:
            url (str): The URL to check.

        Returns:
            int: The HTTP status code of the request.
        """
        response = requests.get(url)
        status_code = response.status_code
        bad_request_button = self.element_is_clickable(self.locators.BAD_REQUEST_LINK)
        self.go_to_element(bad_request_button)
        bad_request_button.click()
        return status_code


class DownloadAndUploadPage(BasePage):
    """
    Page Object Model for handling file downloads and uploads on the Download and Upload page.
    """

    locators = DownloadAndUploadPageLocators()

    @allure.step('Upload file')
    def upload_file(self):
        """
        Uploads a randomly generated file to the page.

        Returns:
            tuple: A tuple containing the file name and the uploaded result.
        """
        file_name, path = generated_file()
        self.element_present(self.locators.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        text = self.element_present(self.locators.UPLOADED_RESULT).text
        return file_name.split("\\")[-1], text.split("\\")[-1]

    @allure.step('Check download file')
    def download_file(self):
        """
        Downloads a file from the page and verifies if it exists.

        Returns:
            bool: True if the file exists and is successfully downloaded, otherwise False.
        """
        link = self.element_present(self.locators.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = rf'C:\Users\David\PycharmProjects\qa_automation_project\filetest{random.randint(0, 999)}.jpeg'
        with open(path_name_file, 'wb+') as file:
            offset = link_b.find(b'\xff\xd8')  # Find the JPEG header
            file.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            file.close()
            os.remove(path_name_file)
        return check_file


class DynamicPropertiesPage(BasePage):
    """
    Page Object Model for handling dynamic properties on the Dynamic Properties page.
    """

    locators = DynamicPropertiesPageLocators()

    @allure.step('Check button color change')
    def check_button_color_change(self):
        """
        Checks if the color of a button changes after 6 seconds.

        Returns:
            tuple: A tuple containing the button's color before and after the change.
        """
        color_button = self.visible_element(self.locators.COLOR_CHANGE_BUTTON)
        color_button_before = color_button.value_of_css_property('color')
        time.sleep(6)
        color_button_after = color_button.value_of_css_property('color')
        return color_button_before, color_button_after

    @allure.step('Check enable button')
    def check_enable_button(self):
        """
        Verifies if the button becomes clickable after 5 seconds.

        Returns:
            bool: True if the button is clickable, otherwise False.
        """
        self.element_is_clickable(self.locators.ENABLE_AFTER_FIVE_SEC_BUTTON)
        return True

    @allure.step('Check visible button')
    def check_visible_button(self):
        """
        Verifies if the button becomes visible after 5 seconds.

        Returns:
            bool: True if the button is visible, otherwise False.
        """
        self.visible_element(self.locators.VISIBLE_AFTER_FIVE_SEC_BUTTON)
        return True
