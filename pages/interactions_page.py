import random
import time

from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
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

    def change_size_resizable_box(self): # "!!!change method to minimize the size of the box after maximizing using negative numbers !!!"

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
