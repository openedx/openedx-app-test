"""discover page filter module"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.ios.pages.ios_discover_page import IosDiscoverPage


class DiscoverFilters(IosDiscoverPage):
    """discover page filter class"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DiscoverFilters, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._all_filters_heading_text = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "All filters"`]'
        )
        self._clear_all_button = Element(AppiumBy.ACCESSIBILITY_ID, "Clear all")
        self._apply_button = Element(AppiumBy.ACCESSIBILITY_ID, "Apply")
        self._close_button = Element(AppiumBy.ACCESSIBILITY_ID, "Close")
        self._subject_dropdown = Element(AppiumBy.ACCESSIBILITY_ID, "Subject")
        self._subject_option_maths = Element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeSwitch[`name == "Math"`]')

    @property
    def all_filters_heading_text(self) -> Element:
        """all filters heading text

        Returns:
            Element: all filters heading text element
        """
        return self._all_filters_heading_text

    @property
    def clear_all_button(self) -> Element:
        """clear all button

        Returns:
            Element: clear all button element
        """
        return self._clear_all_button

    @property
    def apply_button(self) -> Element:
        """apply button

        Returns:
            Element: apply button element
        """
        return self._apply_button

    @property
    def close_button(self) -> Element:
        """close button

        Returns:
            Element: close button element
        """
        return self._close_button

    @property
    def subject_dropdown(self) -> Element:
        """subject dropdown

        Returns:
            Element: subject dropdown element
        """
        return self._subject_dropdown

    @property
    def subject_option_maths(self) -> Element:
        """subject option

        Returns:
            Element: subject option element
        """
        return self._subject_option_maths
