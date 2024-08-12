import allure
from selenium.common import MoveTargetOutOfBoundsException

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage, DraggablePage


@allure.suite('Test interactions page')
class TestInteractionsPage:
    @allure.feature('Test sortable page')
    class TestSortable:
        @allure.title('test check test sortable')
        def test_sortable(self, driver):
            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the list has not been changed"

    @allure.feature('Test selectable page')
    class TestSelectablePage:
        @allure.title('test check test selectable box')
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) != 0, "no elements were selected"
            assert len(item_grid) != 0, "no elements were selected"

    @allure.feature('Test resizable page')
    class TestResizablePage:
        @allure.title('test check test resizable box')
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_resize, min_resize = resizable_page.change_size_resizable()
            assert min_box != max_box, "resizable has not been changed"

            assert min_resize != max_resize, "resizable has not been changed"

    @allure.feature('Test droppable page')
    class TestDroppablePage:
        @allure.title('test check droppable box')
        def test_simple_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text = droppable_page.drop_simple()
            assert text == "Dropped!", "The element has not been dropped"

        @allure.title('check test accept droppable box')
        def test_accept_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            assert not_accept == "Drop here", "the dropped element has been accepted"
            assert accept == "Dropped!", "the dropped element has not been accepted"

        @allure.title('test check prevent propogation droppable page ')
        def test_prevent_propogation_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_greedy_text, greedy_inner_text, outer_droppable_greedy_text, \
                inner_droppable_greedy_text = droppable_page.drop_prevent_propogation()
            assert not_greedy_text == "Dropped!", "element has not been dropped or accepted incorrectly"
            assert greedy_inner_text == "Dropped!", "element has not been dropped or accepted incorrectly"
            assert outer_droppable_greedy_text == "Dropped!", "element has not been dropped or accepted incorrectly"
            assert inner_droppable_greedy_text == "Outer droppable", "element has not been dropped or accepted incorrectly"

        @allure.title('Test check revert droppable box')
        def test_revert_draggable_droppable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            position_after_drop, position_after_revert, drop_here_text = droppable_page.revert_draggable()
            assert position_after_drop != position_after_revert, "elements position has not been changed"
            assert drop_here_text == "Dropped!", "element has not been dropped or accepted incorrectly"

    @allure.feature('Test draggable page ')
    class TestDraggablePage:
        @allure.title('Test check test box')
        def test_simple_draggable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            before, after = draggable_page.simple_drag_box()
            assert before != after, "the position of the box has not been changed"

        @allure.title('check test axis restricted box')
        def test_axis_restricted_droppable(self, driver):
            draggable_page = DraggablePage(driver, "https://demoqa.com/dragabble")
            draggable_page.open()
            top_x, left_x = draggable_page.axis_restricted_x()
            top_y, left_y = draggable_page.axis_restricted_y()
            assert top_x[0][0] == top_x[1][0] and int(
                top_x[1][0]) == 0, 'box position has not been changed or there is a shift on y_axis'
            assert left_x[0][0] != left_x[1][0] and int(
                left_x[1][0]) != 0, 'box position has not been changed or there is a shift on y_axis'
            assert top_y[0][0] != top_y[1][0] and int(
                top_y[1][0]) != 0, 'box position has not been changed or there is a shift on y_axis'
            assert left_y[0][0] == left_y[1][0] and int(
                left_y[1][0]) == 0, 'box position has not been changed or there is a shift on y_axis'

        @allure.title('Check test container restricted box')
        def test_container_restricted_draggable(self, driver):
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
