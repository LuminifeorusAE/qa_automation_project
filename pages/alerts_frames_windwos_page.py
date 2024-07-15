import time

from locators.alerts_frames_windwos_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_new_tab_and_window(self):
        # Check new tab
        self.element_is_clickable(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title_tab = self.element_present(self.locators.SAMPLE_TEXT_TITLE).text
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        self.element_is_clickable(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title_window = self.element_present(self.locators.SAMPLE_TEXT_TITLE).text
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

        return text_title_tab, text_title_window


