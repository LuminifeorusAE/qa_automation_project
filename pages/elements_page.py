from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
import time


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
        current_address = self.element_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(":")[1].replace('\n', ' ').strip()
        permanent_address = self.element_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(":")[1].replace('\n', ' ').strip()

        return full_name, email, current_address, permanent_address
