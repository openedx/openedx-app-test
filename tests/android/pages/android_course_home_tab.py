"""
    Course Home Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidCourseHomeTab(AndroidBasePage):
    """
    Course Home Tab screen
    """

    def __init__(self):
        super().__init__()
        self._finish_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Finish")'
        )
        self._next_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Next")'
        )
        self._previous_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Prev")'
        )
        self._back_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Back")'
        )

    def component_navigation(self, retries=5) -> Element:
        """Navigate between components

        Args:
            retries (int): Maximum number of retries to find the finish button.

        Returns:
            Element: finish button Element
        """
        if retries == 0:
            raise Exception("Finish button not found after maximum retries")

        assert self.next_btn.click()

        if self.finish_button.exists():
            return self.finish_button
        else:
            return self.component_navigation(retries=retries - 1)

    @property
    def finish_button(self) -> Element:
        """Get finish button

        Returns:
            Element: finish element
        """

        return self._finish_button

    @property
    def next_btn(self) -> Element:
        """Get next button

        Returns:
            Element: next button element
        """

        return self._next_button

    @property
    def prev_btn(self) -> Element:
        """Get prev button

        Returns:
            Element: prev button element
        """

        return self._previous_button

    @property
    def back_button(self) -> Element:
        """Back Button
        Returns:
            Element: Back button element
        """
        return self._back_button
