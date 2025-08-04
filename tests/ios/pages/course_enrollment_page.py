"""
Course Enrollment module for iOS.
This module contains class and methods to interact with the course enrollment page.
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.ios.pages.ios_discover_page import IosDiscoverPage


class CourseEnrollmentPage(IosDiscoverPage):
    """
    Course Enrollment Page class for iOS.
    This class contains methods to interact with the course enrollment page.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IosDiscoverPage, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._edx_logo_image = Element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeImage[`name == "edX: DemoX"`]')
        self._demo_course_title = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "edX: DemoX"`]'
        )
        self._advance_your_career_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Advance your career"`][1]'
        )
        self._enrollment_page_back_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Discover"`]'
        )

    @property
    def enrollment_page_back_button(self) -> Element:
        """
        Get back button on course enrollment page

        Returns:
            Element: back button element
        """
        return self._enrollment_page_back_button

    @property
    def edx_logo_image(self) -> Element:
        """
        Get edx logo image on course enrollment page

        Returns:
            Element: edx logo image element
        """
        return self._edx_logo_image

    @property
    def demo_course_title(self) -> Element:
        """
        Get demo course title on course enrollment page

        Returns:
            Element: demo course title element
        """
        return self._demo_course_title

    @property
    def advance_your_career_button(self) -> Element:
        """
        Get advance your career button on course enrollment page

        Returns:
            Element: advance your career button element
        """
        return self._advance_your_career_button
