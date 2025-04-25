"""
What's New Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidWhatsNew(AndroidBasePage):
    """
    What's New screen
    """

    def __init__(self):
        super().__init__()
        self._whats_new_msg_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_whats_new_title")',
        )
        self._whats_new_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_whats_new_description")',
        )
        self._whats_new_btn_next = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_next")')
        self._whats_new_done_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_done")')
        self._whats_new_close_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ib_close")')

    @property
    def get_close_button(self) -> Element:
        """
        Get close button

        Returns:
            Element: sign in description element
        """

        return self._whats_new_close_button

    @property
    def get_whats_new_msg_title(self) -> Element:
        """
        Get title

        Returns:
            Element: whats new title element
        """

        return self._whats_new_msg_title

    @property
    def get_whats_new_description(self) -> Element:
        """
        Get description

        Returns:
            Element: whats new description element
        """

        return self._whats_new_description.find()

    @property
    def next_btn(self) -> Element:
        """
        Get next button

        Returns:
            Element: next button element
        """

        return self._whats_new_btn_next

    @property
    def done_button(self) -> Element:
        """Get done button

        Returns:
            Element: done element
        """

        return self._whats_new_done_button

    def navigate_features(self):
        """Navigate between features

        Returns:
            Element: Done Element
        """

        self.next_btn.click()
        if self.done_button.exists(raise_exception=False):
            return self.done_button
        else:
            self.navigate_features()
            return self.done_button
