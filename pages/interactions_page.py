import random
import re
import time

import allure

from locators.interactions_locators import (
    SortablePageLocators, SelectablePageLocators, ResizablePageLocators,
    DroppablePageLocators, DraggablePageLocators
)
from pages.base_page import BasePage


class SortablePage(BasePage):
    """
    Page Object Model for the Sortable Page. Handles sorting of list and grid items.
    """

    locators = SortablePageLocators()

    @allure.step("Test get sortable items")
    def get_sortable_items(self, elements):
        """
        Retrieves all sortable items and returns their text values.

        Args:
            elements: Locator for the sortable items.

        Returns:
            list: A list of text values of sortable items.
        """
        item_list = self.every_visible_element(elements)
        return [item.text for item in item_list]

    @allure.step("Test change list order")
    def change_list_order(self):
        """
        Changes the order of items in the list by dragging and dropping them.

        Returns:
            tuple: The order of items before and after the change.
        """
        self.element_is_clickable(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_PANEL_ITEM)
        item_list = random.sample(self.every_visible_element(self.locators.LIST_PANEL_ITEM), k=2)
        select_item = item_list[0]
        replace_item = item_list[1]
        self.go_to_element(select_item)
        self.go_to_element(replace_item)
        self.action_drag_and_drop_to_element(select_item, replace_item)
        order_after = self.get_sortable_items(self.locators.LIST_PANEL_ITEM)
        return order_before, order_after

    @allure.step("Test change grid order")
    def change_grid_order(self):
        """
        Changes the order of items in the grid by dragging and dropping them.

        Returns:
            tuple: The order of grid items before and after the change.
        """
        self.visible_element(self.locators.TAB_GRID).click()
        self.go_to_element(self.visible_element(self.locators.GRID_PANEL_ITEM))
        order_before = self.get_sortable_items(self.locators.GRID_PANEL_ITEM)
        item_list = random.sample(self.every_visible_element(self.locators.GRID_PANEL_ITEM), k=2)
        select_item = item_list[0]
        replace_item = item_list[1]
        self.go_to_element(select_item)
        self.go_to_element(replace_item)
        self.action_drag_and_drop_to_element(select_item, replace_item)
        order_after = self.get_sortable_items(self.locators.GRID_PANEL_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    """
    Page Object Model for the Selectable Page. Handles selecting list and grid items.
    """

    locators = SelectablePageLocators()

    @allure.step("Test click selectable items")
    def click_selectable_item(self, elements):
        """
        Clicks a random selectable item from the list of provided elements.

        Args:
            elements: Locator for the selectable items.
        """
        item_list = self.every_visible_element(elements)
        item = random.choice(item_list)
        self.go_to_element(item)
        item.click()

    @allure.step("Test select list item")
    def select_list_item(self):
        """
        Selects a random item from the list and returns its text.

        Returns:
            str: The text of the active list item.
        """
        self.visible_element(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.visible_element(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    @allure.step("Test select grid item")
    def select_grid_item(self):
        """
        Selects a random item from the grid and returns its text.

        Returns:
            str: The text of the active grid item.
        """
        self.visible_element(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.visible_element(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    """
    Page Object Model for the Resizable Page. Handles resizing elements like boxes.
    """

    locators = ResizablePageLocators

    @allure.step("Test get pixels from offsets")
    def get_px_from_width_height(self, value_of_size):
        """
        Extracts width and height from the provided size string.

        Args:
            value_of_size (str): Style attribute containing width and height values.

        Returns:
            tuple: A tuple containing the width and height as strings.
        """
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    @allure.step("Get minimum and maximum sizes")
    def get_max_min_size(self, element):
        """
        Retrieves the style attribute of the given element to determine its size.

        Args:
            element: Locator for the element.

        Returns:
            str: The style attribute of the element.
        """
        size = self.element_present(element)
        size_value = size.get_attribute('style')
        return size_value

    @allure.step("Change size of the resizable box")
    def change_size_resizable_box(self):
        """
        Changes the size of the resizable box and returns the maximum and minimum sizes.

        Returns:
            tuple: A tuple containing the maximum and minimum size (width, height).
        """
        self.action_drag_and_drop_by_offset(self.element_present(self.locators.RESIZABLE_BOX_HANDLE), 150, 170)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_present(self.locators.RESIZABLE_BOX_HANDLE), 150, 110)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    @allure.step("Test change size resizable")
    def change_size_resizable(self):
        """
        Changes the size of a resizable element with random offsets and returns the max and min sizes.

        Returns:
            tuple: A tuple containing the maximum and minimum size (width, height).
        """
        width_offset = random.randint(1, 400)
        height_offset = random.randint(1, 400)
        self.action_drag_and_drop_by_offset(self.element_present(self.locators.RESIZABLE_HANDLE), width_offset,
                                            height_offset)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        width_offset = random.randint(1, 200)
        height_offset = random.randint(1, 200)
        self.action_drag_and_drop_by_offset(self.element_present(self.locators.RESIZABLE_HANDLE), width_offset,
                                            height_offset)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size


class DroppablePage(BasePage):
    """
    Page Object Model for the Droppable Page. Handles drag-and-drop interactions.
    """

    locators = DroppablePageLocators()

    @allure.step("Test drop simple")
    def drop_simple(self):
        """
        Performs a simple drag-and-drop action and returns the text of the drop area.

        Returns:
            str: The text of the drop area after the action.
        """
        drag_me = self.visible_element(self.locators.DRAG_ME_BOX)
        drop_here = self.visible_element(self.locators.DROP_HERE_BOX)
        self.action_drag_and_drop_to_element(drag_me, drop_here)
        return drop_here.text

    @allure.step("Test drop accept")
    def drop_accept(self):
        """
        Performs drag-and-drop with both acceptable and non-acceptable elements.

        Returns:
            tuple: A tuple containing the drop text when using non-acceptable and acceptable items.
        """
        self.visible_element(self.locators.ACCEPT_TAB).click()
        acceptable_box = self.visible_element(self.locators.ACCEPTABLE_BOX)
        not_acceptable_box = self.visible_element(self.locators.NOT_ACCEPTABLE_BOX)
        drop_here = self.visible_element(self.locators.DROP_HERE_ACCEPT_BOX)
        self.action_drag_and_drop_to_element(not_acceptable_box, drop_here)
        not_acceptable_text = drop_here.text
        self.action_drag_and_drop_to_element(acceptable_box, drop_here)
        drop_text_accept = drop_here.text
        return not_acceptable_text, drop_text_accept

    @allure.step("Test prevent propagation boxes")
    def drop_prevent_propagation(self):
        """
        Tests drag-and-drop behavior with prevent propagation elements.

        Returns:
            tuple: A tuple containing the text of the non-greedy, greedy inner, and outer boxes.
        """
        self.visible_element(self.locators.PREVENT_PROPOGATION_TAB).click()
        drag_me = self.visible_element(self.locators.DRAG_ME_PROP_TAB_BOX)
        not_greedy_box = self.visible_element(self.locators.OUTER_DROPPABLE_BOX_not_greedy)
        outer_greedy_box = self.visible_element(self.locators.OUTER_DROPPABLE_BOX_greedy)
        greedy_inner_box = self.visible_element(self.locators.INNER_DROPPABLE_BOX)
        self.action_drag_and_drop_to_element(drag_me, not_greedy_box)
        self.action_drag_and_drop_to_element(drag_me, greedy_inner_box)
        return not_greedy_box.text, greedy_inner_box.text, greedy_inner_box.text, outer_greedy_box.text

    @allure.step("Test reversion of the draggable box")
    def revert_draggable(self):
        """
        Tests the reversion behavior of draggable elements and returns their position.

        Returns:
            tuple: The position after the drop, after revert, and the drop area text.
        """
        self.element_present(self.locators.REVERT_DRAGGABLE_TAB).click()
        will_revert_box = self.element_present(self.locators.WILL_REVERT)
        not_revert_box = self.element_present(self.locators.NOT_REVERT_BOX)
        drop_here = self.element_present(self.locators.DROP_HERE_REVERT_BOX)
        self.action_drag_and_drop_to_element(will_revert_box, drop_here)
        position_after_drop = will_revert_box.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert_box.get_attribute('style')
        self.action_drag_and_drop_to_element(not_revert_box, drop_here)
        return position_after_drop, position_after_revert, drop_here.text


class DraggablePage(BasePage):
    """
    Page Object Model for the Draggable Page. Handles various drag-and-drop interactions.
    """

    locators = DraggablePageLocators()

    @allure.step("Test get positions of the element before and after")
    def get_before_and_after_positions(self, drag_element):
        """
        Retrieves the position of the element before and after dragging.

        Args:
            drag_element: The element to be dragged.

        Returns:
            tuple: The position before and after the drag action.
        """
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 100), random.randint(0, 90))
        before_position = drag_element.get_attribute('style')
        self.action_drag_and_drop_by_offset(drag_element, random.randint(0, 70), random.randint(0, 200))
        after_position = drag_element.get_attribute('style')
        return before_position, after_position

    @allure.step("Test simple drag box")
    def simple_drag_box(self):
        """
        Tests simple drag functionality on a box element.

        Returns:
            tuple: The position before and after dragging the box.
        """
        drag_me = self.visible_element(self.locators.DRAG_ME_BOX)
        before_position, after_position = self.get_before_and_after_positions(drag_me)
        return before_position, after_position

    @allure.step("Test get top position")
    def get_top_position(self, positions):
        """
        Extracts the top position from the element's style attribute.

        Args:
            positions (str): The style attribute containing the position.

        Returns:
            list: A list of digits representing the top position.
        """
        return re.findall(r'\d[0-9]|\d', positions.split(';')[2])

    @allure.step("Test get left position")
    def get_left_position(self, positions):
        """
        Extracts the left position from the element's style attribute.

        Args:
            positions (str): The style attribute containing the position.

        Returns:
            list: A list of digits representing the left position.
        """
        return re.findall(r'\d[0-9]|\d', positions.split(';')[1])

    @allure.step("Test restricted axis x")
    def axis_restricted_x(self):
        """
        Tests restricted axis drag along the x-axis.

        Returns:
            tuple: Lists representing the top and left positions before and after the drag action.
        """
        self.visible_element(self.locators.AXIS_RESTRICTED_TAB).click()
        only_x = self.visible_element(self.locators.ONLY_X_BOX)
        position_x = self.get_before_and_after_positions(only_x)
        top_x_before = self.get_top_position(position_x[0])
        top_x_after = self.get_top_position(position_x[1])
        left_x_before = self.get_left_position(position_x[0])
        left_x_after = self.get_left_position(position_x[1])
        return [top_x_before, top_x_after], [left_x_before, left_x_after]

    @allure.step("Test restricted axis y")
    def axis_restricted_y(self):
        """
        Tests restricted axis drag along the y-axis.

        Returns:
            tuple: Lists representing the top and left positions before and after the drag action.
        """
        only_y = self.visible_element(self.locators.ONLY_Y_BOX)
        position_y = self.get_before_and_after_positions(only_y)
        top_y_before = self.get_top_position(position_y[0])
        top_y_after = self.get_top_position(position_y[1])
        left_y_before = self.get_left_position(position_y[0])
        left_y_after = self.get_left_position(position_y[1])
        return [top_y_before, top_y_after], [left_y_before, left_y_after]

    @allure.step("Test restricted draggable")
    def restricted_draggable(self):
        """
        Tests container-restricted drag-and-drop functionality.

        Returns:
            str: The position of the box after dragging.
        """
        self.visible_element(self.locators.CONTAINER_RESTRICTED_TAB).click()
        within_box = self.visible_element(self.locators.CONTAINED_WITHIN_BOX)
        x_offset = random.randint(1000, 1000)
        y_offset = random.randint(1000, 1000)
        self.action_drag_and_drop_by_offset(within_box, x_offset, y_offset)
        box_position = within_box.get_attribute('style')
        return box_position
