"""
    Course Dashboard Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.appiumby import AppiumBy


class AndroidCourseDashboard(AndroidBasePage):
    """
    Course Dashbaord screen
    """

    def get_my_courses_list(self):
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

    def get_course_dashboard_home_tab(self):
        """
        Get course dashboard home tab
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.course_dashboard_home_tab
        )

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.course_dashboard_home_tab
        )

    def get_course_dashboard_dates_tab(self):
        """
        Get course dashboard dates tab
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.course_dashboard_dates_tab
        )

    def get_course_dashboard_videos_tab(self):
        """
        Get course dashboard videos tab
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.course_dashboard_videos_tab
        )

    def get_course_dashboard_discussions_tab(self):
        """
        Get course dashboard discussions tab
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.course_dashboard_discussions_tab
        )

    def get_course_dashboard_more_tab(self):
        """
        Get course dashboard more tab
        """

        return self.global_contents.get_element_by_text(
            self.driver,
            android_elements.course_dashboard_more_tab
        )

    def get_back_button(self):
        """
        Get course dashboard discussions tab
        """

        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'back')

    def get_allow_notifications_button(self):
        """
        Get Allow button

        Returns:
            webdriver element: Allow Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.permission_allow_button)

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.permission_allow_button)
