from selenium.webdriver.common.by import By

"""
Locator definitions for various pages used in Selenium tests.
This file contains classes with locators for elements on different pages.
"""


class TextBoxPageLocators:
    """
    Locators for elements on the TextBox page.
    """

    # Form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Created form outputs
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    """
    Locators for elements on the CheckBox page.
    """

    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    """
    Locators for elements on the RadioButton page.
    """

    YES_BUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="yesRadio"]')
    IMPRESSIVE_BUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="impressiveRadio"]')
    NO_BUTTON = (By.CSS_SELECTOR, 'label[class^="custom-control"][for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "p span[class='text-success']")


class WebTablePageLocators:
    """
    Locators for elements on the WebTable page.
    """

    # Add person form fields
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # Table elements
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, "div[class='rt-tr-group']")
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = (By.XPATH, ".//ancestor::div[@class='rt-tr-group']")
    NO_ROWS_FOUND_TEXT = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # Update button
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')


class ButtonsPageLocators:
    """
    Locators for elements on the Buttons page.
    """

    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_BUTTON = (By.XPATH, "//div[3]/button")

    # Result messages
    DOUBLE_CLICK_BUTTON_SUCCESS = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RIGHT_CLICK_BUTTON_SUCCESS = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    CLICK_BUTTON_SUCCESS = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    """
    Locators for elements on the Links page.
    """

    HOME_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    DYNAMIC_HOME_BUTTON = (By.CSS_SELECTOR, 'a[id="dynamicLink"]')
    CREATED_LINK = (By.CSS_SELECTOR, 'a[id="created"]')
    NO_CONTENT_LINK = (By.CSS_SELECTOR, 'a[id="no-content"]')
    MOVED_LINK = (By.CSS_SELECTOR, 'a[id="moved"]')
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    UNAUTHORIZED_LINK = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    FORBIDDEN_LINK = (By.CSS_SELECTOR, 'a[id="forbidden"]')
    NOT_FOUND_LINK = (By.CSS_SELECTOR, 'a[id="invalid-url"]')


class DownloadAndUploadPageLocators:
    """
    Locators for elements on the Download and Upload page.
    """

    UPLOAD_FILE = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_RESULT = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')
    DOWNLOAD_FILE = (By.CSS_SELECTOR, 'a[id="downloadButton"]')


class DynamicPropertiesPageLocators:
    """
    Locators for elements on the Dynamic Properties page.
    """

    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR, 'button[id="colorChange"]')
    VISIBLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="visibleAfter"]')
    ENABLE_AFTER_FIVE_SEC_BUTTON = (By.CSS_SELECTOR, 'button[id="enableAfter"]')
