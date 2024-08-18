from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to set up and tear down the Selenium WebDriver instance.

    This fixture initializes a Chrome WebDriver, maximizes the browser window,
    and yields the driver to the test functions. After the test completes, it
    captures a screenshot of the browser and attaches it to the Allure report
    before quitting the driver.

    Scope: Function-level, meaning a new driver instance is created for each test function.

    Returns:
        webdriver.Chrome: The instance of the Chrome WebDriver.
    """
    # Initialize the Chrome WebDriver with the ChromeDriverManager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # Maximize the browser window
    driver.maximize_window()

    # Yield the driver to the test functions
    yield driver

    # Capture a screenshot and attach it to the Allure report
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)

    # Quit the WebDriver instance
    driver.quit()
