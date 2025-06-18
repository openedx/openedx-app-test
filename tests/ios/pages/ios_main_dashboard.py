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
        self._close_button = Element(AppiumBy.ACCESSIBILITY_ID, "close_button")

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
    def get_main_dashboard_learn_tab(self) -> Element:
        """
        Get discover tab

        Returns:
            webdriver element: Discover tab element
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
