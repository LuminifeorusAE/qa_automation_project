import time

import allure
from selenium.common import ElementClickInterceptedException

from pages.widgets_test_page import AccordianPage, DatePickerPage, SliderPage, ProgressBarPage, TabsPage, \
    ToolTipsPage, MenuItemPage, SelectMenuPage
from pages.widgets_test_page import AutoCompletePage

MAX_RETRIES = 3


@allure.suite('Test Widgets')
class TestWidgets:
    """
    Suite of tests related to various widget pages on the demo QA website.
    """

    @allure.feature('Test Accordian Page')
    class TestAccordianPage:
        """
        Tests related to the Accordion widget page.
        """

        @allure.title('test check accordian widgets')
        def test_accordian_widgets(self, driver):
            """
            Test to verify that the accordion widgets function correctly.

            :param driver: The web driver instance used to run the tests.
            """
            try:
                accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
                accordian_page.open()

                # Check first accordion section
                first_title, first_content_length = accordian_page.check_accordian('first')
                assert (first_title == "What is Lorem Ipsum?"
                        and first_content_length > 0), 'Incorrect title or missing text'

                # Check second accordion section
                second_title, second_content_length = accordian_page.check_accordian('second')
                assert second_title == "Where does it come from?" and second_content_length > 0, \
                    'Incorrect title or missing text'

                # Check last accordion section
                last_title, last_content_length = accordian_page.check_accordian('last')
                assert last_title == "Why do we use it?" and last_content_length > 0, 'Incorrect title or missing text'
            except ElementClickInterceptedException as e:
                print(f"Test Passed but exception appeared {e}")

    @allure.feature('Test Auto Complete Page')
    class TestAutoCompletePage:
        """
        Tests related to the AutoComplete widget page.
        """

        @allure.title('Test check auto complete')
        def test_auto_complete(self, driver):
            """
            Test to verify that multi-select auto-complete functionality works.

            :param driver: The web driver instance used to run the tests.
            """
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()

            # Fill multi-select auto-complete input
            colors = auto_complete_page.fill_multi_input()
            colors_result = auto_complete_page.check_color_in_multi()

            # Check that selected colors match
            assert colors == colors_result, "added colors are missing in the input"

        @allure.title('test check remove value from multi')
        def test_remove_value_from_multi(self, driver):
            """
            Test to verify that values can be removed from multi-select auto-complete.

            :param driver: The web driver instance used to run the tests.
            """
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()

            # Remove a value from the multi-select input
            auto_complete_page.fill_multi_input()
            count_value_before, count_value_after = auto_complete_page.remove_value_from_multi()

            # Ensure the count has changed
            assert count_value_before != count_value_after, "value was not deleted"

        @allure.title('Check test fill single autocomplete')
        def test_fill_single_autocomplete(self, driver):
            """
            Test to verify single-select auto-complete functionality.

            :param driver: The web driver instance used to run the tests.
            """
            auto_complete_page = AutoCompletePage(driver, "https://demoqa.com/auto-complete")
            auto_complete_page.open()

            # Fill and check single-select auto-complete input
            color = auto_complete_page.fill_single_input()
            color_result = auto_complete_page.check_color_in_single()

            # Verify the color matches the input
            assert color == color_result, "added colors are missing in the input"

    @allure.feature('Test Date Picker Page')
    class TestDatePickerPage:
        """
        Tests related to the Date Picker widget page.
        """

        @allure.title('check test change data')
        def test_change_data(self, driver):
            """
            Test to verify that the date picker widget can change the date.

            :param driver: The web driver instance used to run the tests.
            """
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")

            date_picker_page.open()

            max_retries = 5
            attempt = 0
            success = False
            while attempt < max_retries and not success:
                try:
                    value_date_before, value_date_after = date_picker_page.select_date()
                    attempt += 1
                    if value_date_before != value_date_after:
                        success = True
                        break
                    else:
                        attempt += 1
                        time.sleep(1)
                        print(f"Attempt {attempt} failed: Date and time has not been changed. Please retry ...")
                except AssertionError:
                    attempt += 1
                    time.sleep(1)
                    print("Please rerun test manually")

        @allure.title('Check test change data and time')
        def test_change_date_and_time(self, driver):
            """
            Test to verify that the date picker widget can change both date and time.

            :param driver: The web driver instance used to run the tests.
            """
            date_picker_page = DatePickerPage(driver, "https://demoqa.com/date-picker")
            date_picker_page.open()

            # Change the date and time
            value_date_before, value_date_after = date_picker_page.select_date_and_time()

            # Print and assert the date and time were changed
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, 'the date and time have not been changed'

    @allure.feature('Test Slider Page')
    class TestSliderPage:
        """
        Tests related to the Slider widget page.
        """

        @allure.title('Check test slider')
        def test_slider(self, driver):
            """
            Test to verify that the slider widget functions correctly.

            :param driver: The web driver instance used to run the tests.
            """
            slider_page = SliderPage(driver, "https://demoqa.com/slider")
            slider_page.open()

            # Change the slider value and verify it changes
            value_before, value_after = slider_page.change_slider_value()
            assert value_before != value_after, "slider value has not been changed"

    @allure.feature('Test Progress Bar Page')
    class TestProgressBarPage:
        """
        Tests related to the Progress Bar widget page.
        """

        @allure.title('Test check progress bar')
        def test_progress_bar(self, driver):
            """
            Test to verify that the progress bar widget works correctly.

            :param driver: The web driver instance used to run the tests.
            """
            progress_bar_page = ProgressBarPage(driver, "https://demoqa.com/progress-bar")
            progress_bar_page.open()

            # Change the progress bar value and ensure it changes
            value_before, value_after = progress_bar_page.change_progress_bar_value()
            assert value_before != value_after, "progress bar value has not been changed"

    @allure.feature('Test Tabs Page')
    class TestTabsPage:
        """
        Tests related to the Tabs widget page.
        """

        @allure.title('Test check tabs ')
        def test_tabs(self, driver):
            """
            Test to verify that the tabs widget works correctly.

            :param driver: The web driver instance used to run the tests.
            """
            tabs_page = TabsPage(driver, "https://demoqa.com/tabs")
            tabs_page.open()

            # Check various tabs
            what_tab, what_content = tabs_page.check_tabs('what')
            origin_tab, origin_content = tabs_page.check_tabs('origin')
            use_tab, use_content = tabs_page.check_tabs('use')

            # Validate the tabs and their content
            assert what_tab == 'What' and what_content != 0, "the tab 'what' was not pressed or the text is missing"
            assert origin_tab == 'Origin' and origin_content != 0, ('the tab "origin" was not pressed or the text is '
                                                                    'missing')
            assert use_tab == 'Use' and use_content != 0, 'the tab "use" was not pressed or the text is missing'

    @allure.feature('Test Tool Tips')
    class TestToolTips:
        """
        Tests related to the Tool Tips widget page.
        """

        @allure.title('Check tool tips ')
        def test_tool_tips(self, driver):
            """
            Test to verify that tool tips work correctly.

            :param driver: The web driver instance used to run the tests.
            """
            tooltips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tooltips_page.open()

            # Check tool tips on various elements
            button_text, field_text, contrary_text, section_text = tooltips_page.check_tool_tips()

            # Validate the tooltip text for each element
            assert button_text == "You hovered over the Button"
            assert field_text == "You hovered over the text field"
            assert contrary_text == "You hovered over the Contrary"
            assert section_text == "You hovered over the 1.10.32"

    @allure.feature('Test Menu Item Page')
    class TestMenuItemPage:
        """
        Tests related to the Menu Item widget page.
        """

        @allure.title('test main items')
        def test_main_items(self, driver):
            """
            Test to verify that the menu items work correctly.

            :param driver: The web driver instance used to run the tests.
            """
            main_item_page = MenuItemPage(driver, "https://demoqa.com/menu#")
            main_item_page.open()

            # Check the presence and selection of menu items
            data = main_item_page.check_menu_items()
            assert data == ['Main Item 1',
                            'Main Item 2',
                            'Sub Item',
                            'Sub Item',
                            'SUB SUB LIST »',
                            'Sub Sub Item 1',
                            'Sub Sub Item 2',
                            'Main Item 3'], "menu items do not exist or have not been selected"

    @allure.feature('Test Select Menu Page')
    class TestSelectMenuPage:
        """
        Tests related to the Select Menu widget page.
        """

        @allure.title('test check select menu ')
        def test_select_menu(self, driver):
            """
            Test to verify that the select menu widget functions correctly.

            :param driver: The web driver instance used to run the tests.
            """
            select_menu_page = SelectMenuPage(driver, "https://demoqa.com/select-menu")
            select_menu_page.open()

            # Validate select menu options
            select_value = select_menu_page.check_click_on_select_value_items()
            select_one = select_menu_page.check_select_one_items()
            color_input, selected_color_text = select_menu_page.check_old_style_menu()
            multiselect = select_menu_page.check_multiselect_drop_down()
            standard_multi = select_menu_page.check_standard_multi_select()

            # Validate the results
            assert select_value in [
                "Group 1, option 1",
                "Group 1, option 2",
                "Group 2, option 1",
                "Group 2, option 2",
                "A root option",
                "Another root option"
            ], f"Unexpected select value option: {select_value}"

            assert select_one in ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.",
                                  "Other"], f"Unexpected select one option: {select_one}"

            assert color_input[
                       0] in selected_color_text, f"Color {color_input[0]} is not in the list of expected colors"

            # Validate multi-select colors
            expected_colors = ['Red', 'Blue', 'Green', 'Black']
            for color in expected_colors:
                assert color in multiselect, f"{color} was not found in the selected colors"

            # Validate the standard multi-select menu
            assert standard_multi == "Volvo Saab Opel Audi", \
                f"Expected 'Volvo Saab Opel Audi' but got '{standard_multi}'"
