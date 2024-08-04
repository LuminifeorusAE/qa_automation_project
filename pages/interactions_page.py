import random
import time

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()

    def get_sortable_items(self, elements):
        item_list = self.every_visible_element(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        self.element_is_clickable(self.locators.TAB_LIST).click()
        order_before = self.get_sortable_items(self.locators.LIST_PANEL_ITEM)
        item_list = random.sample(self.every_visible_element(self.locators.LIST_PANEL_ITEM), k=2)
        select_item = item_list[0]
        replace_item = item_list[1]
        self.action_drag_and_drop_to_element(select_item, replace_item)
        order_after = self.get_sortable_items(self.locators.LIST_PANEL_ITEM)
        return order_before, order_after

    def change_grid_order(self):
        self.element_is_clickable(self.locators.TAB_GRID).click()
        order_before = self.get_sortable_items(self.locators.GRID_PANEL_ITEM)
        item_list = random.sample(self.every_visible_element(self.locators.GRID_PANEL_ITEM), k=2)
        select_item = item_list[0]
        replace_item = item_list[1]
        self.action_drag_and_drop_to_element(select_item, replace_item)
        order_after = self.get_sortable_items(self.locators.GRID_PANEL_ITEM)
        return order_before, order_after


class SelectablePage(BasePage):
    locators = SelectablePageLocators()

    def click_selectable_item(self, elements):
        item_list = self.every_visible_element(elements)
        random.sample(item_list, k=1)[0].click()

    def select_list_item(self):
        self.visible_element(self.locators.TAB_LIST).click()
        self.click_selectable_item(self.locators.LIST_ITEM)
        active_element = self.visible_element(self.locators.LIST_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        self.visible_element(self.locators.TAB_GRID).click()
        self.click_selectable_item(self.locators.GRID_ITEM)
        active_element = self.visible_element(self.locators.GRID_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators

    def get_px_from_width_height(self, value_of_size):
        width = value_of_size.split(';')[0].split(':')[1].replace(' ', '')
        height = value_of_size.split(';')[1].split(':')[1].replace(' ', '')
        return width, height

    def get_max_min_size(self, element):
        size = self.element_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(
            self):  # "!!!change method to minimize the size of the box after maximizing using negative numbers !!!"

        self.action_drag_and_drop_by_offset(self.element_present(self.locators.RESIZABLE_BOX_HANDLE),
                                            150, 170)

        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_present(self.locators.RESIZABLE_BOX_HANDLE), 150, 110)
        min_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, min_size

    def change_size_resizable(self):
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
    locators = DroppablePageLocators()

    def drop_simple(self):
        drag_me = self.visible_element(self.locators.DRAG_ME_BOX)
        drop_here = self.visible_element(self.locators.DROP_HERE_BOX)
        self.action_drag_and_drop_to_element(drag_me, drop_here)
        return drop_here.text

    def drop_accept(self):
        self.visible_element(self.locators.ACCEPT_TAB).click()
        acceptable_box = self.visible_element(self.locators.ACCEPTABLE_BOX)
        not_acceptable_box = self.visible_element(self.locators.NOT_ACCEPTABLE_BOX)
        drop_here = self.visible_element(self.locators.DROP_HERE_ACCEPT_BOX)
        self.action_drag_and_drop_to_element(not_acceptable_box, drop_here)
        not_acceptable_text = drop_here.text
        self.action_drag_and_drop_to_element(acceptable_box, drop_here)
        drop_text_accept = drop_here.text
        return not_acceptable_text, drop_text_accept

    def drop_prevent_propogation(self):
        self.visible_element(self.locators.PREVENT_PROPOGATION_TAB).click()

        drag_me = self.visible_element(self.locators.DRAG_ME_PROP_TAB_BOX)
        not_greedy_box = self.visible_element(self.locators.OUTER_DROPPABLE_BOX_not_greedy)
        outer_greedy_box = self.visible_element(self.locators.OUTER_DROPPABLE_BOX_greedy)
        greedy_inner_box = self.visible_element(self.locators.INNER_DROPPABLE_BOX)
        self.action_drag_and_drop_to_element(drag_me, not_greedy_box)
        self.action_drag_and_drop_to_element(drag_me, greedy_inner_box)

        return not_greedy_box.text, greedy_inner_box.text, greedy_inner_box.text, outer_greedy_box.text
    def revert_draggable(self):
        self.element_present(self.locators.REVERT_DRAGGABLE_TAB).click()
        will_revert_box = self.element_present(self.locators.WILL_REVERT)
        not_revert_box = self.element_present(self.locators.NOT_REVERT_BOX)
        drop_here = self.element_present(self.locators.DROP_HERE_REVERT_BOX)
        self.action_drag_and_drop_to_element(will_revert_box,drop_here)
        position_after_drop = will_revert_box.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert_box.get_attribute('style')
        self.action_drag_and_drop_to_element(not_revert_box,drop_here)
        return position_after_drop, position_after_revert, drop_here.text

