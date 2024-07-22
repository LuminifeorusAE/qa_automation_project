from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')
    SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')
    LAST_SECTION = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    LAST_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_INPUT_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')
    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_AND_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    START_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')
