from selenium.webdriver.common.by import By


class AccordianPageLocators:
    """Locators for the Accordian page elements."""

    # First section heading
    FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Heading"]')

    # First section content paragraph
    FIRST_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    # Second section heading
    SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Heading"]')

    # Second section content paragraph
    SECOND_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    # Last (third) section heading
    LAST_SECTION = (By.CSS_SELECTOR, 'div[id="section3Heading"]')

    # Last (third) section content paragraph
    LAST_SECTION_CONTENT = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    """Locators for the AutoComplete page elements."""

    # Input field for multiple autocomplete selections
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')

    # Container for each selected multiple value
    MULTI_INPUT_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')

    # SVG path to remove selected multiple values
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')

    # Single selection container
    SINGLE_CONTAINER = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')

    # Input field for single autocomplete selection
    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')


class DatePickerPageLocators:
    """Locators for the DatePicker page elements."""

    # Input field for the date picker
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')

    # Dropdown for selecting month
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')

    # Dropdown for selecting year
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')

    # List of selectable days in the date picker
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    # Input field for both date and time picker
    DATE_AND_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')

    # Month selection dropdown in the date and time picker
    DATE_AND_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')

    # Year selection dropdown in the date and time picker
    DATE_AND_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')

    # List of selectable times in the date and time picker
    DATE_AND_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR, 'li[class="react-datepicker__time-list-item "]')

    # List of selectable months in the date and time picker
    DATE_AND_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')

    # List of selectable years in the date and time picker
    DATE_AND_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    """Locators for the Slider page elements."""

    # Input slider for selecting a value
    INPUT_SLIDER = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')

    # Input field showing the slider's current value
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    """Locators for the ProgressBar page elements."""

    # Button to start or stop the progress bar
    START_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')

    # Element showing the current progress of the progress bar
    PROGRESS_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')


class TabsPageLocators:
    """Locators for the Tabs page elements."""

    # 'What' tab
    WHAT_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-what"]')

    # Content of the 'What' tab
    WHAT_TAB_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-what"]')

    # 'Origin' tab
    ORIGIN_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-origin"]')

    # Content of the 'Origin' tab
    ORIGIN_TAB_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-origin"]')

    # 'Use' tab
    USE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-use"]')

    # Content of the 'Use' tab
    USE_TAB_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-use"]')

    # 'More' tab
    MORE_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-more"]')

    # Content of the 'More' tab
    MORE_TAB_CONTENT = (By.CSS_SELECTOR, 'div[id="demo-tabpane-more"]')


class ToolTipsPageLocators:
    """Locators for the ToolTips page elements."""

    # Button that shows tooltip on hover
    HOVER_ME_TO_SEE_BUTTON = (By.CSS_SELECTOR, 'button[id="toolTipButton"]')

    # Tooltip that appears when hovering over the button
    TOOL_TIP_BUTTON = (By.CSS_SELECTOR, 'button[aria-describedby="buttonToolTip"]')

    # Input field that shows tooltip on hover
    INPUT_HOVER_ME_TO_SEE = (By.CSS_SELECTOR, 'input[id="toolTipTextField"]')

    # Tooltip that appears when hovering over the input field
    TOOL_TIP_INPUT = (By.CSS_SELECTOR, 'input[aria-describedby="textFieldToolTip"]')

    # XPath for the 'Contrary' link that shows tooltip on hover
    CONTRARY_XPATH = (By.XPATH, '//*[.="Contrary"]')

    # Tooltip for the 'Contrary' link
    TOOL_TIP_CONTRARY = (By.CSS_SELECTOR, 'a[aria-describedby="contraryTexToolTip"]')

    # XPath for the '1.10.32' section that shows tooltip on hover
    SECTION_XPATH = (By.XPATH, '//*[.="1.10.32"]')

    # Tooltip for the '1.10.32' section
    TOOL_TIP_SECTION = (By.CSS_SELECTOR, 'a[aria-describedby="sectionToolTip"]')

    # All tooltip inner elements
    TOOL_TIPS_INNERS = (By.CSS_SELECTOR, 'div[class="tooltip-inner"]')


class MenuItemPageLocators:
    """Locators for the MenuItem page elements."""

    # List of main menu items
    MAIN_ITEM_LIST = (By.CSS_SELECTOR, "ul[id='nav'] li a")


class SelectMenuPageLocators:
    """Locators for the SelectMenu page elements."""

    # Dropdown to select a value
    SELECT_VALUE_DROP = (By.CSS_SELECTOR, "div[id='withOptGroup']")

    # Input field for selecting a value in the dropdown
    SELECT_VALUE_DROP_OPTION = (By.CSS_SELECTOR, "input[id='react-select-2-input']")

    # Dropdown to select one option
    SELECT_ONE_DROP = (By.CSS_SELECTOR, "div[id='selectOne']")

    # Input field for selecting one option in the dropdown
    SELECT_ONE_DROP_OPTION = (By.CSS_SELECTOR, "input[id='react-select-3-input']")

    # Dropdown for selecting in the old style
    SELECT_OLD_STYLE_DROP = (By.CSS_SELECTOR, "select[id='oldSelectMenu']")

    # Dropdown for multiselect with placeholder 'Select...'
    MULTISELECT_DROP = (By.XPATH, '//*[.="Select..."]')

    # Input field for multiselect dropdown
    MULTISELECT_DROP_OPTION = (By.CSS_SELECTOR, "input[id='react-select-4-input']")

    # Standard multi-select dropdown for selecting cars
    STANDARD_MULTI_SELECT = (By.CSS_SELECTOR, "select[id='cars']")
