"""
    Course Dashboard Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class AndroidCourseDashboard(AndroidBasePage):
    """
    Course Dashbaord screen
    """

    def get_my_courses_list(self, driver):
        """
        Get courses list

        Returns:
            element: my courses list
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.my_courses_description
        )

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            android_elements.my_courses_course_item
        )

    def get_course_dashboard_resources_tab(self):
        """
        Get course dashboard resources tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_resources_tab
        )

    def get_course_dashboard_course_tab(self):
        """
        Get course dashboard courses tab
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_course_tab
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_course_tab
        )

    def get_course_dashboard_dates_tab(self):
        """
        Get course dashboard dates tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_dates_tab
        )

    def get_course_dashboard_videos_tab(self):
        """
        Get course dashboard videos tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_videos_tab
        )

    def get_course_dashboard_discussions_tab(self):
        """
        Get course dashboard discussions tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.course_dashboard_discussions_tab
        )

    def get_back_button(self):
        """
        Get course dashboard discussions tab
        """

        return self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'back')
