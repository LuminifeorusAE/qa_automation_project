import time

from selenium.common import TimeoutException

from locators.widgeds_locators import AccordianPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {
            'first': {
                'title': self.locators.FIRST_SECTION,
                'content': self.locators.FIRST_SECTION_CONTENT
            },
            'second': {
                'title': self.locators.SECOND_SECTION,
                'content': self.locators.SECOND_SECTION_CONTENT
            },
            'last': {
                'title': self.locators.LAST_SECTION,
                'content': self.locators.LAST_SECTION_CONTENT
            }
        }

        section_title = self.element_is_clickable(accordian[accordian_num]['title'])
        self.go_to_element(section_title)
        section_title.click()

        try:
            section_content = self.visible_element(accordian[accordian_num]['content']).text
        except TimeoutException:
            self.go_to_element(section_title)
            section_title.click()
            section_content = self.element_is_clickable(accordian[accordian_num]['content']).text

        return [section_title.text, len(section_content)]


