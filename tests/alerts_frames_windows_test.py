import time

from pages.alerts_frames_windwos_page import BrowserWindowsPage, AlertsPage


class TestAlertsFramesWindows:
    class TestBrowserWindows:

        def test_new_tab_and_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result_tab, text_result_window = new_tab_page.check_new_tab_and_window()

            assert text_result_tab == "This is a sample page"
            assert text_result_window == "This is a sample page"

        def test_alert_button_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_text = alerts_page.click_button_to_alert()
            assert alerts_text == "You clicked a button", "Alert did not show up"

        def test_5_sec_after_test_alert_button_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            alerts_text = alerts_page.click_button_to_alert_appear_in_5_sec()
            assert alerts_text == "This alert appeared after 5 seconds", "Alert did not show up"

        def test_confirm_box_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            confirm_box = alerts_page.check_confirm_alert()
            assert confirm_box == "You selected Ok", "Alert did not show up"

        def test_prompt_click(self, driver):
            alerts_page = AlertsPage(driver, "https://demoqa.com/alerts")
            alerts_page.open()
            text, alerts_text = alerts_page.check_prompt_box_input()
            assert text in alerts_text, "Alert did not show up"
