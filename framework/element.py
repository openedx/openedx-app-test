from logging import Logger

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement as MobileWebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.common.enums import ElementAttribute, ScrollDirections
from tests.common.exceptions import NotFoundError
from tests.common.utils import normalize_string


class Element:
    def __init__(self, strategy: AppiumBy, locator: str):
        self.locator = (strategy, locator)
        self.element: MobileWebElement = None
        self.elements: list[MobileWebElement] = None
        self.use_existing = False

    @classmethod
    def set_driver(cls, driver: WebDriver):
        cls.__driver = driver

    @classmethod
    def set_logger(cls, logger: Logger):
        cls.__logger = logger

    def find(self, timeout=10, raise_exception=True) -> "Element":
        """Finds the required element.
        Arguments:
            timeout (int) : time to wait for element
            raise_exception (bool): True or False
        Returns:
            Element: Returns self
        """
        try:
            if not self.element:
                self.element = WebDriverWait(Element.__driver, timeout).until(
                    expected_conditions.visibility_of_element_located(self.locator)
                )
            return self
        except Exception as exception:
            if raise_exception:
                raise NotFoundError(
                    f"failed to find element {self.locator} with exception {exception}"
                )
            Element.__logger.info(
                f"failed to find element {self.locator} with exception {exception}"
            )

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
                Element.__logger.info(
                    f"found {len(elements)} elements matching {self.locator}"
                )

                self.elements = elements if elements else None
            return self

        except Exception as exception:
            if raise_exception:
                raise NotFoundError(
                    f"failed to find elements with locator: {self.locator} with exception {exception}"
                )
            Element.__logger.info(
                f"failed to find elements with locator: {self.locator} with exception {exception}"
            )

    def get_child_element(self, child_locator: "Element") -> "Element":
        """Get child elements from parent element
        Arguments:
            child_locator: Element instance initialized with child locator
        Returns:
            Element: Returns instance of Element class for child elements
        """
        try:
            child_locator.element = self.find().element.find_element(
                child_locator.locator
            )
            Element.__logger.info(f"found elements matching {child_locator.locator}")
            return child_locator

        except Exception as exception:
            Element.__logger.info(
                f"failed to find elements with locator: {self.locator} with exception {exception}"
            )
            raise NotFoundError(
                f"failed to find elements with locator: {self.locator} with exception {exception}"
            )

    def get_child_elements(self, child_locator: "Element") -> "Element":
        """Get child elements from parent element
        Arguments:
            child_locator: Element instance initialized with child locator
        Returns:
            Element: Returns instance of Element class for child elements
        """
        try:
            child_elements = self.find().element.find_elements(child_locator.locator)
            if len(child_elements) > 0:
                child_locator.elements = child_elements
                Element.__logger.info(
                    f"found {len(child_elements)} elements matching {child_locator.locator}"
                )
                return child_locator

            raise NotFoundError(f"failed to find elements with locator: {self.locator}")

        except Exception as exception:
            Element.__logger.info(
                f"failed to find elements with locator: {self.locator} with exception {exception}"
            )
            raise NotFoundError(
                f"failed to find elements with locator: {self.locator} with exception {exception}"
            )

    def __getitem__(self, index: int):
        """retrieve element at the given index
        Arguments:
            index (int): index of required element
        Returns:
            Element: Returns self
        """
        if 0 <= index < len(self.elements):
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

    def get_attribute(
        self, attribute=ElementAttribute.LABEL, timeout=10, raise_exception=True
    ) -> str:
        """Finds the required attribute from element
        Arguments:
            attribute (ElementAttribute) : attribute to get, defaults to Label
            raise_exception (bool): True or False
        Returns:
            str : mentioned property of the element
        """
        try:
            return normalize_string(self.find(timeout).element.get_attribute(attribute))
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
                raise NotFoundError(
                    f"failed to click element {self.locator} with exception {exception}"
                )
            Element.__logger.info(
                f"failed to click element {self.locator} with exception {exception}"
            )
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
                raise NotFoundError(
                    f"failed to send keys to element {self.locator} with exception {exception}"
                )
            Element.__logger.info(
                f"failed to send keys to element {self.locator} with exception {exception}"
            )
            return False

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
            self.find(timeout)
            return True
        except Exception as exception:
            if raise_exception:
                # Raise a NotFoundError if the element is not found and raise_exception is True
                raise NotFoundError(
                    f"Element with locator: {self.locator} not found with exception {exception}"
                )
            # Log the exception if the element does not exist
            Element.__logger.info(
                f"Element {self.locator} does not exist with exception {exception}"
            )
            return False

    def is_selected(self, timeout=10) -> bool:
        """
            Checks if element is selected
        Arguments:
            timeout (int) : time to wait for element
        """
        try:
            return self.find(timeout).element.is_selected()
        except Exception as exception:
            Element.__logger.info(
                f"element {self.locator} is not selected with exception {exception}"
            )
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
            Element.__logger.info(
                f"element {self.locator} is not clickable with exception {exception}"
            )
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
            Element.__logger.info(
                f"element {self.locator} is not enabled with exception {exception}"
            )
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
            Element.__logger.info(
                f"element {self.locator} is not enabled with exception {exception}"
            )
            return False

    def scroll_vertically_from_element(self):
        """Scroll from element"""

        screen_width = Element.__driver.get_window_size()["width"]
        screen_height = Element.__driver.get_window_size()["height"]
        element_x_position = self.find().element.location["x"]
        element_y_position = self.find().element.location["y"]

        Element.__logger.info(
            "screen width {} - screen height {} - element_x {} - "
            "element_y {} ".format(
                screen_width, screen_height, element_x_position, element_y_position
            )
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
    def press_keycode(code):
        """
            Presses the key code
        Arguments:
            code (int) : key code
        """
        Element.__driver.press_keycode(code)
        Element.__logger.info(f"pressed key code {code}")
