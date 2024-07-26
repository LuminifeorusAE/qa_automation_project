import random
import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generate_date
from locators.widgeds_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, \
    MenuItemPageLocators
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


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    def select_date(self):
        date = next(generate_date())
        input_date = self.visible_element(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    def select_date_and_time(self):
        date = next(generate_date())
        input_date = self.visible_element(self.locators.DATE_AND_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_clickable(self.locators.DATE_AND_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_MONTH_LIST, date.month)
        self.element_is_clickable(self.locators.DATE_AND_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_YEAR_LIST, "2023")
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_AND_TIME_SELECT_TIME_LIST, date.time)
        input_date_after = self.visible_element(self.locators.DATE_AND_TIME_INPUT)
        value_date_after = input_date_after.get_attribute('value')
        return value_date_before, value_date_after

    def set_date_by_text(self, element, value):
        select = Select(self.element_present(element))  # !!!add Select methods in base page later !!!
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    def change_slider_value(self):
        value_before = self.visible_element(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.visible_element(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.visible_element(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    #  write method that waits until progress bar is finished and resets it
    def change_progress_bar_value(self):
        value_before = self.not_visible_elements(self.locators.PROGRESS_VALUE).get_attribute('aria-valuenow')
        progress_bar_button = self.element_is_clickable(self.locators.START_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1, 15))
        progress_bar_button.click()
        value_after = self.element_present(self.locators.PROGRESS_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    def check_tabs(self, tabs_name):
        tabs = {
            'what': {
                'title': self.locators.WHAT_TAB,
                'content': self.locators.WHAT_TAB_CONTENT
            },
            'origin': {
                'title': self.locators.ORIGIN_TAB,
                'content': self.locators.ORIGIN_TAB_CONTENT
            },
            'use': {
                'title': self.locators.USE_TAB,
                'content': self.locators.USE_TAB_CONTENT
            },
            'more': {
                'title': self.locators.MORE_TAB,
                'content': self.locators.MORE_TAB_CONTENT
            }
        }
        tabs_titles = self.element_is_clickable(tabs[tabs_name]['title'])
        tabs_titles.click()

        tabs_content = self.visible_element(tabs[tabs_name]['content']).text

        return tabs_titles.text, len(tabs_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    def get_text_from_tool_tips(self, hover_element, wait_element):
        element = self.element_present(hover_element)
        self.go_to_element(element)
        self.action_move_to_element(element)
        time.sleep(1)  # !!! rewrite this part later to code work without time sleep!!!
        self.visible_element(wait_element)
        tool_tip_text = self.visible_element(self.locators.TOOL_TIPS_INNERS)
        return tool_tip_text.text

    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_from_tool_tips(
            self.locators.HOVER_ME_TO_SEE_BUTTON,
            self.locators.TOOL_TIP_BUTTON
        )

        tool_tip_text_field = self.get_text_from_tool_tips(
            self.locators.INPUT_HOVER_ME_TO_SEE,
            self.locators.TOOL_TIP_INPUT
        )

        tool_tip_text_contrary = self.get_text_from_tool_tips(
            self.locators.CONTRARY_XPATH,
            self.locators.TOOL_TIP_CONTRARY
        )

        tool_tip_text_section = self.get_text_from_tool_tips(
            self.locators.SECTION_XPATH,
            self.locators.TOOL_TIP_SECTION
        )

        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuItemPage(BasePage):
    locators = MenuItemPageLocators()

    def check_menu_items(self):
        menu_items_list = self.elements_are_present(self.locators.MAIN_ITEM_LIST)
        data = []
        for item in menu_items_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data




