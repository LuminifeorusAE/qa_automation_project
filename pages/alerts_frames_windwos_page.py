import random
import time

import allure

from locators.alerts_frames_windwos_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def open_new_window_and_capture_text(self, button_locator):
        """
        Opens a new tab or window, captures the text, and switches back to the original window.

        Args:
            button_locator (WebElement): Locator for the button that opens the new tab or window.

        Returns:
            str: Text from the new tab or window.
        """
        self.element_is_clickable(button_locator).click()
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        text = self.element_present(self.locators.SAMPLE_TEXT_TITLE).text
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return text

    @allure.step("Check new tab and window")
    def check_new_tabs_and_windows(self):
        """
        Check the text from a new tab and window.

        Returns:
            tuple: Text from the new tab and new window.
        """
        new_tab_text = self.open_new_window_and_capture_text(self.locators.NEW_TAB_BUTTON)
        new_window_text = self.open_new_window_and_capture_text(self.locators.NEW_WINDOW_BUTTON)
        return new_tab_text, new_window_text


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step("Click button to display alert")
    def click_button_to_alert(self):
        """
        Clicks a button that triggers an alert box.

        This method performs the following actions:
        - Clicks the button identified by the locator `ALERT_CLICK_BUTTON` to display an alert.
        - Handles the alert and returns its text.

        Returns:
            str: The text of the alert that appears.

        Raises:
            WebDriverException: If the element is not clickable or the alert cannot be handled.
        """
        self.element_is_clickable(self.locators.ALERT_CLICK_BUTTON).click()
        return self.handle_alert()

    @allure.step("Click button to display alert after 5 seconds")
    def click_button_to_alert_appear_in_5_sec(self):
        """
        Clicks a button that triggers an alert box to appear after 5 seconds.

        This method performs the following actions:
        - Clicks the button identified by the locator `ALERT_AFTER_5_SECS_BUTTON` to initiate an alert.
        - Waits for the alert to appear, handles it, and returns its text.

        Returns:
            str: The text of the alert that appears after 5 seconds.

        Raises:
            WebDriverException: If the element is not clickable, the alert does not appear, or the alert cannot be handled.
        """
        self.element_is_clickable(self.locators.ALERT_AFTER_5_SECS_BUTTON).click()
        return self.handle_alert()

    @allure.step("Click button to display confirm alert")
    def check_confirm_alert(self):
        """
        Clicks a button that triggers a confirmation alert box.

        This method performs the following actions:
        - Clicks the button identified by the locator `CONFIRM_BOX_ALERT_BUTTON` to display a confirmation alert.
        - Handles the confirmation alert and returns its text.

        Returns:
            str: The text of the confirmation alert that appears.

        Raises:
            WebDriverException: If the element is not clickable, the confirmation alert does not appear, or the alert cannot be handled.
        """
        self.element_is_clickable(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        return self.handle_alert()


    @allure.step("Check prompt box input")
    def check_prompt_box_input(self):
        """
        Trigger a prompt box, input text, and retrieve the result.

        - Clicks a button to show a prompt box.
        - Inputs random text into the prompt box and accepts it.
        - Retrieves the result text.

        Returns:
            tuple: A tuple containing the input text and the result text.
        """
        text = f"David{random.randint(0, 999)}"
        self.element_is_clickable(self.locators.NAME_INPUT_ALERT_BUTTON).click()
        input_box = self.driver.switch_to.alert
        input_box.send_keys(text)
        input_box.accept()
        text_result = self.element_present(self.locators.NAME_INPUT_ALERT_BUTTON_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def switch_to_frame_and_capture(self, frame_locator):
        """
        Switches to a frame, retrieves its text, width, and height, and then switches back.

        Args:
            frame_locator (WebElement): Locator for the frame to switch to.

        Returns:
            list: A list containing the frame's text, width, and height.
        """
        frame = self.element_present(frame_locator)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.element_present(self.locators.TITLE_FRAME).text
        self.driver.switch_to.default_content()
        return [text, width, height]

    @allure.step("Test check frame")
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            return self.switch_to_frame_and_capture(self.locators.FRAME_1)
        elif frame_num == 'frame2':
            return self.switch_to_frame_and_capture(self.locators.FRAME_2)


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step("Test check nested frames")
    def check_nested_frames(self):
        """
        Check the content of nested frames.

        - Switches to the parent frame, retrieves its text.
        - Switches to the child frame, retrieves its text.

        Returns:
            tuple: A tuple containing the text from the parent frame and the child frame.
        """
        parent_frame = self.element_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_frame_text = self.element_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_frame_text = self.element_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_frame_text, child_frame_text


class ModalButtonPage(BasePage):
    locators = ModalDialogPageLocators()

    def open_modal_and_capture_text(self, button_locator):
        """
        Opens a modal, captures the text from the modal body, and closes it if it's a small modal.

        Args:
            button_locator (WebElement): Locator for the modal button to click.

        Returns:
            str: The text from the modal body.
        """
        self.element_is_clickable(button_locator).click()
        modal_body_text = self.element_present(self.locators.MODAL_BODY).text
        if button_locator == self.locators.SMALL_MODAL_BUTTON:
            self.element_is_clickable(self.locators.CLOSE_BUTTON).click()
            self.driver.switch_to.default_content()
        return modal_body_text

    @allure.step("Test check dialog buttons")
    def check_dialog_buttons(self):
        small_modal_text = self.open_modal_and_capture_text(self.locators.SMALL_MODAL_BUTTON)
        large_modal_text = self.open_modal_and_capture_text(self.locators.LARGE_MODAL_BUTTON)

        allure.attach(small_modal_text, "Small Modal Text", allure.attachment_type.TEXT)
        allure.attach(large_modal_text, "Large Modal Text", allure.attachment_type.TEXT)

        return small_modal_text, large_modal_text

