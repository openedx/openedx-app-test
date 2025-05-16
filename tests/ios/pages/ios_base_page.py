"""
Module covers iOS base page
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.common.enums.general_enums import IosClassViews


class IosBasePage:
    """
    Base page for all iOS Pages
    """

    def __init__(self):
        self._back_button_navigation = Element(AppiumBy.ACCESSIBILITY_ID, "back_button")
        self._notification_allow_button = Element(AppiumBy.ACCESSIBILITY_ID, "Allow")
        self._screen_heading_title = Element(AppiumBy.ACCESSIBILITY_ID, "title_text")
        self._navigation_bar_title = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeNavigationBar")
        self._snackbar_text_message = Element(AppiumBy.ACCESSIBILITY_ID, "snackbar_text")
        self._progress_bar = Element(AppiumBy.ACCESSIBILITY_ID, "progress_bar")

    @property
    def back_navigation_button(self) -> Element:
        """
        Get main dashboard back icon
        Returns:
            Element: back navigation button element locator
        """

        return self._back_button_navigation

    @property
    def allow_notifications_button(self) -> Element:
        """
        Get Allow button

        Returns:
            Element: Allow Element
        """

        return self._notification_allow_button

    @property
    def screen_heading_title(self):
        """
        Get heading title elements

        Returns:
            Element: screen heading title element
        """

        return self._screen_heading_title

    @property
    def navigation_bar_title(self):
        """
        Get discovery title

        Returns:
            Element: discovery title element
        """

        return self._navigation_bar_title

    @property
    def snackbar_text_message(self):
        """
        Get snackbar text message

        Returns:
            Element: snackbar text message element
        """

        return self._snackbar_text_message

    @property
    def progress_bar(self):
        """
        Get progress bar

        Returns:
            Element: progress bar element
        """

        return self._progress_bar

    @staticmethod
    def find_all_views_on_screen(view_name: IosClassViews) -> Element:
        """
        Find all views on the screen by their class name

        Args:
            view_name (IosClassViews): The class view to search for

        Returns:
            Element: An element representing the collection of all matching views
        """
        return Element(AppiumBy.CLASS_NAME, f"XCUIElementType{view_name.value}").find_all()

    @staticmethod
    def find_by_text_on_screen(text: str) -> Element:
        """
        Find an element on the screen by its text

        Args:
            text (str): element text to search for

        Returns:
            Element: found element
        """
        if text:
            return Element(AppiumBy.IOS_PREDICATE, f'label == "{text}"').find()
        raise ValueError("text cannot be empty")
