"""
    My Courses List Page Module
"""
from appium.webdriver.common.mobileby import MobileBy
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosMyCoursesList(IosBasePage):
    """
    My Courses List screen
    """

    def get_my_courses_header_text(self):
        """
        Get header text

        Returns:
            webdriver element: header text element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.my_courses_header_text
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.my_courses_header_text
        )

    def get_my_courses_welcomeback_text(self):
        """
        Get welcome back text

        Returns:
            webdriver element: welcome back text element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.my_courses_welcomeback_text
        )

    def get_my_course_image(self):
        """
        Get course image

        Returns:
            webdriver element: course image element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.my_course_image
        )

    def get_my_course_org_text(self):
        """
        Get course org text

        Returns:
            webdriver element: course org text element
        """

        return self.global_contents.get_element_by_name_ios(
            self.driver,
            ios_elements.my_course_org_text
        )

    def get_my_course_name_text(self):
        """
        Get course name text

        Returns:
            webdriver element: course name text element
        """

        return self.global_contents.get_element_by_name_ios(
            self.driver,
            ios_elements.my_course_name_text
        )

    def get_my_course_end_text(self):
        """
        Get course end text

        Returns:
            webdriver element: course end text element
        """

        all_text = self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_textviews
        )[5]

    def get_my_course_arrow_image(self):
        """
        Get course arrow image

        Returns:
            webdriver element: course arrow image element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.my_course_arrow_image
        )

    def get_my_course_item_list(self):
        """
        Get course item

        Returns:
            webdriver element: course item element
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.my_course_item_list
        )

    def get_all_buttons(self):
        """
        Get all buttons

        Returns:
            webdriver element: all buttons element
        """

        return self.global_contents.get_all_views_on_ios_screen(
            self.driver,
            ios_elements.all_buttons
        )

    def get_all_courses_header_text(self):
        """
        Get all courses header text

        Returns:
            webdriver element: all courses header text element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.all_courses_header_text
        )

    def get_all_courses_label(self):
        """
        Get all courses label

        Returns:
            webdriver element: all courses label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.all_courses_label
        )

    def get_all_courses_inprogress_label(self):
        """
        Get all courses in progress label element

        Returns:
            webdriver element: all courses in progress label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.all_courses_inprogress_label
        )

    def get_all_courses_completed_label(self):
        """
        Get all courses completed label element

        Returns:
            webdriver element: all courses completed label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.all_courses_completed_label
        )

    def get_all_courses_expired_label(self):
        """
        Get all courses expired label element

        Returns:
            webdriver element: all courses expired label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.all_courses_expired_label
        )
