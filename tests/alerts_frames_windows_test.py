import allure
from pages.alerts_frames_windwos_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalButtonPage

@allure.suite('Test Alerts Frames Windows')
class TestAlertsFramesWindows:
    """
    This class contains test cases for testing alerts, frames, and windows functionalities
    on the DemoQA website.
    """

    @allure.feature('Test Browser Windows')
    class TestBrowserWindows:
        """
        Test cases related to browser windows functionalities.
        """

        @allure.title('test new tab and window')
        def test_new_tab_and_window(self, driver):
            """
            Test that a new tab and a new window can be opened successfully.

            Args:
                driver: WebDriver instance used for testing.

            Asserts:
                - The content of the new tab is "This is a sample page".
                - The content of the new window is "This is a sample page".
            """
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result_tab, text_result_window = new_tab_page.check_new_tab_and_window()

            assert text_result_tab == "This is a sample page"
            assert text_result_window == "This is a sample page"

        @allure.title('test alert button click')
        def test_alert_button_click(self, driver):
            """
            Test that an alert box is displayed when a button is clicked.

            Args:
                driver: WebDriver instance used for testing.

            Asserts:
                - The alert text is "You clicked a button".
            """
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_text = alerts_page.click_button_to_alert()
            assert alerts_text == "You clicked a button", "Alert did not show up"

        @allure.title('test button that appears in five seconds')
        def test_5_sec_after_test_alert_button_click(self, driver):
            """
            Test that an alert box appears after 5 seconds when a button is clicked.

            Args:
                driver: WebDriver instance used for testing.

            Asserts:
                - The alert text is "This alert appeared after 5 seconds".
            """
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_text = alerts_page.click_button_to_alert_appear_in_5_sec()
            assert alerts_text == "This alert appeared after 5 seconds", "Alert did not show up"

        @allure.title('test confirm box click')
        def test_confirm_box_click(self, driver):
            """
            Test that a confirmation box appears and the "Ok" option can be selected.

            Args:
                driver: WebDriver instance used for testing.

            Asserts:
                - The confirm box text is "You selected Ok".
            """
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            confirm_box = alerts_page.check_confirm_alert()
            assert confirm_box == "You selected Ok", "Alert did not show up"

        @allure.title('test prompt click')
        def test_prompt_click(self, driver):
            """
            Test that a prompt box appears and text can be entered.

            Args:
                driver: WebDriver instance used for testing.

            Asserts:
                - The entered text is part of the prompt alert text.
            """
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text, alerts_text = alerts_page.check_prompt_box_input()
            assert text in alerts_text, "Alert did not show up"

        @allure.feature('Test Frames')
        class TestFrames:
            """
            Test cases related to frame functionalities.
            """

            @allure.title('test frame')
            def test_frame(self, driver):
                """
                Test that frames can be located and their content is as expected.

                Args:
                    driver: WebDriver instance used for testing.

                Asserts:
                    - Frame1 contains the correct content and dimensions.
                    - Frame2 contains the correct content and dimensions.
                """
                frames_page = FramesPage(driver, "https://demoqa.com/frames")
                frames_page.open()
                result_frame_1 = frames_page.check_frame("frame1")
                result_frame_2 = frames_page.check_frame("frame2")
                assert result_frame_1 == ['This is a sample page', '500px', '350px'], " The frame does not exist"
                assert result_frame_2 == ['This is a sample page', '100px', '100px'], " The frame does not exist"

        @allure.feature('Test Nested Frames')
        class TestNestedFrames:
            """
            Test cases related to nested frames functionalities.
            """

            @allure.title('test nested frame')
            def test_nested_frame(self, driver):
                """
                Test that nested frames can be located and their content is as expected.

                Args:
                    driver: WebDriver instance used for testing.

                Asserts:
                    - The parent frame contains the correct text.
                    - The child frame contains the correct text.
                """
                frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
                frames_page.open()
                child_frame_text, parent_frame_text = frames_page.check_nested_frames()
                assert child_frame_text == "Parent frame", ""
                assert parent_frame_text == "Child Iframe", ""

        @allure.feature('Test Modal Dialogs Page')
        class TestModalDialogsPage:
            """
            Test cases related to modal dialog functionalities.
            """

            @allure.title('Test modal dialogs')
            def test_modal_dialogs(self, driver):
                """
                Test that modal dialogs can be opened and their content is as expected.

                Args:
                    driver: WebDriver instance used for testing.

                Asserts:
                    - The small modal text is shorter than the large modal text.
                """
                modal_dialog = ModalButtonPage(driver, "https://demoqa.com/modal-dialogs")
                modal_dialog.open()
                small_modal_text, large_modal_text = modal_dialog.check_dialog_buttons()
                assert len(small_modal_text) < len(
                    large_modal_text), (f"Expected small modal text to be shorter than large modal text, but got "
                                        f"{len(small_modal_text)} vs {len(large_modal_text)}")
