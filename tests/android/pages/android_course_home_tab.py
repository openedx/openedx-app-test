"""
Course Home Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage
from tests.common.exceptions import NotFoundError


class AndroidCourseHomeTab(AndroidBasePage):
    """
    Course Home Tab screen
    """

    def __init__(self):
        super().__init__()
        self._finish_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Finish")')
        self._next_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Next")')
        self._previous_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Prev")')
        self._back_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Back")')
        self._close_missed_deadline_msg_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Cancel")'
        )
        self._module_name_selector = 'new UiSelector().text("{}")'
        self._download_course_section_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Download course section").instance(0)'
        )
        self._stop_download_course_section_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Stop downloading course section")'
        )
        self._remove_downloaded_course_section_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Remove course section")'
        )
        self._course_component_bottom_nav_bar = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.edx.mobile:id/cv_navigationBar")'
        )

    @property
    def download_course_section_button(self) -> Element:
        """Get Download Course Section button

        Returns:
            Element: Download course section button element
        """
        return self._download_course_section_button

    @property
    def stop_download_course_section_button(self) -> Element:
        """Get Stop Download Course Section button

        Returns:
            Element: Stop Download course section button element
        """
        return self._stop_download_course_section_button

    @property
    def remove_downloaded_course_section_button(self) -> Element:
        """Get Remove Downloaded Course Section button

        Returns:
            Element: Remove Downloaded course section button element
        """
        return self._remove_downloaded_course_section_button

    def navigate_components_until_last_screen_is_reached(self, retries=6) -> Element:
        """Navigate between components

        Args:
            retries (int): Maximum number of retries to find the finish button.

        Returns:
            Element: finish button Element
        """
        if retries == 0:
            raise NotFoundError("Finish button not found after maximum retries")

        self.course_component_bottom_nav_bar.get_child_element(self.next_btn).click()

        self.android_loading_circle.wait_to_disappear(20)
        finish_btn = self.course_component_bottom_nav_bar.get_child_element(self.finish_button, raise_exception=False)
        if finish_btn.exists():
            return finish_btn
        else:
            return self.navigate_components_until_last_screen_is_reached(retries=retries - 1)

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

    @property
    def close_missed_deadline_msg_button(self) -> Element:
        """Close Missed Deadline Message Button

        Returns:
            Element: Close button element
        """
        return self._close_missed_deadline_msg_button

    @property
    def course_component_bottom_nav_bar(self) -> Element:
        """Course component bottom nav bar

        Returns:
            Element: Course component bottom nav bar element
        """
        return self._course_component_bottom_nav_bar

    def verify_modules_exists(self, module_name: str):
        """verify given module exists on discover page"""

        Element(AppiumBy.ANDROID_UIAUTOMATOR, self._module_name_selector.format(module_name)).scroll_and_find()
