"""Discover Screen Module"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.ios.pages.ios_base_page import IosBasePage


class IosDiscoverPage(IosBasePage):
    """discover page class"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IosDiscoverPage, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._all_filters_dropdown = Element(AppiumBy.ACCESSIBILITY_ID, "All filters")
        self._search_field = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField")
        self._search_button = Element(AppiumBy.ACCESSIBILITY_ID, "Search")
        self._results_for_text = Element(
            AppiumBy.IOS_PREDICATE, 'label CONTAINS "results for" AND type == "XCUIElementTypeStaticText"'
        )

    @property
    def all_filters_dropdown(self) -> Element:
        """all filters dropdown

        Returns:
            Element: all filters dropdown element
        """
        return self._all_filters_dropdown

    @property
    def search_field(self) -> Element:
        """search field

        Returns:
            Element: search field element
        """
        return self._search_field

    @property
    def search_button(self) -> Element:
        """search button

        Returns:
            Element: search button element
        """
        return self._search_button

    @property
    def results_for_text(self) -> Element:
        """results for text

        Returns:
            Element: results for text element
        """
        return self._results_for_text
