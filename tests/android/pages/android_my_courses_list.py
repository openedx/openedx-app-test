"""
    My Courses List Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class AndroidMyCoursesList(AndroidBasePage):
    """
    My Courses List screen
    """

    def get_my_course_toolbar_title(self):
        """
        Get toolbar title

        Returns:
            element: toolbar title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.my_course_toolbar_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_course_toolbar_title
        )

    def get_my_course_screen_title(self):
        """
        Get screen title

        Returns:
            element: screen title element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_course_screen_title
        )

    def get_my_courses_description(self):
        """
        Get course description title

        Returns:
            element: course description element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_courses_description
        )

    def get_my_courses_org_name(self):
        """
        Get course organization title

        Returns:
            element: course organization element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_courses_org_name
        )

    def get_my_courses_course_date(self):
        """
        Get course date title

        Returns:
            element: course date element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.my_courses_course_date
        )
