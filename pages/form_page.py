import os
import time

import allure
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    @allure.step("Fill all forms")
    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.visible_element(self.locators.FIRST_NAME).send_keys(person.first_name)
        self.visible_element(self.locators.LAST_NAME).send_keys(person.last_name)
        self.visible_element(self.locators.EMAIL).send_keys(person.email)
        self.element_is_clickable(self.locators.GENDER).click()  # review
        self.visible_element(self.locators.MOBILE_NUMBER).send_keys(person.mobile_number)
        self.visible_element(self.locators.SUBJECT).send_keys('Maths')
        # write a massive to take every time a different subject instead of only maths subject
        self.visible_element(self.locators.SUBJECT).send_keys(Keys.RETURN)
        self.go_to_element(self.element_present(self.locators.HOBBIES))
        self.element_is_clickable(self.locators.HOBBIES).click()
        self.element_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.visible_element(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.go_to_element(self.element_present(self.locators.SELECT_STATE))
        self.visible_element(self.locators.SELECT_STATE).click()
        self.element_is_clickable(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.visible_element(self.locators.SELECT_CITY).click()
        self.element_is_clickable(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_clickable(self.locators.SUBMIT).click()
        return person

    @allure.step("show form results")
    def form_result(self):
        result_list = self.elements_are_present(self.locators.TABLE_RESULT)
        data = []
        for value in result_list:
            self.go_to_element(value)
            data.append(value.text)
        return data
