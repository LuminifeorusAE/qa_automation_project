import random
import time

from locators.interactions_locators import InteractionsPageLocators
from pages.base_page import BasePage


class InteractionsPage(BasePage):
    locators = InteractionsPageLocators()

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





