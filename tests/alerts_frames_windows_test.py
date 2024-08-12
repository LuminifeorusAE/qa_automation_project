import time

import allure

from pages.alerts_frames_windwos_page import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalButtonPage


@allure.suite('Test Alerts Frames Windows')
class TestAlertsFramesWindows:
    @allure.feature('Test Browser Windows')
    class TestBrowserWindows:
        @allure.title('test new tab and window')
        def test_new_tab_and_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result_tab, text_result_window = new_tab_page.check_new_tab_and_window()

            assert text_result_tab == "This is a sample page"
            assert text_result_window == "This is a sample page"

        @allure.title('test alert button click')
        def test_alert_button_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_text = alerts_page.click_button_to_alert()
            assert alerts_text == "You clicked a button", "Alert did not show up"

        @allure.title('test button that appears in five seconds')
        def test_5_sec_after_test_alert_button_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_text = alerts_page.click_button_to_alert_appear_in_5_sec()
            assert alerts_text == "This alert appeared after 5 seconds", "Alert did not show up"

        @allure.title('test confirm box click')
        def test_confirm_box_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            confirm_box = alerts_page.check_confirm_alert()
            assert confirm_box == "You selected Ok", "Alert did not show up"

        @allure.title('test prompt click')
        def test_prompt_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text, alerts_text = alerts_page.check_prompt_box_input()
            assert text in alerts_text, "Alert did not show up"

        @allure.feature('Test Frames')
        class TestFrames:
            @allure.title('test frame')
            def test_frame(self, driver):
                frames_page = FramesPage(driver, "https://demoqa.com/frames")
                frames_page.open()
                result_frame_1 = frames_page.check_frame("frame1")
                result_frame_2 = frames_page.check_frame("frame2")
                assert result_frame_1 == "['This is a sample page', '500px', '350px']", " The frame does not exist"
                assert result_frame_2 == "['This is a sample page', '100px', '100px']", " The frame does not exist"

        @allure.feature('Test Nested Frames')
        class TestNestedFrames:
            @allure.title('test nested frame')
            def test_nested_frame(self, driver):
                frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
                frames_page.open()
                child_frame_text, parent_frame_text = frames_page.check_nested_frames()
                assert child_frame_text == "Parent frame", ""
                assert parent_frame_text == "Child Iframe", ""

        @allure.feature('Test Modal Dialogs Page')
        class TestModalDialogsPage:
            @allure.title('test modal dialogs')
            def test_modal_dialogs(self, driver):
                modal_dialog = ModalButtonPage(driver, "https://demoqa.com/modal-dialogs")
                modal_dialog.open()
                small_modal_text, large_modal_text = modal_dialog.check_dialog_buttons()
                assert len(small_modal_text) < len(
                    large_modal_text), "Small modal text is not shorter than large modal text"
                # add to the test title checkers
