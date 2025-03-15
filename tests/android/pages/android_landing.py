"""
    Landing Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webelement import WebElement as MobileWebElement

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from framework.element import Element
from tests.common.enums.attributes import ElementAttribute


class AndroidLanding(AndroidBasePage):
    """
    Landing screen
    """

    def __init__(self):
        super().__init__()
        self._landidng_screen_title = Element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("txt_screen_title")')
        self._landing_search_label = Element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("txt_search_label")')
        self._landing_discovery_search = Element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("tf_search")')
        self._landing_explore_courses_button = Element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("txt_explore_all_courses")')
        self._landing_register_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_register")')
        self._landing_signin_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_sign_in")')

    @property
    def get_search_label(self) -> 'Element':
        """
        Get search label

        Returns:
            Element: the Element object
        """

        return self._landing_search_label

    def seach_using_landing_discovery_seach(self, search_text: str):
        """
        search using landing discovery search
        """

        self._landing_discovery_search.click()
        self._landing_discovery_search.send_keys(search_text)
        Element.press_keycode(66)
        # self.driver.press_keycode(self.global_contents.android_enter_key)
        # search_result_title = self.global_contents.get_txt_toolbar_title(self.driver)
        # return search_result_title

    @property
    def discovery_search(self) -> Element:
        """"""
        return self._landing_discovery_search

    @property
    def get_explore_courses(self) -> 'Element':
        """
        Get explore courses button

        Returns:
            Element: the Element object
        """

        return self._landing_explore_courses_button

    @property
    def get_register_button(self) -> 'Element':
        """
        Get register button

        Returns:
            Element: the Element object
        """

        return self._landing_register_button

    def load_register_screen(self):
        """
        Get register button

        Returns:
            element: Register button element
        """

        return self._landing_register_button.click()

    def load_signin_screen(self):
        """
        Get sign in button

        Returns:
            element: Signin button element
        """

        return self._landing_signin_button.click()


    @property
    def signin_button(self) -> 'Element':
        """
        Get signin button

        Returns:
            Element: the Element object
        """

        return self._landing_signin_button

    def navigate_back_on_screen(self):
        """
        Navigate back on screen

        Returns:
            element: Back button element
        """

        # will update this method once we have a unique id on back button
        self.driver.back()
        self.driver.back()
        self.driver.back()

    def get_back_button(self):
        """
        Get back button

        Returns:
            element: Back button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.back_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.back_button
        )

