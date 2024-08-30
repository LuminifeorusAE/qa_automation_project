# base_page.py
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base class for page object models, containing reusable methods for interacting with web elements.
    """

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Open the page with the given URL."""
        self.driver.get(self.url)

    def wait_for_element(self, condition, timeout=10):
        """
        Wait for a specific condition to be met and return the result.

        Args:
            condition: The expected condition to wait for.
            timeout: Maximum wait time in seconds (default: 10).

        Returns:
            The element if the condition is met, otherwise raises a TimeoutException.
        """
        return wait(self.driver, timeout).until(condition)

    def visible_element(self, locator, timeout=10):
        """
        Wait for an element to be visible and return it.

        Args:
            locator: The locator tuple (By, value) to locate the element.
            timeout: Maximum wait time in seconds (default: 10).

        Returns:
            The visible WebElement.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def every_visible_element(self, locator, timeout=5):
        """
        Wait for all elements matching the locator to be visible and return them.

        Args:
            locator: The locator tuple (By, value) to locate the elements.
            timeout: Maximum wait time in seconds (default: 5).

        Returns:
            A list of visible WebElements.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_present(self, locator, timeout=10):
        """
        Wait for an element to be present in the DOM.

        Args:
            locator: The locator tuple (By, value) to locate the element.
            timeout: Maximum wait time in seconds (default: 10).

        Returns:
            The WebElement if present.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def alert_is_present(self, timeout=10):
        """
        Wait for an alert to be present within the specified timeout.

        Args:
            timeout (int): The number of seconds to wait for the alert (default is 10 seconds).

        Returns:
           Alert: The alert object if it appears within the timeout.
        """
        return wait(self.driver, timeout).until(EC.alert_is_present())

    def elements_are_present(self, locator, timeout=5):
        """
        Wait for all elements matching the locator to be present in the DOM.

        Args:
            locator: The locator tuple (By, value) to locate the elements.
            timeout: Maximum wait time in seconds (default: 5).

        Returns:
            A list of WebElements.
        """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def not_visible_elements(self, locator, timeout=5):
        """
        Wait for an element to become invisible.

        Args:
            locator: The locator tuple (By, value) to locate the element.
            timeout: Maximum wait time in seconds (default: 5).

        Returns:
            True if the element is invisible, otherwise raises a TimeoutException.
        """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=7):
        """
        Wait for an element to be clickable.

        Args:
            locator: The locator tuple (By, value) to locate the element.
            timeout: Maximum wait time in seconds (default: 7).

        Returns:
            The clickable WebElement.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        """
        Scroll the page to bring the element into view.

        Args:
            element: The WebElement to bring into view.
        """
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def action_double_click(self, element):
        """
        Perform a double click action on the element.

        Args:
            element: The WebElement to double-click.
        """
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def action_drag_and_drop_by_offset(self, element, x_offset, y_offset):
        """
        Drag and drop the element by an offset.

        Args:
            element: The WebElement to drag.
            x_offset: Horizontal offset in pixels.
            y_offset: Vertical offset in pixels.
        """
        self.go_to_element(element)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_offset, y_offset).perform()

    def action_drag_and_drop_to_element(self, item, destination):
        """Drag and drop the item onto the destination element."""
        action = ActionChains(self.driver)
        action.drag_and_drop(item, destination).perform()

    def action_move_to_element(self, element):
        """Move the cursor to the element."""
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    def action_right_click(self, element):
        """Perform a right-click (context click) on the element."""
        action = ActionChains(self.driver)
        action.context_click(element).perform()
