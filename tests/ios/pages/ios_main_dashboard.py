"""
Main Dashboard Page Module
"""

from framework import Element
from appium.webdriver.common.appiumby import AppiumBy
from tests.ios.pages.ios_base_page import IosBasePage


class IosMainDashboard(IosBasePage):
    """
    Main Dashboard screen
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IosMainDashboard, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._profile_tab = Element(AppiumBy.ACCESSIBILITY_ID, "Profile")
        self._main_dashboard_tab = Element(AppiumBy.ACCESSIBILITY_ID, "Dashboard")
        self._programs_tab = Element(AppiumBy.ACCESSIBILITY_ID, "Programs")
        self._learn_tab = Element(AppiumBy.ACCESSIBILITY_ID, "Learn")
        self._discover_tab = Element(AppiumBy.ACCESSIBILITY_ID, "Discover")
        self._discover_tab_selected = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Discover"`]'
        )
        self._close_button = Element(AppiumBy.ACCESSIBILITY_ID, "close_button")
        self._course_item_demoX = Element(AppiumBy.IOS_PREDICATE, 'name == "course_item" AND label == "DemoX"')
        self._course_name_demoX = Element(AppiumBy.ACCESSIBILITY_ID, "DemoX")
        self._tab_bar = Element(AppiumBy.ACCESSIBILITY_ID, "Tab Bar")

    @property
    def get_close_button(self) -> Element:
        """
        Get close button

        Returns:
            webdriver element: close Element
        """
        return self._close_button

    @property
    def main_dashboard_discover_tab(self) -> Element:
        """
        Get discover tab

        Returns:
            webdriver element: Discover tab element
        """

        return self._discover_tab

    @property
    def main_dashboard_discover_tab_selected(self) -> Element:
        """
        Get discover tab
        Returns:
            webdriver element: Discover tab element
        """

        return self._discover_tab_selected

    @property
    def learn_tab(self) -> Element:
        """
        Get learn tab

        Returns:
            Element: learn tab element
        """

        return self._learn_tab

    @property
    def get_main_dashboard_programs_tab(self) -> Element:
        """
        Get programs tab

        Returns:
            webdriver element: Programs tab element
        """

        return self._programs_tab

    @property
    def main_dashboard_tab(self) -> Element:
        """
        Get dashboard tab

        Returns:
            webdriver element: Dashboard tab element
        """

        return self._main_dashboard_tab

    @property
    def profile_tab(self) -> Element:
        """
        Get profile tab

        Returns:
            webdriver element: profile tab element
        """

        return self._profile_tab

    @property
    def course_item_demoX(self) -> Element:
        """
        Get course item DemoX

        Returns:
            webdriver element: course item DemoX element
        """
        return self._course_item_demoX

    @property
    def course_name_demoX(self) -> Element:
        """
        Get course name DemoX

        Returns:
            webdriver element: course name DemoX element
        """
        return self._course_name_demoX

    @property
    def tab_bar(self) -> Element:
        """
        tab bar

        Returns:
            Element: tab bar element
        """
        return self._tab_bar
