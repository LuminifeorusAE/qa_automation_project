from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators
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

    def add_new_person(self, count=1):
        count = 1
        while count != 0:
            person_info = next(generated_person())
            first_name = person_info.first_name
            last_name = person_info.last_name
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            departament = person_info.departament
            self.visible_element(self.locators.ADD_BUTTON).click()
            self.visible_element(self.locators.FIRST_NAME_INPUT).send_keys(first_name)
            self.visible_element(self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.visible_element(self.locators.EMAIL_INPUT).send_keys(email)
            self.visible_element(self.locators.AGE_INPUT).send_keys(age)
            self.visible_element(self.locators.SALARY_INPUT).send_keys(salary)
            self.visible_element(self.locators.DEPARTMENT_INPUT).send_keys(departament)
            self.visible_element(self.locators.SUBMIT_BUTTON).click()

            count -= 1
            return first_name, last_name, email, age, salary, departament
