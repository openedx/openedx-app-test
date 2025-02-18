"""
    Course Home Page Module
"""

from tests.ios.pages.ios_base_page import IosBasePage
from tests.common import values
from selenium.common.exceptions import NoSuchElementException


class IosCourseHomeTab(IosBasePage):
    """
    Course Home Tab screen
    """

    def component_navigation(self, retries=5):
        """
        Navigate between components

        Args:
            retries (int): Maximum number of retries to find the finish button.

        Returns:
            webdriver element: finish Element
        """
        if retries == 0:
            raise Exception("Finish button not found after maximum retries")

        self.get_next_btn().click()

        if self.get_finish_button():
            return self.get_finish_button()
        else:
            return self.component_navigation(retries=retries - 1)

    def get_finish_button(self):
        """
        Get finish button

        Returns:
            element: finish element
        """

        try:
            return self.global_contents.get_element_by_label_ios(
                self.driver, values.COURSE_COMPONENT_FINISH_BUTTON)
        except NoSuchElementException:
            return

    def get_next_btn(self):
        """
        Get next button

        Returns:
            element: next button element
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver, values.COURSE_COMPONENT_NEXT_BUTTON)

    def get_prev_btn(self):
        """
        Get prev button

        Returns:
            element: prev button element
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver, values.COURSE_COMPONENT_PREVIOUS_BUTTON)
