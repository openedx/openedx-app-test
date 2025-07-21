"""
New Landing Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.ios.pages.ios_base_page import IosBasePage


class IosLanding(IosBasePage):
    """
    New Landing screen
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IosLanding, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._edx_logo_image = Element(AppiumBy.ACCESSIBILITY_ID, "logo_image")
        self._landing_explore_search_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "explore_courses_textfield")
        self._landing_heading_text = Element(AppiumBy.ACCESSIBILITY_ID, "heading_text")
        self._landing_search_title = Element(AppiumBy.ACCESSIBILITY_ID, "search_title_text")
        self._landing_explore_all_courses = Element(AppiumBy.ACCESSIBILITY_ID, "explore_all_courses")
        self._landing_register = Element(AppiumBy.ACCESSIBILITY_ID, "register")
        self._landing_signin = Element(AppiumBy.ACCESSIBILITY_ID, "signin")
        self._explore_courses_button = Element(AppiumBy.ACCESSIBILITY_ID, "explore_courses_button")
        self._signin_button = Element(AppiumBy.ACCESSIBILITY_ID, "logistration_signin_button")
        self._logistration_register_button = Element(AppiumBy.ACCESSIBILITY_ID, "logistration_register_button")
        self._landing_back_button = Element(AppiumBy.ACCESSIBILITY_ID, "Start")
        self._search_magnifying_glass_icon = Element(AppiumBy.ACCESSIBILITY_ID, "magnifyingglass")

    @property
    def edx_logo_image(self) -> Element:
        """
        Get logo image

        Returns:
            webdriver element: logo image element
        """

        return self._edx_logo_image

    @property
    def search_courses_field(self) -> Element:
        """
        Get search courses field

        Returns:
            Element: search courses field element
        """

        return self._landing_explore_search_textfield

    @property
    def welcome_message(self):
        """
        Get welcome message

        Returns:
            webdriver element: welcome message element
        """

        return self._landing_heading_text

    @property
    def get_search_title(self):
        """
        Get search title

        Returns:
            webdriver element: search title element
        """

        return self._landing_search_title

    @property
    def discover_page_back_button(self) -> Element:
        """
        Get discovery title

        Returns:
            webdriver element: discovery title element
        """

        return self._landing_back_button

    @property
    def go_back_to_landing_screen(self):
        """
        Get discovery screen

        Returns:
            webdriver element: discovery title element
        """

        return self.discover_page_back_button.click()

    @property
    def register_button(self):
        """
        Get register button

        Returns:
            webdriver element: register button element
        """

        return self._logistration_register_button

    @property
    def sign_in_button(self) -> Element:
        """sign in button

        Returns:
            Element: Sign In button Element
        """

        return self._signin_button

    @property
    def explore_all_courses_button(self) -> Element:
        """Explore all courses button

        Returns:
            Element: Explore all courses button Element
        """

        return self._explore_courses_button

    @property
    def search_magnifying_glass_icon(self) -> Element:
        """Search magnifying glass icon

        Returns:
            Element: Search magnifying glass icon Element
        """

        return self._search_magnifying_glass_icon
