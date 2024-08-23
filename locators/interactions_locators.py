from selenium.webdriver.common.by import By


class SortablePageLocators:
    """
    Locators for the Sortable page elements.
    """

    # Locator for the 'List' tab.
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")

    # Locator for items within the 'List' tab.
    LIST_PANEL_ITEM = (
        By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")

    # Locator for the 'Grid' tab.
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")

    # Locator for items within the 'Grid' tab.
    GRID_PANEL_ITEM = (
        By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    """
    Locators for the Selectable page elements.
    """

    # Locator for the 'List' tab.
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")

    # Locator for items in the list.
    LIST_ITEM = (
        By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class='mt-2 list-group-item list-group-item-action']")

    # Locator for the active item in the list.
    LIST_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')

    # Locator for the 'Grid' tab.
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")

    # Locator for items in the grid.
    GRID_ITEM = (
        By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item list-group-item-action"]')

    # Locator for the active item in the grid.
    GRID_ITEM_ACTIVE = (
        By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    """
    Locators for the Resizable page elements.
    """

    # Locator for the handle of the resizable box with restrictions.
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']")

    # Locator for the resizable box with restrictions.
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")

    # Locator for the handle of the resizable element.
    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR, "div[id='resizable'] span[class='react-resizable-handle react-resizable-handle-se']")

    # Locator for the resizable element.
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")


class DroppablePageLocators:
    """
    Locators for the Droppable page elements.
    """

    # Simple Drop
    # Locator for the 'Drag me' box.
    DRAG_ME_BOX = (By.CSS_SELECTOR, 'div[id="draggable"]')

    # Locator for the drop target box.
    DROP_HERE_BOX = (By.CSS_SELECTOR, "div[id='droppable']")

    # Accept Drop
    # Locator for the 'Accept' tab.
    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")

    # Locator for the acceptable box that can be dropped.
    ACCEPTABLE_BOX = (By.CSS_SELECTOR, "div[id='acceptable']")

    # Locator for the box that cannot be dropped.
    NOT_ACCEPTABLE_BOX = (By.CSS_SELECTOR, "div[id='notAcceptable']")

    # Locator for the drop target box when accept conditions are met.
    DROP_HERE_ACCEPT_BOX = (By.CSS_SELECTOR, "div[id='acceptDropContainer'] div[id='droppable']")

    # Prevent Propagation Drop
    # Locator for the 'Prevent Propagation' tab.
    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")

    # Locator for the non-greedy outer droppable box.
    OUTER_DROPPABLE_BOX_not_greedy = (By.CSS_SELECTOR, "div[id='notGreedyDropBox'] p:nth-child(1)")

    # Locator for the non-greedy inner droppable box.
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']")

    # Locator for the greedy outer droppable box.
    OUTER_DROPPABLE_BOX_greedy = (By.CSS_SELECTOR, "div[id='greedyDropBox'] p:nth-child(1)")

    # Locator for the greedy inner droppable box.
    INNER_DROPPABLE_BOX = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']")

    # Locator for the draggable box within the prevention propagation tab.
    DRAG_ME_PROP_TAB_BOX = (By.CSS_SELECTOR, "div[id='ppDropContainer'] div[id='dragBox']")

    # Revert Draggable
    # Locator for the 'Revert Draggable' tab.
    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")

    # Locator for the box that will not revert after being dropped.
    NOT_REVERT_BOX = (By.CSS_SELECTOR, "div[id='notRevertable']")

    # Locator for the box that will revert after being dropped.
    WILL_REVERT = (By.CSS_SELECTOR, "div[id='revertable']")

    # Locator for the drop target box in the revert draggable scenario.
    DROP_HERE_REVERT_BOX = (By.CSS_SELECTOR, "div[id='revertableDropContainer'] div[id='droppable']")


class DraggablePageLocators:
    """
    Locators for the Draggable page elements.
    """

    # Simple Drag
    # Locator for the 'Drag me' box in the simple drag scenario.
    DRAG_ME_BOX = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')

    # Axis Restricted Drag
    # Locator for the 'Axis Restricted' tab.
    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')

    # Locator for the box that can only be dragged along the X-axis.
    ONLY_X_BOX = (By.CSS_SELECTOR, 'div[id="restrictedX"]')

    # Locator for the box that can only be dragged along the Y-axis.
    ONLY_Y_BOX = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    # Container Restricted Drag
    # Locator for the 'Container Restricted' tab.
    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-containerRestriction"]')

    # Locator for the box contained within a specific boundary.
    CONTAINED_WITHIN_BOX = (
        By.CSS_SELECTOR, 'div[class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')

    # Locator for the boundary wrapper containing the box.
    BOX_WRAPPER = (By.CSS_SELECTOR, 'div[id="containmentWrapper"]')
