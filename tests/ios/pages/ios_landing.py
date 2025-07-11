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
        self._landing_logo_image = Element(AppiumBy.ACCESSIBILITY_ID, "logo_image")
        self._landing_explore_search_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "explore_courses_textfield")
        self._landing_heading_text = Element(AppiumBy.ACCESSIBILITY_ID, "heading_text")
        self._landing_search_title = Element(AppiumBy.ACCESSIBILITY_ID, "search_title_text")
        self._landing_explore_all_courses = Element(AppiumBy.ACCESSIBILITY_ID, "explore_all_courses")
        self._landing_register = Element(AppiumBy.ACCESSIBILITY_ID, "register")
        self._landing_signin = Element(AppiumBy.ACCESSIBILITY_ID, "signin")
        self._landing_explore_courses_button = Element(AppiumBy.ACCESSIBILITY_ID, "explore_courses_button")
        self._signin_button = Element(AppiumBy.ACCESSIBILITY_ID, "logistration_signin_button")
        self._logistration_register_button = Element(AppiumBy.ACCESSIBILITY_ID, "logistration_register_button")
        self._landing_back_button = Element(AppiumBy.ACCESSIBILITY_ID, "Start")

    @property
    def get_logo_image(self) -> Element:
        """
        Get logo image

        Returns:
            webdriver element: logo image element
        """

        return self._landing_logo_image

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
    def landing_back_button(self) -> Element:
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

        self.landing_back_button.click()
        return self.get_logo_image

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
        """
        Get Sing In

        Returns:
            Element: Sign In Element
        """

        return self._signin_button

    @property
    def get_get_explore_courses_button(self) -> Element:
        """
        Get Explore Courses button

        Returns:
            webdriver element: Explore Courses Element
        """

        return self._landing_explore_courses_button
