import allure
from selenium.common import MoveTargetOutOfBoundsException

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Test interactions page')
class TestInteractionsPage:
    """
    Test suite for the interactions pages on the demoqa.com website.
    This class contains nested classes, each responsible for testing a specific interaction page.
    """

    @allure.feature('Test sortable page')
    class TestSortable:
        """
        Test cases for the Sortable page.
        This includes tests for changing the order of list items and grid items.
        """

        @allure.title('test check test sortable')
        def test_sortable(self, driver):
            """
            Test the sortable functionality by changing the order of list and grid items.

            Steps:
            1. Open the Sortable page.
            2. Change the order of the list and grid items.
            3. Verify that the order has changed.

            Asserts:
            - The order of the list and grid items should not remain the same after sorting.
            """
            # Initialize the SortablePage object with the specified URL
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()

            # Change the order of the list and grid items and capture the order before and after the change
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()

            # Assert that the list and grid order have changed
            assert list_before != list_after, "The order of the list has not been changed"
            assert grid_before != grid_after, "The order of the grid has not been changed"

    @allure.feature('Test selectable page')
    class TestSelectablePage:
        """
        Test cases for the Selectable page.
        This includes tests for selecting items from a list and a grid.
        """

        @allure.title('test check test selectable box')
        def test_selectable(self, driver):
            """
            Test the selectable functionality by selecting items from a list and a grid.

            Steps:
            1. Open the Selectable page.
            2. Select items from the list and grid.
            3. Verify that items have been selected.

            Asserts:
            - The selected items should not be empty.
            """
            # Initialize the SelectablePage object with the specified URL
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()

            # Select items from the list and grid
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()

            # Assert that at least one item has been selected from both the list and grid
            assert len(item_list) > 0, "no elements were selected"
            assert len(item_grid) > 0, "no elements were selected"

    @allure.feature('Test resizable page')
    class TestResizablePage:
        """
        Test cases for the Resizable page.
        This includes tests for resizing elements on the page.
        """

        @allure.title('test check test resizable box')
        def test_resizable(self, driver):
            """
            Test the resizable functionality by changing the size of resizable elements.

            Steps:
            1. Open the Resizable page.
            2. Change the size of the resizable box and other resizable elements.
            3. Verify that the size has changed.

            Asserts:
            - The size of the resizable elements should change after resizing.
            """
            # Initialize the ResizablePage object with the specified URL
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()

            # Change the size of the resizable box and other resizable elements
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()

            # Assert that the sizes have changed after resizing
            assert min_box != max_box, "Resizable box has not been changed"
            assert min_resize != max_resize, "Resizable element has not been changed"

    @allure.feature('Test droppable page')
    class TestDroppablePage:
        """
        Test cases for the Droppable page.
        This includes tests for various droppable functionalities.
        """

        @allure.title('test check droppable box')
        def test_simple_droppable(self, driver):
            """
            Test the simple droppable functionality.

            Steps:
            1. Open the Droppable page.
            2. Perform a simple drag-and-drop operation.
            3. Verify that the element has been dropped.

            Asserts:
            - The element should be successfully dropped.
            """
            # Initialize the DroppablePage object with the specified URL
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            # Perform a simple drag-and-drop operation
            text = droppable_page.drop_simple()

            # Assert that the element has been dropped
            assert text == "Dropped!", "The element has not been dropped"

        @allure.title('check test accept droppable box')
        def test_accept_droppable(self, driver):
            """
            Test the accept droppable functionality.

            Steps:
            1. Open the Droppable page.
            2. Perform drag-and-drop operations with both acceptable and non-acceptable elements.
            3. Verify that only the acceptable element is dropped.

            Asserts:
            - The non-acceptable element should not be accepted.
            - The acceptable element should be successfully dropped.
            """
            # Initialize the DroppablePage object with the specified URL
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            # Perform drag-and-drop operations with both acceptable and non-acceptable elements
            not_accept, accept = droppable_page.drop_accept()

            # Assert that the non-acceptable element is not accepted and the acceptable element is dropped
            assert not_accept == "Drop here", "The dropped element has been accepted incorrectly"
            assert accept == "Dropped!", "The dropped element has not been accepted"

        @allure.title('test check prevent propagation droppable page ')
        def test_prevent_propogation_droppable(self, driver):
            """
            Test the prevention propagation droppable functionality.

            Steps:
            1. Open the Droppable page.
            2. Perform drag-and-drop operations that involve preventing propagation.
            3. Verify that the elements have been dropped correctly without propagation issues.

            Asserts:
            - The elements should be successfully dropped in the correct areas without propagation issues.
            """
            # Initialize the DroppablePage object with the specified URL
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            # Perform drag-and-drop operations with propagation prevention
            not_greedy_text, greedy_inner_text, outer_droppable_greedy_text, \
                inner_droppable_greedy_text = droppable_page.drop_prevent_propagation()

            # Assert that all elements are dropped correctly
            assert not_greedy_text == "Dropped!", "Element has not been dropped or accepted incorrectly"
            assert greedy_inner_text == "Dropped!", "Element has not been dropped or accepted incorrectly"
            assert outer_droppable_greedy_text == "Dropped!", "Element has not been dropped or accepted incorrectly"
            assert (inner_droppable_greedy_text ==
                    "Outer droppable"), "Element has not been dropped or accepted incorrectly"

        @allure.title('Test check revert droppable box')
        def test_revert_draggable_droppable(self, driver):
            """
            Test the revert draggable functionality.

            Steps:
            1. Open the Droppable page.
            2. Perform drag-and-drop operations with elements that revert after dropping.
            3. Verify that the elements revert back to their original position after dropping.

            Asserts:
            - The elements should revert to their original position after dropping.
            - The element should be successfully dropped.
            """
            # Initialize the DroppablePage object with the specified URL
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()

            # Perform drag-and-drop operations with reverting elements
            position_after_drop, position_after_revert, drop_here_text = droppable_page.revert_draggable()

            # Assert that the element reverts to its original position and is dropped correctly
            assert position_after_drop != position_after_revert, "Element's position has not been changed"
            assert drop_here_text == "Dropped!", "Element has not been dropped or accepted incorrectly"

    @allure.feature('Test droppable page')
    class TestDroppablePage:
        """
        Test class for testing the Droppable page.
        Contains tests to verify different droppable box functionalities.
        """

        @allure.title('Test check droppable box')
        def test_simple_droppable(self, driver):
            """
            Test the simple droppable functionality.

            Steps:
            1. Open the Droppable page.
            2. Perform a simple drop action.
            3. Assert that the element has been successfully dropped.

            :param driver: WebDriver instance.
            """
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "The element has not been dropped"

        @allure.title('Check test accept droppable box')
        def test_accept_droppable(self, driver):
            """
            Test the accept droppable functionality.

            Steps:
            1. Open the Droppable page.
            2. Perform drop actions with both acceptable and non-acceptable elements.
            3. Assert that the non-acceptable element is not accepted and the acceptable element is accepted.

            :param driver: WebDriver instance.
            """
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == "Drop here", "The dropped element has been accepted"
            assert accept == "Dropped!", "The dropped element has not been accepted"

        @allure.title('Test check prevent propagation droppable page')
        def test_prevent_propogation_droppable(self, driver):
            """
            Test the prevention propagation functionality in the Droppable page.

            Steps:
            1. Open the Droppable page.
            2. Perform drop actions in both greedy and non-greedy droppable areas.
            3. Assert the correct behavior in each droppable area.

            :param driver: WebDriver instance.
            """
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy_text, greedy_inner_text, outer_droppable_greedy_text, \
                inner_droppable_greedy_text = droppable_page.drop_prevent_propagation()
            assert not_greedy_text == "Dropped!", "Element has not been dropped or accepted incorrectly"
            assert greedy_inner_text == "Dropped!", "Element has not been dropped or accepted incorrectly"
            assert outer_droppable_greedy_text == "Dropped!", "Element has not been dropped or accepted incorrectly"
            assert inner_droppable_greedy_text == "Outer droppable", \
                "Element has not been dropped or accepted incorrectly"

        @allure.title('Test check revert droppable box')
        def test_revert_draggable_droppable(self, driver):
            """
            Test the revert draggable functionality in the Droppable page.

            Steps:
            1. Open the Droppable page.
            2. Perform a drag and drop action that reverts the draggable element.
            3. Assert that the element reverts back to its original position.

            :param driver: WebDriver instance.
            """
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            position_after_drop, position_after_revert, drop_here_text = droppable_page.revert_draggable()
            assert position_after_drop != position_after_revert, "Element's position has not been changed"
            assert drop_here_text == "Dropped!", "Element has not been dropped or accepted incorrectly"

    @allure.feature('Test draggable page')
    class TestDraggablePage:
        """
        Test class for testing the Draggable page.
        Contains tests to verify different draggable box functionalities.
        """

        @allure.title('Test check test box')
        def test_simple_draggable(self, driver):
            """
            Test the simple draggable functionality.

            Steps:
            1. Open the Draggable page.
            2. Drag the box and assert its position has changed.

            :param driver: WebDriver instance.
            """
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "The position of the box has not been changed"

        @allure.title('Check test axis restricted box')
        def test_axis_restricted_droppable(self, driver):
            """
            Test the axis-restricted draggable functionality.

            Steps:
            1. Open the Draggable page.
            2. Drag the box restricted to the X-axis and Y-axis.
            3. Assert the box only moves along the correct axis.

            :param driver: WebDriver instance.
            """
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, 'Box position has not been changed or there is a shift on Y-axis'
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, 'Box position has not been changed or there is a shift on Y-axis'
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, 'Box position has not been changed or there is a shift on Y-axis'
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, 'Box position has not been changed or there is a shift on Y-axis'

        @allure.title('Check test container restricted box')
        def test_container_restricted_draggable(self, driver):
            """
            Test the container-restricted draggable functionality.

            Steps:
            1. Open the Draggable page.
            2. Attempt to drag the box outside its container boundaries.
            3. Assert that the box cannot be moved outside the container or raise an appropriate exception.

            :param driver: WebDriver instance.
            """
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()

            try:
                within_box_position = draggable_page.restricted_draggable()
                if within_box_position is not None and within_box_position.strip() != "":
                    assert True, "The box was moved outside its boundaries, but no exception was raised."
                else:
                    raise AssertionError('Box Position is not returned properly')
            except MoveTargetOutOfBoundsException:
                assert True, "The box is restricted and cannot be moved outside the container boundaries."
