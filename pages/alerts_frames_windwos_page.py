import random
import time

from locators.alerts_frames_windwos_page_locators import BrowserWindowsPageLocators, AlertsPageLocators, \
    FramesPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_new_tab_and_window(self):
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

    def click_button_to_alert(self):
        self.element_is_clickable(self.locators.ALERT_CLICK_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def click_button_to_alert_appear_in_5_sec(self):
        self.element_is_clickable(self.locators.ALERT_AFTER_5_SECS_BUTTON).click()
        # !!! remove time sleep to method work without it later !!!
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_confirm_alert(self):
        # !!! write a case when user selects cancel button instead of confirm!!
        self.element_is_clickable(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        confirm_box = self.driver.switch_to.alert
        confirm_box.accept()
        text_result = self.element_present(self.locators.CONFIRM_BOX_ALERT_RESULT).text
        return text_result

    def check_prompt_box_input(self):
        text = f"David{random.randint(0, 999)}"
        self.element_is_clickable(self.locators.NAME_INPUT_ALERT_BUTTON).click()
        input_box = self.driver.switch_to.alert
        input_box.send_keys(text)
        input_box.accept()
        text_result = self.element_present(self.locators.NAME_INPUT_ALERT_BUTTON_RESULT).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    def check_frame(self, frame_num):
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

