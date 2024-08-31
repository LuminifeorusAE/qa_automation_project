from selenium.webdriver.common.by import By


class BrowserWindowsPageLocators:
    """
    Locators for the Browser Windows page.

    Attributes:
        NEW_TAB_BUTTON: Locator for the button that opens a new tab.
        SAMPLE_TEXT_TITLE: Locator for the heading inside the newly opened tab.
        NEW_WINDOW_BUTTON: Locator for the button that opens a new browser window.
    """
    NEW_TAB_BUTTON = (By.CSS_SELECTOR, "button[id='tabButton']")
    SAMPLE_TEXT_TITLE = (By.CSS_SELECTOR, "h1[id='sampleHeading']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, "button[id='windowButton']")


class AlertsPageLocators:
    """
    Locators for the Alerts page.

    Attributes:
        ALERT_CLICK_BUTTON: Locator for the button that triggers a simple alert.
        ALERT_AFTER_5_SECS_BUTTON: Locator for the button that triggers an alert after 5 seconds.
        CONFIRM_BOX_ALERT_BUTTON: Locator for the button that triggers a confirmation box alert.
        CONFIRM_BOX_ALERT_RESULT: Locator for the result text of the confirmation box alert.
        NAME_INPUT_ALERT_BUTTON: Locator for the button that triggers an alert with a name input prompt.
        NAME_INPUT_ALERT_BUTTON_RESULT: Locator for the result text of the name input prompt alert.
    """
    ALERT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='alertButton']")
    ALERT_AFTER_5_SECS_BUTTON = (By.CSS_SELECTOR, "button[id='timerAlertButton']")
    CONFIRM_BOX_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='confirmButton']")
    CONFIRM_BOX_ALERT_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")
    NAME_INPUT_ALERT_BUTTON = (By.CSS_SELECTOR, "button[id='promtButton']")
    NAME_INPUT_ALERT_BUTTON_RESULT = (By.CSS_SELECTOR, "span[id='confirmResult']")


class FramesPageLocators:
    """
    Locators for the Frames page.

    Attributes:
        FRAME_1: Locator for the first iframe on the page.
        FRAME_2: Locator for the second iframe on the page.
        TITLE_FRAME: Locator for the heading inside the iframe.
    """
    FRAME_1 = (By.CSS_SELECTOR, "iframe[id='frame1']")
    FRAME_2 = (By.CSS_SELECTOR, "iframe[id='frame2']")
    TITLE_FRAME = (By.CSS_SELECTOR, "h1[id='sampleHeading']")


class NestedFramesPageLocators:
    """
    Locators for the Nested Frames page.

    Attributes:
        PARENT_FRAME: Locator for the parent iframe on the page.
        PARENT_FRAME_TEXT: Locator for the text inside the parent iframe.
        CHILD_FRAME: Locator for the child iframe inside the parent iframe.
        CHILD_FRAME_TEXT: Locator for the text inside the child iframe.
    """
    PARENT_FRAME = (By.CSS_SELECTOR, "iframe[id='frame1']")
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR, "body")
    CHILD_FRAME = (By.CSS_SELECTOR, "iframe[srcdoc='<p>Child Iframe</p>']")
    CHILD_FRAME_TEXT = (By.CSS_SELECTOR, 'p')


class ModalDialogPageLocators:
    """
    Locators for the Modal Dialogs page.

    Attributes:
        TITLE_SMALL_MODAL: Locator for the title of the small modal dialog.
        SMALL_MODAL_BUTTON: Locator for the button that opens the small modal dialog.
        CLOSE_BUTTON: Locator for the button that closes the small modal dialog.
        MODAL_BODY: Locator for the body content of the modal dialog.
        LARGE_MODAL_BUTTON: Locator for the button that opens the large modal dialog.
        TITLE_LARGE_MODAL: Locator for the title of the large modal dialog.
    """
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, "div[class = 'example-modal-sizes-title-sm']")
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showSmallModal']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "button[id='closeSmallModal']")

    MODAL_BODY = (By.CSS_SELECTOR, "div[class='modal-body']")
    LARGE_MODAL_BUTTON = (By.CSS_SELECTOR, "button[id='showLargeModal']")
    TITLE_LARGE_MODAL = (By.CSS_SELECTOR, "div[class = 'example-modal-sizes-title-sm']")
