"""
   Module covers iOS base page
"""
from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.common.enums.general_enums import IosClassViews


def find_all_views_on_screen(view_name: IosClassViews) -> Element:
    """"""
    return Element(AppiumBy.CLASS_NAME, f'XCUIElementType{view_name.value}').find_all()


class IosBasePage:
    """
    Base page for all iOS Pages
    """

    def __init__(self):
        self._back_button_navigation = Element(AppiumBy.ACCESSIBILITY_ID, 'back_button')
        self._notification_allow_button = Element(AppiumBy.ACCESSIBILITY_ID, 'Allow')
        self._screen_heading_title = Element(AppiumBy.ACCESSIBILITY_ID, 'title_text')
        self._navigation_bar_title = Element(AppiumBy.CLASS_NAME, 'XCUIElementTypeNavigationBar')

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
            webdriver element: Allow Element
        """

        return self._notification_allow_button

    @property
    def screen_heading_title(self):
        """
        Get heading title elements

        Returns:
            Webdriver element: screen heading title element
        """

        return self._screen_heading_title

    @property
    def navigation_bar_title(self):
        """
        Get discovery title

        Returns:
            webdriver element: discovery title element
        """

        return self._navigation_bar_title

    @staticmethod
    def find_all_views_on_screen(view_name: IosClassViews) -> Element:
        """"""
        return Element(AppiumBy.CLASS_NAME, f'XCUIElementType{view_name.value}').find_all()

    @staticmethod
    def find_by_text_on_screen(text: str) -> Element:
        """"""
        if text:
            return Element(AppiumBy.IOS_PREDICATE, f'label == "{text}"').find()
        raise ValueError('text cannot be empty')