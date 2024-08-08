from selenium.webdriver.common.by import By


class SortablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_PANEL_ITEM = (
        By.CSS_SELECTOR, "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']")

    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_PANEL_ITEM = (
        By.CSS_SELECTOR, "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']")


class SelectablePageLocators:
    TAB_LIST = (By.CSS_SELECTOR, "a[id='demo-tab-list']")
    LIST_ITEM = (
        By.CSS_SELECTOR, "ul[id='verticalListContainer'] li[class='mt-2 list-group-item list-group-item-action']")
    LIST_ITEM_ACTIVE = (
        By.CSS_SELECTOR,
        'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, "a[id='demo-tab-grid']")
    GRID_ITEM = (By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item list-group-item-action"]')
    GRID_ITEM_ACTIVE = (
        By.CSS_SELECTOR, 'div[id="gridContainer"]  li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, "div[class='constraint-area'] span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE_BOX = (By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")

    RESIZABLE_HANDLE = (
        By.CSS_SELECTOR, "div[id='resizable'] span[class='react-resizable-handle react-resizable-handle-se']")
    RESIZABLE = (By.CSS_SELECTOR, "div[id='resizable']")


class DroppablePageLocators:
    # Simple
    DRAG_ME_BOX = (By.CSS_SELECTOR, 'div[id="draggable"]')
    DROP_HERE_BOX = (By.CSS_SELECTOR, "div[id='droppable']")

    # Accept
    ACCEPT_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    ACCEPTABLE_BOX = (By.CSS_SELECTOR, "div[id='acceptable']")
    NOT_ACCEPTABLE_BOX = (By.CSS_SELECTOR, "div[id='notAcceptable']")
    DROP_HERE_ACCEPT_BOX = (By.CSS_SELECTOR, "div[id='acceptDropContainer'] div[id='droppable']")

    # Prevent Propogation
    PREVENT_PROPOGATION_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-preventPropogation']")
    OUTER_DROPPABLE_BOX_not_greedy = (By.CSS_SELECTOR, "div[id='notGreedyDropBox'] p:nth-child(1)")
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, "div[id='notGreedyInnerDropBox']")
    OUTER_DROPPABLE_BOX_greedy = (By.CSS_SELECTOR, "div[id='greedyDropBox'] p:nth-child(1)")
    INNER_DROPPABLE_BOX = (By.CSS_SELECTOR, "div[id='greedyDropBoxInner']")
    DRAG_ME_PROP_TAB_BOX = (By.CSS_SELECTOR, "div[id='ppDropContainer'] div[id='dragBox']")

    # Revert Draggable
    REVERT_DRAGGABLE_TAB = (By.CSS_SELECTOR, "a[id='droppableExample-tab-revertable']")
    NOT_REVERT_BOX = (By.CSS_SELECTOR, "div[id='notRevertable']")
    WILL_REVERT = (By.CSS_SELECTOR, "div[id='revertable']")
    DROP_HERE_REVERT_BOX = (By.CSS_SELECTOR, "div[id='revertableDropContainer'] div[id='droppable']")


class DraggablePageLocators:
    # Simple
    DRAG_ME_BOX = (By.CSS_SELECTOR, 'div[id="draggableExample-tabpane-simple"] div[id="dragBox"]')

    # Axis Restricted
    AXIS_RESTRICTED_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-axisRestriction"]')
    ONLY_X_BOX = (By.CSS_SELECTOR, 'div[id="restrictedX"]')
    ONLY_Y_BOX = (By.CSS_SELECTOR, 'div[id="restrictedY"]')

    # Container Restricted
    CONTAINER_RESTRICTED_TAB = (By.CSS_SELECTOR, 'a[id="draggableExample-tab-containerRestriction"]')
    CONTAINED_WITHIN_BOX = (
        By.CSS_SELECTOR, 'div[class="draggable ui-widget-content ui-draggable ui-draggable-handle"]')
    BOX_WRAPPER = (By.CSS_SELECTOR, 'div[id="containmentWrapper"]')
