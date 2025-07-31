"""
Course Home Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.common.exceptions import NotFoundError
from tests.ios.pages.ios_base_page import IosBasePage


class IosCourseHomeTab(IosBasePage):
    """
    Course Home Tab screen
    """

    def __init__(self):
        super().__init__()
        self._finish_button = Element(AppiumBy.IOS_PREDICATE, 'label == "Finish"')
        self._next_button = Element(AppiumBy.IOS_PREDICATE, 'label == "Next"')
        self._previous_button = Element(AppiumBy.IOS_PREDICATE, 'label == "Prev"')
        self._module_name_selector = 'label == "{}"'

    def component_navigation(self, retries=5) -> Element:
        """
        Navigate between components

        Args:
            retries (int): Maximum number of retries to find the finish button.

        Returns:
            webdriver element: finish Element
        """
        if retries == 0:
            raise NotFoundError("Finish button not found after maximum retries")

        self.next_btn.click()

        if self.finish_button.exists():
            return self.finish_button
        else:
            return self.component_navigation(retries=retries - 1)

    @property
    def finish_button(self) -> Element:
        """
        Get finish button

        Returns:
            element: finish element
        """

        return self._finish_button

    @property
    def next_btn(self) -> Element:
        """
        Get next button

        Returns:
            element: next button element
        """

        return self._next_button

    @property
    def prev_btn(self) -> Element:
        """
        Get prev button

        Returns:
            element: prev button element
        """

        return self._previous_button

    def verify_modules_exists(self, module_name: str):
        """
        verify given module exists on discover page
        """

        Element(AppiumBy.IOS_PREDICATE, self._module_name_selector.format(module_name)).scroll_and_find()
