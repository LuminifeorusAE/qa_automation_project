from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    SAMPLE_TEXT_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")


class AlertsPageLocators:
    ALERT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_AFTER_5_SECS_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    NAME_INPUT_CONFIRM_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    NAME_INPUT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    NAME_INPUT_ALERT_BUTTON_RESULT = (By.CSS_SELECTOR, "span[id='promptResult']")

