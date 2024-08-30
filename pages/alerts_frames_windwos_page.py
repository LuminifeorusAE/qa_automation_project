import random
import time

import allure

from locators.alerts_frames_windwos_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators, NestedFramesPageLocators, ModalDialogPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step("Check new tab and window")
    def check_new_tab_and_window(self):
        """
        Open new tabs and windows and retrieve the text from each.

        - Clicks on buttons to open new tabs and windows.
        - Switches to the new tab/window, retrieves text, and closes it.
        - Switches back to the original window.

        Returns:
            tuple: A tuple containing text from the new tab and new window.
        """
        buttons = [self.locators.NEW_TAB_BUTTON, self.locators.NEW_WINDOW_BUTTON]
        text = []

        for button in buttons:
            self.element_is_clickable(button).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            text.append(self.element_present(self.locators.SAMPLE_TEXT_TITLE).text)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        return text[0], text[1]


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step("Test click button to alert")
    def click_button_to_alert(self):
        """
        Trigger an alert and retrieve its text.

        - Clicks a button to show an alert.
        - Switches to the alert, retrieves its text, and closes it.

        Returns:
            str: The text of the alert.
        """
        self.element_is_clickable(self.locators.ALERT_CLICK_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_text = alert_window.text
        alert_window.accept()
        return alert_text

    @allure.step("Test click button to alert appearing in 5 seconds")
    def click_button_to_alert_appear_in_5_sec(self):
        """
        Trigger an alert that appears after 5 seconds and retrieve its text.

        - Clicks a button to trigger an alert that appears after a delay.
        - Waits for the alert to appear, retrieves its text, and closes it.

        Returns:
            str: The text of the alert.
        """
        # Click the button that triggers an alert after 5 seconds
        self.element_is_clickable(self.locators.ALERT_AFTER_5_SECS_BUTTON).click()

        # Wait for the alert to be present
        alert_window = self.alert_is_present()

        # Retrieve the alert text and accept it
        alert_text = alert_window.text
        alert_window.accept()

        return alert_text

    @allure.step("Test check confirm alert")
    def check_confirm_alert(self):
        """
        Trigger a confirmation alert and retrieve its result.

        - Clicks a button to show a confirmation alert.
        - Accepts the alert and retrieves the result text.

        Returns:
            str: The result text after accepting the alert.
        """
        self.element_is_clickable(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        confirm_box = self.driver.switch_to.alert
        confirm_box.accept()
        text_result = self.element_present(self.locators.CONFIRM_BOX_ALERT_RESULT).text
        return text_result

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

    @allure.step("Test check frame")
    def check_frame(self, frame_num):
        """
        Check the content of a specific frame and retrieve its attributes.

        - Switches to the specified frame.
        - Retrieves the text and dimensions of the frame.

        Args:
            frame_num (str): The frame to check ('frame1' or 'frame2').

        Returns:
            list: A list containing the frame's text, width, and height.
        """
        if frame_num == 'frame1':
            frame = self.element_present(self.locators.FRAME_1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width, height]

        if frame_num == 'frame2':
            frame = self.element_present(self.locators.FRAME_2)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_present(self.locators.TITLE_FRAME).text
            return [text, width, height]


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

    @allure.step("Test check dialog buttons")
    def check_dialog_buttons(self):
        """
        Check the content of modal dialogs by clicking on their respective buttons.

        - Clicks on buttons to open small and large modals.
        - Captures the text from the modal body for both types.
        - Closes the small modal after capturing its text.

        Returns:
            tuple: A tuple containing the text from the small and large modals.
        """
        buttons = [self.locators.SMALL_MODAL_BUTTON, self.locators.LARGE_MODAL_BUTTON]
        texts = []

        for button in buttons:
            self.element_is_clickable(button).click()

            # Capture the body text of the modal
            modal_body_text = self.element_present(self.locators.MODAL_BODY).text
            texts.append(modal_body_text)

            # If it's the small modal, close it after capturing the text
            if button == self.locators.SMALL_MODAL_BUTTON:
                self.element_is_clickable(self.locators.CLOSE_BUTTON).click()
                self.driver.switch_to.default_content()

        # Log the texts to Allure
        allure.attach(texts[0], "Small Modal Text", allure.attachment_type.TEXT)
        allure.attach(texts[1], "Large Modal Text", allure.attachment_type.TEXT)

        return texts[0], texts[1]
