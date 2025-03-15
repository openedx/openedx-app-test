"""
    My Courses List Page Module
"""
from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidMyCoursesList(AndroidBasePage):
    """
    My Courses List screen
    """

    def __init__(self):
        super().__init__()
        self._my_course_screen_title = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_courses_title")')
        self._my_courses_description = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_courses_description")')
        self._my_courses_org_name = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_course_org")')
        self._my_courses_course_date = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_course_date")')

    def get_my_course_screen_title(self) -> Element:
        """Get screen title

        Returns:
            Element: screen title element
        """

        return self._my_course_screen_title

    def get_my_courses_description(self) -> Element:
        """Get course description title

        Returns:
            Element: course description element
        """

        return self._my_courses_description

    def get_my_courses_org_name(self):
        """Get course organization title

        Returns:
            Element: course organization element
        """

        return self._my_courses_org_name

    def get_my_courses_course_date(self):
        """Get course date title

        Returns:
            Element: course date element
        """

        return self._my_courses_course_date
