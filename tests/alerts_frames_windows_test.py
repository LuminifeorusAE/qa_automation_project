import time

from pages.alerts_frames_windwos_page import BrowserWindowsPage


class TestAlertsFramesWindows:

    class TestBrowserWindows:

        def test_new_tab_and_window(self, driver):
            new_tab_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result_tab, text_result_window = new_tab_page.check_new_tab_and_window()

            assert text_result_tab == "This is a sample page"
            assert text_result_window == "This is a sample page"



