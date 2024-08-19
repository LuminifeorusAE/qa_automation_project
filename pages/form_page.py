import os
import allure
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from locators.form_page_locators import FormPageLocators
from pages.base_page import BasePage


class FormPage(BasePage):
    locators = FormPageLocators()

    @allure.step("Fill all forms")
    def fill_form_fields(self):
        """
        Fill out all fields in the form and submit it.

        - Generates a random person and a temporary file.
        - Fills in the form fields with the generated person's details.
        - Handles file upload and removes the temporary file.
        - Selects state and city from dropdowns.
        - Submits the form.

        Returns:
            person: The generated person object used to fill the form.
        """
        person = next(generated_person())
        file_name, path = generated_file()

        # Fill in the first name
        self.visible_element(self.locators.FIRST_NAME).send_keys(person.first_name)

        # Fill in the last name
        self.visible_element(self.locators.LAST_NAME).send_keys(person.last_name)

        # Fill in the email
        self.visible_element(self.locators.EMAIL).send_keys(person.email)

        # Click on the gender radio button
        self.element_is_clickable(self.locators.GENDER).click()  # review

        # Fill in the mobile number
        self.visible_element(self.locators.MOBILE_NUMBER).send_keys(person.mobile_number)

        # Fill in the subject with 'Maths'
        self.visible_element(self.locators.SUBJECT).send_keys('Maths')
        ## Modify this to choose a different subject each time
        self.visible_element(self.locators.SUBJECT).send_keys(Keys.RETURN)

        # Scroll to hobbies section and select hobbies
        self.go_to_element(self.element_present(self.locators.HOBBIES))
        self.element_is_clickable(self.locators.HOBBIES).click()

        # Upload the file and remove it after upload
        self.element_present(self.locators.FILE_INPUT).send_keys(path)
        os.remove(path)

        # Fill in the current address
        self.visible_element(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)

        # Scroll to state dropdown and select a state
        self.go_to_element(self.element_present(self.locators.SELECT_STATE))
        self.visible_element(self.locators.SELECT_STATE).click()
        self.element_is_clickable(self.locators.STATE_INPUT).send_keys(Keys.RETURN)

        # Select a city from the dropdown
        self.visible_element(self.locators.SELECT_CITY).click()
        self.element_is_clickable(self.locators.CITY_INPUT).send_keys(Keys.RETURN)

        # Click on the submit button
        self.element_is_clickable(self.locators.SUBMIT).click()

        return person

    @allure.step("Show form results")
    def form_result(self):
        """
        Retrieve and return the results displayed after form submission.

        - Collects all elements representing the results.
        - Retrieves and returns the text of each result element.

        Returns:
            data: A list of text values from the result elements.
        """
        result_list = self.elements_are_present(self.locators.TABLE_RESULT)
        data = []
        for value in result_list:
            self.go_to_element(value)
            data.append(value.text)
        return data
