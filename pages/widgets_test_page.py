import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generate_date
from locators.widgeds_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators, \
    SliderPageLocators, ProgressBarPageLocators, TabsPageLocators, ToolTipsPageLocators, \
    MenuItemPageLocators, SelectMenuPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step("test check accordian")
    def check_accordian(self, accordian_num):
        """
        Checks the accordion section (either 'first', 'second', or 'last'), clicks on the title,
        and retrieves the content length and the section title text.

        Args:
            accordian_num (str): Specifies which accordion section to interact with ('first', 'second', 'last').
            Returns:
            list: The title of the section and the length of the content text.
        """
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
        # Click on the section title and retrieve the content length
        section_title = self.element_is_clickable(accordian[accordian_num]['title'])
        self.go_to_element(section_title)
        section_title.click()
        # Retry clicking if TimeoutException is raised.
        try:
            section_content = self.visible_element(accordian[accordian_num]['content']).text
        except TimeoutException:
            self.go_to_element(section_title)
            section_title.click()
            section_content = self.element_is_clickable(accordian[accordian_num]['content']).text

        return [section_title.text, len(section_content)]


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step("test fill multi input line ")
    def fill_multi_input(self):
        """
        Fills the multi-input line with random colors using auto-complete feature.

       Returns:
            list: The list of colors that were entered.
       """
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step("test removing value in multi input line ")
    def remove_value_from_multi(self):
        """
        Removes a single value from the multi-input line.

        Returns:
            tuple: Count of values before and after removing one.
        """
        count_value_before = len(self.elements_are_present(self.locators.MULTI_INPUT_VALUE))
        remove_button_list = self.every_visible_element(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_INPUT_VALUE))
        return count_value_before, count_value_after

        # !!!write method that deletes every value!!!

    @allure.step("test check color in multi")
    def check_color_in_multi(self):
        """
        Retrieves the colors currently present in the multi-input container.

        Returns:
            list: List of colors currently selected in the multi-input.
        """
        color_list = self.elements_are_present(self.locators.MULTI_INPUT_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step("fill single input")
    def fill_single_input(self):
        """
        Fills the single-input line with a random color using the auto-complete feature.

        Returns:
            str: The color that was entered.
        """
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.element_is_clickable(self.locators.SINGLE_INPUT)
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    @allure.step("check color in single container")
    def check_color_in_single(self):
        """
        Retrieves the color currently present in the single-input container.

        Returns:
            str: The color currently selected in the single-input.
        """
        color = self.visible_element(self.locators.SINGLE_CONTAINER)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step("test selecting date")
    def select_date(self):
        """
        Selects a date using the date picker by setting the month, year, and day.

        Returns:
            tuple: The value of the date before and after the selection.
        """
        date = next(generate_date())
        input_date = self.visible_element(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        self.go_to_element(input_date)
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step("test select date and time ")
    def select_date_and_time(self):
        """
        Selects both date and time using the date-time picker.

        Returns:
            tuple: The value of the date-time before and after the selection.
        """
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

    @allure.step("test set date by text")
    def set_date_by_text(self, element, value):
        """
        Selects an option from a drop-down based on the visible text.

        Args:
            element: The element of the drop-down to select from.
            value (str): The visible text of the option to select.
        """
        select = Select(self.element_present(element))  # !!!add Select methods in base page later !!!
        select.select_by_visible_text(value)

    @allure.step("test date item from list ")
    def set_date_item_from_list(self, elements, value):
        """
        Selects a specific item from a list of elements based on its text.

        Args:
            elements: The list of elements to choose from.
            value (str): The text value to match and click on.
        """
        item_list = self.elements_are_present(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step("test change slider value")
    def change_slider_value(self):
        """
        Adjusts the slider by a random offset and retrieves its value before and after the change.

        Returns:
            tuple: The slider value before and after changing it.
        """
        value_before = self.visible_element(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.visible_element(self.locators.INPUT_SLIDER)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(1, 100), 0)
        value_after = self.visible_element(self.locators.SLIDER_VALUE).get_attribute('value')
        return value_before, value_after


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step("test change progress bar value ")
    #  write method that waits until progress bar is finished and resets it
    def change_progress_bar_value(self):
        """
        Starts the progress bar, waits for a random amount of time, then stops it.

        Returns:
            tuple: The progress value before and after the operation.
        """
        value_before = self.not_visible_elements(self.locators.PROGRESS_VALUE).get_attribute('aria-valuenow')
        progress_bar_button = self.element_is_clickable(self.locators.START_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(1, 10))
        progress_bar_button.click()
        value_after = self.element_present(self.locators.PROGRESS_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step("test check tabs contents")
    def check_tabs(self, tabs_name):
        """
        Checks the contents of a specific tab by its name ('what', 'origin', 'use', 'more').

        Args:
            tabs_name (str): The name of the tab to select.

        Returns:
            tuple: The tab's title and the length of the content text.
        """
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

    @allure.step("get text from tool tips")
    def get_text_from_tool_tips(self, hover_element, wait_element):
        """
        Retrieves the text from a tooltip by hovering over the specified element and waiting for the tooltip to appear.

        Args:
            hover_element: The element to hover over to display the tooltip.
            wait_element: The element representing the tooltip content to wait for.

        Returns:
            str: The tooltip text.
        """
        element = self.element_present(hover_element)
        self.go_to_element(element)
        self.action_move_to_element(element)
        time.sleep(1)  # !!! rewrite this part later to code work without time sleep!!!
        self.visible_element(wait_element)
        tool_tip_text = self.visible_element(self.locators.TOOL_TIPS_INNERS)
        return tool_tip_text.text

    @allure.step("check tool tips")
    def check_tool_tips(self):
        """
        Retrieves and returns the tooltip texts for various elements on the page.

        Returns:
            tuple: Tooltip texts for button, field, contrary section, and general section.
        """
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

    @allure.step("check menu items")
    def check_menu_items(self):
        """
        Retrieves and returns the text of all menu items by hovering over them.

        Returns:
            list: A list of menu item texts.
        """
        menu_items_list = self.elements_are_present(self.locators.MAIN_ITEM_LIST)
        data = []
        for item in menu_items_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data


class SelectMenuPage(BasePage):
    locators = SelectMenuPageLocators()

    @allure.step("check click on select value items")
    def check_click_on_select_value_items(self):
        """
        Clicks on the drop-down and selects a random value from the options.

        Returns:
            str: The selected value.
        """
        select_value = self.element_is_clickable(self.locators.SELECT_VALUE_DROP)
        select_value.click()

        options = [
            "Group 1, option 1",
            "Group 1, option 2",
            "Group 2, option 1",
            "Group 2, option 2",
            "A root option",
            "Another root option"
        ]

        select_option = random.choice(options)

        option_input = self.element_present(self.locators.SELECT_VALUE_DROP_OPTION)
        option_input.send_keys(select_option)
        option_input.send_keys(Keys.ENTER)
        return select_option

    @allure.step("check select on items")
    def check_select_one_items(self):
        """
         Clicks on the drop-down and selects a random title (e.g., 'Dr.', 'Mr.', etc.).

        Returns:
            str: The selected title.
        """
        select_one = self.element_is_clickable(self.locators.SELECT_ONE_DROP)
        select_one.click()
        options = ["Dr.",
                   "Mr.",
                   "Mrs.",
                   "Ms.",
                   "Prof.",
                   "Other", ]

        select_option = random.choice(options)

        option_input = self.element_present(self.locators.SELECT_ONE_DROP_OPTION)
        option_input.send_keys(select_option)
        option_input.send_keys(Keys.ENTER)
        return select_option

    @allure.step("check old style menu")
    def check_old_style_menu(self):
        """
        Selects a random color using the old-style select menu.

        Returns:
            tuple: The selected color and the displayed text.
        """
        color_option = self.element_is_clickable(self.locators.SELECT_OLD_STYLE_DROP)
        color_option.click()
        color_input = random.sample(next(generated_color()).color_name, k=1)
        color_option.send_keys(color_input)
        color_option.send_keys(Keys.ENTER)
        return color_input, color_option.text

    @allure.step("check multiselect drop down")
    def check_multiselect_drop_down(self):
        """
        Selects multiple options from the multi-select drop-down by sending the ENTER key multiple times.

        Returns:
            list: The filtered list of selected options.
        """
        select_color = self.visible_element(self.locators.MULTISELECT_DROP)
        select_color.click()
        option_input = self.element_present(self.locators.MULTISELECT_DROP_OPTION)
        count = 0
        while count < 4:
            option_input.send_keys(Keys.ENTER)
            count += 1
        raw_text = select_color.text
        selected_colors = [color.strip() for color in raw_text.split('\n') if
                           color.strip() and 'selected' not in color and 'No options' not in color]
        filtered_list = list(set(selected_colors))
        return filtered_list

    @allure.step("check standard multi select")
    def check_standard_multi_select(self):
        """
        Retrieves the text of the selected options in the standard multi-select.

        Returns:
            str: The selected options as a single string.
        """
        multi_select = self.visible_element(self.locators.STANDARD_MULTI_SELECT)
        return multi_select.text.replace('\n', " ")
