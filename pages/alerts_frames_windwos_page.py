import time

from locators.alerts_frames_windwos_page_locators import BrowserWindowsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BrowserWindowsPageLocators()

    def check_new_tab_and_window(self):
        buttons = [self.locators.NEW_TAB_BUTTON, self.locators.NEW_WINDOW_BUTTON]
        titles = []

        for button in buttons:
            self.element_is_clickable(button).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            titles.append(self.element_present(self.locators.SAMPLE_TEXT_TITLE).text)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        return titles[0], titles[1]



