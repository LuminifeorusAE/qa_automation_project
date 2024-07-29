from pages.interactions_page import InteractionsPage


class TestInteractionsPage:
    class TestSortable:

        def test_sortable(self, driver):
            sortable_page = InteractionsPage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            assert list_before != list_after, "the order of the list has not been changed"
            assert grid_before != grid_after, "the order of the list has not been changed"





