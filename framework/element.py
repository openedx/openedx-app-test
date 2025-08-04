"""
Module containing Element class representing web driver element
"""

from logging import Logger
from typing import Union

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement as MobileWebElement
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.common.enums import ElementAttribute, ScrollDirections
from tests.common.enums.general_enums import AppContext
from tests.common.exceptions import NotFoundError
from tests.common.utils import normalize_string


class Element:
    """
    A class representing an element in the application.

    It provides methods to perform actions on the element and to verify its state.
    """

    def __init__(self, strategy: str, locator: str):
        """
        Initializes an Element instance.

        Args:
            strategy (str): The strategy to use to find the element.
            locator (str): The locator to use to find the element.
        """
        self.locator = (strategy, locator)
        self.element: MobileWebElement = None
        self.elements: list[MobileWebElement] = None
        self._has_parent = False

    @classmethod
    def set_driver(cls, driver: WebDriver):
        cls.__driver = driver

    @classmethod
    def get_driver(cls) -> WebDriver:
        return cls.__driver

    @classmethod
    def set_logger(cls, logger: Logger):
        cls.__logger = logger

    def find(self, timeout=10, raise_exception=True) -> Union["Element", None]:
        """Finds the required element.
        Arguments:
            timeout (int) : time to wait for element in seconds
            raise_exception (bool): True or False
        Returns:
            Element: Returns self | None if not found and raise_exception is false
        """
        try:
            self.element = WebDriverWait(Element.__driver, timeout).until(
                expected_conditions.visibility_of_element_located(self.locator)
            )
            Element.__logger.info(f"found element matching {self.locator}")
            return self
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(f"failed to find element {self.locator} with exception {exception}")
            Element.__logger.info(f"failed to find element {self.locator} with exception {exception}")

    def find_all(self, timeout=10, raise_exception=True) -> "Element":
        """Finds all the required elements matching locator.
        Arguments:
            timeout (int) : time to wait for element
            raise_exception (bool): True or False
        Returns:
            Element: Returns self
        """
        try:
            if not self.elements:
                elements = WebDriverWait(Element.__driver, timeout).until(
                    expected_conditions.presence_of_all_elements_located(self.locator)
                )
                Element.__logger.info(f"found {len(elements)} elements matching {self.locator}")

                self.elements = elements if elements else None
            return self

        except Exception as exception:
            if raise_exception:
                raise NotFoundError(f"failed to find elements with locator: {self.locator} with exception {exception}")
            Element.__logger.info(f"failed to find elements with locator: {self.locator} with exception {exception}")

    def get_child_element(self, child_locator: "Element") -> "Element":
        """Get child elements from parent element
        Arguments:
            child_locator: Element instance initialized with child locator
        Returns:
            Element: Returns instance of Element class for child elements
        """
        try:
            child_locator.element = self.find().element.find_element(*child_locator.locator)
            child_locator._has_parent = True
            Element.__logger.info(f"found child element matching {child_locator.locator}")
            return child_locator

        except Exception as exception:
            Element.__logger.info(
                f"failed to find child element with locator: {child_locator.locator} with exception {exception}"
            )
            raise NotFoundError(
                f"failed to find child element with locator: {child_locator.locator} with exception {exception}"
            )

    def get_child_elements(self, child_locator: "Element") -> "Element":
        """Get child elements from parent element
        Arguments:
            child_locator: Element instance initialized with child locator
        Returns:
            Element: Returns instance of Element class for child elements
        """
        try:
            child_elements = self.find().element.find_elements(*child_locator.locator)
            if len(child_elements) > 0:
                child_locator.elements = child_elements
                child_locator._has_parent = True
                Element.__logger.info(f"found {len(child_elements)} elements matching {child_locator.locator}")
                return child_locator

            raise NotFoundError(f"failed to find elements with locator: {self.locator}")

        except Exception as exception:
            Element.__logger.info(f"failed to find elements with locator: {self.locator} with exception {exception}")
            raise NotFoundError(f"failed to find elements with locator: {self.locator} with exception {exception}")

    def __getitem__(self, index: int):
        """retrieve element at the given index
        Arguments:
            index (int): index of required element
        Returns:
            Element: Returns self
        """
        if 0 <= index < len(self.elements):
            if self._has_parent:
                self.element = self.elements[index]
            else:
                self.element = self.find_all().elements[index]
            return self
        else:
            raise NotFoundError(
                f"The index: {index} you are trying to access does not exists in list of len: {len(self.elements)}"
            )

    def count(self) -> int:
        """
        Returns the count of elements matching the given locator

        Returns:
            int: number of elements matching the given locator
        """
        return len(self.elements) if self.elements else 0

    def get_attribute(self, attribute=ElementAttribute.LABEL, timeout=10, raise_exception=True) -> str:
        """Finds the required attribute from element
        Arguments:
            attribute (ElementAttribute) : attribute to get, defaults to Label
            timeout (int): maximum time to wait for the element to be found
            raise_exception (bool): True or False
        Returns:
            str : mentioned property of the element
        """
        try:
            if self._has_parent:
                attribute = self.element.get_attribute(attribute)
                if attribute:
                    return normalize_string(attribute)
                raise NotFoundError("attribute not found")
            attribute = self.find(timeout).element.get_attribute(attribute)
            if attribute:
                return normalize_string(attribute)
            raise NotFoundError("attribute not found")
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(
                    f"failed to get attribute {attribute} for element {self.locator} with exception {exception}"
                )
            Element.__logger.info(
                f"failed to get attribute {attribute} for element {self.locator} with exception {exception}"
            )

    def click(self, timeout=10, raise_exception=True) -> bool:
        """
            Clicks the element
        Arguments:
            timeout (int) : time to wait for element
            raise_exception (bool): True or False
        Returns:
            bool: true of flase
        Raises:
            NotFoundError: If the user sets raise_exception arg to True and click fails
        """
        try:
            self.find(timeout).element.click()
            self.element = None
            return True
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(f"failed to click element {self.locator} with exception {exception}")
            Element.__logger.info(f"failed to click element {self.locator} with exception {exception}")
            return False

    def send_keys(self, *keys, timeout=10, raise_exception=True) -> bool:
        """
            Sends keys to element
        Arguments:
            keys (str) : keys to send
            timeout (int) : time to wait for element
            raise_exception (bool): True or False
        Returns:
            bool: true of false
        Raises:
            NotFoundError: If the user sets raise_exception arg to True and click fails
        """
        try:
            self.find(timeout).element.send_keys(*keys)
            return True
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(f"failed to send keys to element {self.locator} with exception {exception}")
            Element.__logger.info(f"failed to send keys to element {self.locator} with exception {exception}")
            return False

    def clear(self, timeout=10, raise_exception=True) -> bool:
        """
        Clears the text field element.
        Arguments:
            timeout (int): The time to wait for the element.
            raise_exception (bool): Whether to raise an exception if the element is not found.
        Returns:
            bool: True if the text field is cleared; False otherwise.
        Raises:
            NotFoundError: If raise_exception is True and the element is not found.
        """
        try:
            self.find(timeout).element.clear()
            return True
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(f"failed to clear text field for element {self.locator} with exception {exception}")
            Element.__logger.info(f"failed to clear text field for element {self.locator} with exception {exception}")
            return False

    def long_press(self, timeout=10, raise_exception=True) -> bool:
        """
        Long presses the element.
        Arguments:
            timeout (int): The time to wait for the element.
            raise_exception (bool): Whether to raise an exception if the element is not found.
        Returns:
            bool: True if the element is long pressed; False otherwise.
        Raises:
            NotFoundError: If raise_exception is True and the element is not found.
        """
        try:
            self.find(timeout)
            # Long press to select text
            actions = ActionChains(Element.__driver)
            touch = PointerInput(interaction.POINTER_TOUCH, "touch")
            actions.w3c_actions = ActionBuilder(Element.__driver, mouse=touch)

            loc = self.element.location
            size = self.element.size
            center_x = loc["x"] + size["width"] // 2
            center_y = loc["y"] + size["height"] // 2

            actions.w3c_actions.pointer_action.move_to_location(center_x, center_y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(1)  # 1 second long press
            actions.w3c_actions.pointer_action.pointer_up()
            actions.perform()
            return True
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(f"failed to long press element {self.locator} with exception {exception}")
            Element.__logger.info(f"failed to long press element {self.locator} with exception {exception}")
            return False

    def clear_and_type(self, value, timeout=10, raise_exception=True) -> None:
        """
        Clears the text field element and types the given value.
        Arguments:
            value (str): The value to type.
            timeout (int): The time to wait for the element.
            raise_exception (bool): Whether to raise an exception if the element is not found.
        Returns:
            bool: True if the text field is cleared and the value is typed; False otherwise.
        Raises:
            NotFoundError: If raise_exception is True and the element is not found.
        """

        self.find(timeout)
        platform = Element.__driver.capabilities["platformName"].lower()
        self.element.click()

        if platform == "android":
            # Select all text (CTRL + A) and delete (DEL)
            self.element.send_keys(Keys.CONTROL, "a")
            self.element.send_keys(Keys.DELETE)
        elif platform == "ios":
            # iOS does not support CTRL+A. So we can:
            # - Tap and hold to bring up select options
            # - Then clear the field by sending BACKSPACE repeatedly
            current_text = self.element.text

            if current_text:
                self.long_press(timeout, raise_exception)
                select_all_element = WebDriverWait(Element.__driver, timeout).until(
                    expected_conditions.visibility_of_element_located(
                        (AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeMenuItem[`name == 'Select All'`]")
                    )
                )
                select_all_element.click()
                self.element.send_keys(Keys.BACKSPACE)
        else:
            raise NotFoundError(f"Unsupported platform: {platform}")

        self.element.send_keys(value)

    def exists(self, timeout=10, raise_exception=True) -> bool:
        """
        Checks if the element is present in the DOM and has a size greater than zero.

        Arguments:
            timeout (int): The time to wait for the element.
            raise_exception (bool): Whether to raise an exception if the element is not found.

        Returns:
            bool: True if the element exists; False otherwise.

        Raises:
            NotFoundError: If raise_exception is True and the element is not found.
        """
        try:
            # Attempt to find the element within the specified timeout
            if self.find(timeout, raise_exception):
                Element.__logger.info(f"Element with {self.locator} found successfully")
                return True
            return False
        except Exception as exception:
            if raise_exception:
                # Raise a NotFoundError if the element is not found and raise_exception is True
                raise NotFoundError(f"Element with locator: {self.locator} not found with exception {exception}")
            # Log the exception if the element does not exist
            Element.__logger.info(f"Element {self.locator} does not exist with exception {exception}")
            return False

    def get_coordinates(self, timeout=10, raise_exception=True) -> tuple:
        """
        Returns the (x, y) coordinates of the element.

        Arguments:
            timeout (int): The time to wait for the element.
            raise_exception (bool): Whether to raise an exception if the element is not found.

        Returns:
            tuple: (x, y) coordinates of the element.

        Raises:
            NotFoundError: If raise_exception is True and the element is not found.
        """
        try:
            self.find(timeout, raise_exception)
            location = self.element.location
            return location["x"], location["y"]
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(f"failed to get coordinates for element {self.locator} with exception {exception}")
            Element.__logger.info(f"failed to get coordinates for element {self.locator} with exception {exception}")
            return None, None

    def is_selected(self, timeout=10) -> bool:
        """
            Checks if element is selected
        Arguments:
            timeout (int) : time to wait for element
        """
        try:
            return self.find(timeout).element.is_selected()
        except Exception as exception:
            Element.__logger.info(f"element {self.locator} is not selected with exception {exception}")
            return False

    def is_clickable(self, timeout=10) -> bool:
        """
            Checks if element is clickable
        Arguments:
            timeout (int) : time to wait for element
        """
        try:
            return self.get_attribute(ElementAttribute.CLICKABLE, timeout) == "true"
        except Exception as exception:
            Element.__logger.info(f"element {self.locator} is not clickable with exception {exception}")
            return False

    def is_enabled(self, timeout=10) -> bool:
        """
            Checks if element is enabled
        Arguments:
            timeout (int) : time to wait for element
        """
        try:
            return self.find(timeout).element.is_enabled()
        except Exception as exception:
            Element.__logger.info(f"element {self.locator} is not enabled with exception {exception}")
            return False

    def is_displayed(self, timeout=10) -> bool:
        """
            Checks if element is enabled
        Arguments:
            timeout (int) : time to wait for element
        """
        try:
            return self.find(timeout).element.is_displayed()
        except Exception as exception:
            Element.__logger.info(f"element {self.locator} is not displayed with exception {exception}")
            return False

    def is_checked(self, timeout=10) -> bool:
        """
            Checks if element is checked
        Arguments:
            timeout (int) : time to wait for element
        """
        try:
            return self.get_attribute(ElementAttribute.CHECKED, timeout) == "true"
        except Exception as exception:
            Element.__logger.info(f"element {self.locator} is not checked with exception {exception}")
            return False

    def wait_for_clickable(self, timeout=30, polling_time=0.5, raise_exception=True) -> "Element":
        """Finds the required element and waits for a given timeout until that element is clickable
        Arguments:
            timeout (int) : time to wait for element
            raise_exception (bool): True or False
        Returns:
            Element: Returns self
        """
        import time

        end_time = time.time() + timeout
        while time.time() < end_time:
            if self.is_clickable(timeout=5):
                return self
            time.sleep(polling_time)
        if raise_exception:
            raise NotFoundError(f"element {self.locator} is not clickable with in {timeout} seconds")

    def scroll_into_view_via_uiautomator(self, timeout=10, raise_exception=True) -> "Element":
        """Finds the required element and scrolls it into view
            only for android uiautomator style locators
        Arguments:
            timeout (int) : time to wait for element
            raise_exception (bool): True or False
        Returns:
            Element: Returns self
        """
        try:

            self.element = WebDriverWait(Element.__driver, timeout).until(
                expected_conditions.visibility_of_element_located(
                    (
                        self.locator[0],
                        f"new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView({self.locator[1]})",
                    )
                )
            )
            return self
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(
                    f"failed to find element"
                    f"({self.locator[0]},"
                    f" 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView({self.locator[1]})')"
                    f" with exception {exception}"
                )
            Element.__logger.info(f"failed to find element {self.locator} with exception {exception}")

    def scroll_and_find(
        self, timeout=10, tries=3, scroll_direction: ScrollDirections = ScrollDirections.UP
    ) -> "Element":
        """Scroll until element is visible
        Arguments:
            timeout (int) : time to wait for element
            tries (int): Number of times to scroll
            scroll_direction (str): Scroll direction
        Returns:
            Element: Returns self
        """

        for _ in range(tries):
            self.find(timeout=timeout, raise_exception=False)
            if self.element and self.is_displayed():
                return self
            self.swipe_vertical_full_page(scroll_direction, end_y_pc=40)

        if not self.element:
            raise NotFoundError(f"element {self.locator} not found after {tries} swipes")
        return self

    def scroll_vertically_from_element(self):
        """Scroll from element"""
        """
            Scroll from element

        Arguments:
            driver (webdriver element): webdriver instance variable
            from_element (webdriver element): element from which scroll will start
        """

        screen_width = Element.__driver.get_window_size()["width"]
        screen_height = Element.__driver.get_window_size()["height"]
        element_x_position = self.find().element.location["x"]
        element_y_position = self.find().element.location["y"]

        Element.__logger.info(
            "screen width {} - screen height {} - element_x {} - "
            "element_y {} ".format(screen_width, screen_height, element_x_position, element_y_position)
        )

        horizontal_start_point = int(element_x_position)
        vertical_start_point = int(element_y_position)
        horizontal_end_point = int(element_x_position)
        vertical_end_point = 0

        Element.__logger.info(
            "horizontal_start_point {} - vertical_start_point {} - horizontal_end_point {} "
            "- vertical_end_point {} ".format(
                horizontal_start_point,
                vertical_start_point,
                horizontal_end_point,
                vertical_end_point,
            )
        )

        Element.__driver.swipe(
            horizontal_start_point,
            vertical_start_point,
            horizontal_end_point,
            vertical_end_point,
            500,
        )
        self.element = None

    def swipe_horizontal_on_element(self, direction, swipe_percent=0.1):
        """Swipe from left to right or vice versa on a given element
        Arguments:
            direction (enums.ScrollDirections) : LEFT OR RIGHT
            swipe_percent (float) : device width in percentage
        Returns:
            None
        """
        self.find()
        element_width = self.element.size["width"]
        element_height = self.element.size["height"]

        swipe_width = element_width * swipe_percent
        offset_x = element_width * ((1 - swipe_percent) / 2)
        start_x = self.element.location["x"] + offset_x
        anchor_y = self.element.location["y"] + (element_height / 2)
        end_x = start_x + swipe_width

        if direction == ScrollDirections.LEFT:
            start_x, end_x = end_x, start_x

        Element.__driver.swipe(start_x, anchor_y, end_x, anchor_y, 300)

    @staticmethod
    def swipe_horizontal(start_x, end_x, anchor_y, duration=300):
        """
        Swipe horizontally on the screen.
        Arguments:
            start_x (int): Starting x-coordinate for the swipe.
            end_x (int): Ending x-coordinate for the swipe.
            anchor_y (int): y-coordinate to anchor the swipe.
            duration (int): Duration of the swipe in milliseconds.
        Returns:
            None
        """
        Element.__driver.swipe(start_x, anchor_y, end_x, anchor_y, duration)

    def wait_to_disappear(self, timeout=15, raise_exception=True) -> bool:
        """
        Waits until the element is not visible on the page

        Args:
            timeout (int): The time to wait for the element to disappear
            raise_exception (bool): Whether to raise a NotFoundError if the element is still present after the timeout
        Returns:
            bool: True if the element has disappeared, False if not
        """
        try:
            # Wait until the element is not visible on the page
            if WebDriverWait(Element.__driver, timeout).until_not(
                expected_conditions.visibility_of_element_located(self.locator)
            ):
                Element.__logger.info(f"Element with {self.locator} disappeared")
                return True
            return False
        except Exception as exception:
            # If the element is still present after the timeout, raise a NotFoundError if raise_exception is True
            if raise_exception:
                raise NotFoundError(
                    f"Element with locator: {self.locator} still present after "
                    f"{timeout} seconds. Exception: {exception}"
                )
            # Otherwise, just log the exception
            Element.__logger.info(
                f"Element with locator: {self.locator} still present after {timeout} seconds. Exception: {exception}"
            )
            return False

    @staticmethod
    def press_keycode(code):
        """
            Presses the key code
        Arguments:
            code (int) : key code
        """
        Element.__driver.press_keycode(code)
        Element.__logger.info(f"pressed key code {code}")

    @staticmethod
    def swipe_vertical_full_page(
        direction=ScrollDirections.UP,
        start_y_pc=80,
        end_y_pc=20,
        horizontal_anchor=0.5,
    ):
        """
            Swipe on page via given points
        Arguments:
            direction (Enum) : enums.ScrollDirections
            start_y_pc (int) : start screen percentage
            end_y_pc (int) : end screen percentage
            horizontal_anchor (float): ratio of screen with to be used as anchor point
        Returns:
            None
        """
        screen_coordinates = Element.__driver.get_window_size()
        screen_width = screen_coordinates.get("width")
        screen_height = screen_coordinates.get("height")
        x_anchor = int(screen_width * horizontal_anchor)

        if direction == ScrollDirections.UP:
            start_y = int((screen_height * (start_y_pc / 100)))
            end_y = int((screen_height * (end_y_pc / 100)))
        else:
            start_y = int((screen_height * (end_y_pc / 100)))
            end_y = int((screen_height * (start_y_pc / 100)))

        Element.__driver.swipe(x_anchor, start_y, x_anchor, end_y, 2500)

    @staticmethod
    def get_window_size() -> dict:
        """
        Get the size of the current window.

        Returns:
            dict: A dictionary containing the width and height of the window.
        """
        return Element.__driver.get_window_size()

    @staticmethod
    def switch_back_to_app():
        """Switch back to app"""
        Element.__driver.activate_app("org.edx.mobile")

    @staticmethod
    def switch_context(context_type: AppContext):
        """
        Switches the driver context to either 'NATIVE_APP' or a 'WEBVIEW' context.

        Args:
            context_type (str): 'native' to switch to native context, 'webview' to switch to webview context.

        Raises:
            NotFoundError: If the requested context is not found.
        """
        driver = Element.__driver
        available_contexts = driver.contexts
        Element.__logger.info(f"Available contexts: {available_contexts}")

        if context_type == AppContext.NATIVE:
            if "NATIVE_APP" in available_contexts:
                driver.switch_to.context("NATIVE_APP")
                Element.__logger.info("Switched to native context")
            else:
                raise NotFoundError("NATIVE_APP context not found")
        elif context_type == AppContext.WEBVIEW:
            webview_contexts = [c for c in available_contexts if c.startswith("WEBVIEW")]
            if webview_contexts:
                driver.switch_to.context(webview_contexts[0])
                Element.__logger.info(f"Switched to webview context: {webview_contexts[0]}")
            else:
                raise NotFoundError("WEBVIEW context not found")
        else:
            raise ValueError(f"context_type must be either '{AppContext.NATIVE}' or '{AppContext.WEBVIEW}'")
