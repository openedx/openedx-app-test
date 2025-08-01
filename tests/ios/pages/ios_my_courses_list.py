"""
My Courses List Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.ios.pages.ios_base_page import IosBasePage


class IosMyCoursesList(IosBasePage):
    """
    My Courses List screen
    """

    def __init__(self):
        super().__init__()
        self._all_courses_expired_label = Element(AppiumBy.ACCESSIBILITY_ID, "Expired")
        self._all_courses_in_progress_label = Element(AppiumBy.ACCESSIBILITY_ID, "In Progress")
        self._all_courses_completed_label = Element(AppiumBy.ACCESSIBILITY_ID, "Completed")
        self._all_courses_header_text = Element(AppiumBy.ACCESSIBILITY_ID, "all_courses_header_text")
        self._all_courses_label = Element(AppiumBy.ACCESSIBILITY_ID, "All")
        self._my_courses_welcomeback_text = Element(AppiumBy.ACCESSIBILITY_ID, "courses_welcomeback_text")
        self._my_course_name_text = Element(AppiumBy.NAME, "Infinity test course")
        self._my_course_org_text = Element(AppiumBy.NAME, "Infinity test course")
        self._my_course_image = Element(AppiumBy.ACCESSIBILITY_ID, "course_image")
        self._my_course_header_text = Element(AppiumBy.ACCESSIBILITY_ID, "courses_header_text")
        self._my_course_arrow_image = Element(AppiumBy.ACCESSIBILITY_ID, "course_item")
        self._courses_dropdown_menu = Element(AppiumBy.ACCESSIBILITY_ID, "dropdown_menu_text")
        self._course_demoX = Element(AppiumBy.ACCESSIBILITY_ID, "DemoX")

    @property
    def my_courses_header_text(self) -> Element:
        """
        Get header text

        Returns:
            webdriver element: header text element
        """

        return self._my_course_header_text

    @property
    def my_courses_welcome_back_text(self) -> Element:
        """
        Get welcome back text

        Returns:
            webdriver element: welcome back text element
        """

        return self._my_courses_welcomeback_text

    @property
    def get_my_course_image(self) -> Element:
        """
        Get course image

        Returns:
            webdriver element: course image element
        """

        return self._my_course_image

    @property
    def get_my_course_org_text(self) -> Element:
        """
        Get course org text

        Returns:
            webdriver element: course org text element
        """

        return self._my_course_org_text

    @property
    def get_my_course_name_text(self) -> Element:
        """
        Get course name text

        Returns:
            webdriver element: course name text element
        """

        return self._my_course_name_text

    @property
    def get_all_courses_header_text(self) -> Element:
        """
        Get all courses header text

        Returns:
            webdriver element: all courses header text element
        """

        return self._all_courses_header_text

    @property
    def get_all_courses_label(self) -> Element:
        """
        Get all courses label

        Returns:
            webdriver element: all courses label element
        """

        return self._all_courses_label

    @property
    def all_courses_in_progress_label(self) -> Element:
        """
        Get all courses in progress label element

        Returns:
            webdriver element: all courses in progress label element
        """

        return self._all_courses_in_progress_label

    @property
    def get_all_courses_completed_label(self) -> Element:
        """
        Get all courses completed label element

        Returns:
            webdriver element: all courses completed label element
        """

        return self._all_courses_completed_label

    @property
    def get_all_courses_expired_label(self) -> Element:
        """
        Get all courses expired label element

        Returns:
            webdriver element: all courses expired label element
        """

        return self._all_courses_expired_label

    @property
    def courses_dropdown_menu(self) -> Element:
        """
        Get courses dropdown menu element

        Returns:
            webdriver element: courses dropdown menu element
        """
        return self._courses_dropdown_menu

    @property
    def course_demoX(self) -> Element:
        """
        Get course demoX element

        Returns:
            webdriver element: course demoX element
        """
        return self._course_demoX
