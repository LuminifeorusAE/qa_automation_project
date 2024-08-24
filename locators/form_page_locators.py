import random
from selenium.webdriver.common.by import By


class FormPageLocators:
    """
    This class contains locators for a form page using Selenium's By selectors.
    These locators are used to interact with various elements on the form.
    """

    # Locating the 'First Name' input field by its CSS selector
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')

    # Locating the 'Last Name' input field by its CSS selector
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')

    # Locating the 'Email' input field by its CSS selector
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')

    # Locating one of the 'Gender' radio buttons by a dynamically generated CSS selector
    # Randomly selects one of three gender options by generating a random number between 1 and 3
    GENDER = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1, 3)}"]')

    # Locating the 'Mobile Number' input field by its CSS selector
    MOBILE_NUMBER = (By.CSS_SELECTOR, 'input[id="userNumber"]')

    # Locating the 'Date of Birth' input field by its CSS selector
    DATE_OF_BIRTH = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')

    # Locating the 'Subjects' input field by its CSS selector
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')

    # Locating one of the 'Hobbies' checkboxes by a dynamically generated CSS selector
    # Randomly selects one of three hobby options by generating a random number between 1 and 3
    HOBBIES = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1, 3)}"]')

    # Locating the 'Upload Picture' input field by its CSS selector
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    # Locating the 'Current Address' textarea by its CSS selector
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')

    # Locating the 'State' dropdown by its CSS selector
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')

    # Locating the input field within the 'State' dropdown by its CSS selector
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')

    # Locating the 'City' dropdown by its CSS selector
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')

    # Locating the input field within the 'City' dropdown by its CSS selector
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')

    # Locating the 'Submit' button by its CSS selector
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Locating the result table that appears after form submission by its XPath
    TABLE_RESULT = (By.XPATH, "//div[@class='table-responsive']//td[2] ")
    """
    This locator is used to extract data from the results table after the form has been submitted.
    The table is dynamically generated after submission, and the locator targets the second column of the table.
    """
