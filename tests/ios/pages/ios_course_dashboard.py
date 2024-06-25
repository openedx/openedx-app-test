"""
    Course Dashboard Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosCourseDashboard(IosBasePage):
    """
    Course Dashboard screen
    """

    def get_my_courses_list(self):
        """
        Get courses list

        Returns:
            element: my courses list
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.my_courses_course_item
        )

        return self.global_contents.get_all_views_on_screen_by_id(
            self.driver,
            ios_elements.my_courses_course_item
        )

    def get_course_dashboard_resources_tab(self):
        """
        Get course dashboard resources tab
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.course_dashboard_resources_tab
        )

    def get_course_dashboard_course_tab(self):
        """
        Get course dashboard courses tab
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.course_dashboard_course_tab
        )

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.course_dashboard_course_tab
        )

    def get_course_dashboard_dates_tab(self):
        """
        Get course dashboard dates tab
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.course_dashboard_dates_tab
        )

    def get_course_dashboard_videos_tab(self):
        """
        Get course dashboard videos tab
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.course_dashboard_videos_tab
        )

    def get_course_dashboard_discussions_tab(self):
        """
        Get course dashboard discussions tab
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.course_dashboard_discussions_tab
        )

    def get_course_dashboard_more_tab(self):
        """
        Get course dashboard more tab
        """

        return self.global_contents.get_element_by_label_ios(
            self.driver,
            ios_elements.course_dashboard_more_tab
        )

    def navigate_to_main_dashboard_tab(self):
        """
        Get main dashboard back icon
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.back_button_navigation
        )
