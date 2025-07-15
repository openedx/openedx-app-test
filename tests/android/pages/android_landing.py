"""
Landing Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidLanding(AndroidBasePage):
    """
    Landing screen
    """

    def __init__(self):
        super().__init__()
        self._landing_screen_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_screen_title")',
        )
        self._landing_search_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_search_label")',
        )
        self._landing_discovery_search = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_search")'
        )
        self._search_bar_placeholder_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_search_placeholder")'
        )
        self._landing_explore_courses_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_explore_all_courses")',
        )
        self._register_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_register")')
        self._register_button_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_register")'
        )
        self._signin_button_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_sign_in")')
        self._landing_signin_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_sign_in")'
        )
        self._back_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_back")')

    @property
    def get_search_label(self) -> Element:
        """Get search label

        Returns:
            Element: the Element object
        """

        return self._landing_search_label

    def search_using_landing_discovery_search(self, search_text: str):
        """search using landing discovery search
        Args:
            search_text (str): search text
        Returns:
            None
        """

        self._landing_discovery_search.click()
        self._landing_discovery_search.send_keys(search_text)
        Element.press_keycode(66)

    @property
    def discovery_search(self) -> Element:
        """
        Returns:
            Element: landing discovery search
        """
        return self._landing_discovery_search

    @property
    def search_bar_placeholder_text(self):
        """
        Returns:
            Element: search bar placeholder text element
        """
        return self._search_bar_placeholder_text

    @property
    def explore_all_courses_button(self) -> Element:
        """Get explore courses button

        Returns:
            Element: the Element object
        """

        return self._landing_explore_courses_button

    @property
    def register_button(self) -> Element:
        """Get register button

        Returns:
            Element: the Element object
        """

        return self._register_button

    @property
    def register_button_text(self) -> Element:
        """register button text element

        Returns:
            Element: the Element object
        """

        return self._register_button_text

    @property
    def signin_button_text(self) -> Element:
        """signin button text element

        Returns:
            Element: the Element object
        """

        return self._signin_button_text

    def load_register_screen(self):
        """Get register button

        Returns:
            Element: Register button element
        """

        return self._register_button.click()

    def load_signin_screen(self):
        """Get sign in button

        Returns:
            Element: Signin button element
        """

        return self._landing_signin_button.click()

    @property
    def signin_button(self) -> Element:
        """Get signin button

        Returns:
            Element: the Element object
        """

        return self._landing_signin_button

    @property
    def get_back_button(self) -> Element:
        """Get back button

        Returns:
            Element: Back button element
        """

        return self._back_button
