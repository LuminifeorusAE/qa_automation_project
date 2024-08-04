import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


class TestInteractionsPage:
    class TestSortable:

        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the list has not been changed"

    class TestSelectablePage:

        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) != 0, "no elements were selected"
            assert len(item_grid) != 0, "no elements were selected"

    class TestResizablePage:

        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert min_box != max_box, "resizable has not been changed"

            assert min_resize != max_resize, "resizable has not been changed"

    class TestDroppablePage:
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "The element has not been dropped"

        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == "Drop here", "the dropped element has been accepted"
            assert accept == "Dropped!", "the dropped element has not been accepted"

        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy_text, greedy_inner_text, outer_droppable_greddy_text, \
            inner_droppable_greedy_text = droppable_page.drop_prevent_propogation()
            assert not_greedy_text == "Dropped!", "element has not been dropped or accepted incorectly"
            assert greedy_inner_text == "Dropped!", "element has not been dropped or accepted incorectly"
            assert outer_droppable_greddy_text == "Dropped!", "element has not been dropped or accepted incorectly"
            assert inner_droppable_greedy_text == "Outer droppable", "element has not been dropped or accepted incorectly"

        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            drop_here_revert_text = droppable_page.revert_draggable()
            assert drop_here_revert_text == "Dropped!", "element has not been dropped or accepted incorectly"
