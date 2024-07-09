import requests
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By

from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators
from pages.base_page import BasePage
import time
import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address.replace('\n', ' ')
        permanent_address = person_info.permanent_address.replace('\n', ' ')

        self.visible_element(self.locators.FULL_NAME).send_keys(full_name)
        self.visible_element(self.locators.EMAIL).send_keys(email)
        self.visible_element(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.visible_element(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        time.sleep(5)
        self.visible_element(self.locators.SUBMIT).click()
        time.sleep(5)
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        full_name = self.element_present(self.locators.CREATED_FULL_NAME).text.split(":")[1].strip()
        email = self.element_present(self.locators.CREATED_EMAIL).text.split(":")[1].strip()

        current_address = self.element_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1].replace('\n',
                                                                                                                 ' ').strip()
        permanent_address = self.element_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1].replace(
            '\n', ' ').strip()

        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage):
    locators = CheckBoxPageLocators

    def open_full_list(self):
        self.visible_element(self.locators.EXPAND_ALL_BUTTON).click()

    def click_random_checkbox(self):
        item_list = self.every_visible_element(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(1, 15)]
            if count > 0:
                self.go_to_element(item)
                item.click()
                count -= 1
                print(item.text)
            else:
                break

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)

        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()


class RadioButtonPage(BasePage):
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice):
        choices = {'yes': self.locators.YES_BUTTON,
                   'impressive': self.locators.IMPRESSIVE_BUTTON,
                   'no': self.locators.NO_BUTTON}

        self.visible_element(choices[choice]).click()

    def get_output_result(self):
        return self.element_present(self.locators.OUTPUT_RESULT).text


class WebTablePage(BasePage):
    locators = WebTablePageLocators()

    def add_new_person(self, ):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.visible_element(self.locators.ADD_BUTTON).click()
            self.visible_element(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.visible_element(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.visible_element(self.locators.EMAIL_INPUT).send_keys(email)
            self.visible_element(self.locators.AGE_INPUT).send_keys(age)
            self.visible_element(self.locators.SALARY_INPUT).send_keys(salary)
            self.visible_element(self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.visible_element(self.locators.SUBMIT_BUTTON).click()

            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def check_new_added_person(self):
        people_list = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_person_by_keyword(self, key_word):
        self.visible_element(self.locators.SEARCH_INPUT).send_keys(key_word)

    def check_found_person(self):
        delete_button = self.element_present(self.locators.DELETE_BUTTON)
        row = delete_button.find_element(*self.locators.ROW_PARENT)
        return row.text.splitlines()

    def update_person_info(self):
        person_info = next(generated_person())
        age = person_info.age
        self.visible_element(self.locators.UPDATE_BUTTON).click()
        self.visible_element(self.locators.AGE_INPUT).clear()
        self.visible_element(self.locators.AGE_INPUT).send_keys(age)
        self.visible_element(self.locators.SUBMIT_BUTTON).click()
        return str(age)

    def delete_person_info(self):
        self.visible_element(self.locators.DELETE_BUTTON).click()

    def check_deleted_person(self):
        return self.element_present(self.locators.NO_ROWS_FOUND_BUTTON).text

    def select_row(self):
        count = [5, 10, 20, 25, 100]
        data = []
        for x in count:
            count_row_button = self.visible_element(self.locators.COUNT_ROW_LIST)
            self.go_to_element(count_row_button)
            count_row_button.click()
            self.visible_element((By.CSS_SELECTOR, f'option[value="{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        list_rows = self.elements_are_present(self.locators.FULL_PEOPLE_LIST)
        return len(list_rows)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def button_clicks(self, type_click):
        if type_click == "double":
            self.action_double_click(self.visible_element(self.locators.DOUBLE_CLICK_BUTTON))
            return self.check_clicked_buttons(self.locators.DOUBLE_CLICK_BUTTON_SUCCESS)

        if type_click == "right":
            self.action_right_click(self.visible_element(self.locators.RIGHT_CLICK_BUTTON))
            return self.check_clicked_buttons(self.locators.RIGHT_CLICK_BUTTON_SUCCESS)

        if type_click == "dynamic":
            self.visible_element(self.locators.CLICK_BUTTON).click()
            return self.check_clicked_buttons(self.locators.CLICK_BUTTON_SUCCESS)

    def check_clicked_buttons(self, locator):
        return self.element_present(locator).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        simple_link = self.visible_element(self.locators.HOME_LINK)
        link_href = (simple_link.get_attribute('href'))
        request = requests.get(f"{link_href}")
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    def check_new_tab_dynamic_link(self):
        dynamic_link = self.visible_element(self.locators.HOME_LINK)
        link_href = (dynamic_link.get_attribute('href'))
        request = requests.get(f"{link_href}")
        if request.status_code == 200:
            dynamic_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    def check_created_link(self, url):
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")
        self.element_present(self.locators.CREATED_LINK).click()

        if request.status_code == 201:
            return request.status_code
        else:
            print(request.status_code)

    def check_no_content_link(self, url):
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")
        self.element_present(self.locators.NO_CONTENT_LINK).click()

        if request.status_code == 204:
            return request.status_code
        else:
            print(request.status_code)

    def check_moved_link(self, url):
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")
        self.element_present(self.locators.MOVED_LINK).click()

        if request.status_code == 301:
            return request.status_code
        else:
            print(request.status_code)

    def check_forbidden_link(self, url):
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")

        forbidden_link = self.element_present(self.locators.FORBIDDEN_LINK)
        self.go_to_element(forbidden_link)
        return request.status_code

    def check_not_found_link(self, url):
        request = requests.get(url)
        print(f"Request URL: {url}, Status Code: {request.status_code}")

        not_found = self.element_present(self.locators.NOT_FOUND_LINK)
        self.go_to_element(not_found)
        return request.status_code

    def check_bad_request_link(self, url):
        request = requests.get(url)
        self.element_present(self.locators.BAD_REQUEST_LINK).click()
        if request.status_code == 200:
            return request.status_code
        else:
            return None

