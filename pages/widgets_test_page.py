import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.widgeds_locators import AccordianPageLocators, AutoCompletePageLocators
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


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    def fill_multi_input(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_INPUT_VALUE))
        remove_button_list = self.every_visible_element(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_INPUT_VALUE))
        return count_value_before, count_value_after

        # !!!write method that deletes every value!!!

    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_INPUT_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_single_input(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        color = self.visible_element(self.locators.SINGLE_CONTAINER)
        return color.text

