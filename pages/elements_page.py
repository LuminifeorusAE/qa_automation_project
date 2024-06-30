from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators
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
