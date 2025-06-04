"""
Module covers iOS base page
"""

from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element, expect
from tests.common.enums.general_enums import IosClassViews


class IosBasePage:
    """
    Base page for all iOS Pages
    """

    def __init__(self):
        self._back_button_navigation = Element(AppiumBy.ACCESSIBILITY_ID, "back_button")
        self._notification_allow_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Allow'`]"
        )
        self._screen_heading_title = Element(AppiumBy.ACCESSIBILITY_ID, "title_text")
        self._navigation_bar_title = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeNavigationBar")
        self._snackbar_text_message = Element(AppiumBy.ACCESSIBILITY_ID, "snackbar_text")
        self._progress_bar = Element(AppiumBy.ACCESSIBILITY_ID, "progress_bar")
        self._picker_title_label = Element(AppiumBy.ACCESSIBILITY_ID, "picker_title_text")
        self._picker_search_textfield = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`name == "picker_search_textfield"`]'
        )
        self._static_text = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeStaticText")

    @property
    def static_text(self) -> Element:
        """
        Get static text element
        Returns:
            Element: static text element locator
        """
        return self._static_text

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

    @property
    def picker_title_text(self) -> Element:
        """
        picker title text

        Returns:
            Element: picker title text
        """

        return self._picker_title_label

    @property
    def option_picker_search_field(self) -> Element:
        """
        option picker search field

        Returns:
            Element: option picker search field
        """

        return self._picker_search_textfield

    def search_and_verify_option_exists(self, option: Enum):
        """
        Search and verify that a picker option exists

        Args:
            option: Any enum-like object with a .value attribute
        """

        self.option_picker_search_field.clear_and_type(option.value)
        option_element = Element(
            AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypePickerWheel[`value == "{option.value}"`]'
        )
        expect(option_element).to_exist()

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
    def find_by_text_on_screen(text: str, partial: bool = False) -> Element:
        """
        Find an element on the screen by its text

        Args:
            text (str): element text to search for
            partial (bool): whether to search for a partial match

        Returns:
            Element: found element
        """
        if text:
            locator = f'label == "{text}"'
            if partial:
                locator = f'label CONTAINS "{text}"'
            return Element(AppiumBy.IOS_PREDICATE, locator).find()
        raise ValueError("text cannot be empty")
