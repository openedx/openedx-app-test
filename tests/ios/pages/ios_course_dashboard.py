"""
    Course Dashboard Page Module
"""
from framework import Element
from tests.ios.pages.ios_base_page import IosBasePage
from appium.webdriver.common.appiumby import AppiumBy



class IosCourseDashboard(IosBasePage):
    """
    Course Dashboard screen
    """

    def __init__(self):
        super().__init__()
        self._my_courses_course_item =  Element(AppiumBy.ACCESSIBILITY_ID, 'course_item')
        self._course_dashboard_resources_tab = Element(AppiumBy.ACCESSIBILITY_ID, 'org.edx.mobile:id/resources')
        self._course_dashboard_course_tab = Element(AppiumBy.ACCESSIBILITY_ID, 'Home')
        self._course_dashboard_dates_tab = Element(AppiumBy.ACCESSIBILITY_ID, 'Dates')
        self._course_dashboard_videos_tab = Element(AppiumBy.ACCESSIBILITY_ID, 'Videos')
        self._course_dashboard_discussions_tab = Element(AppiumBy.ACCESSIBILITY_ID, 'Discussions')
        self._course_dashboard_more_tab = Element(AppiumBy.ACCESSIBILITY_ID, 'More')


    @property
    def my_courses_list(self) -> Element:
        """
        Get courses list

        Returns:
            element: my courses list
        """

        return self._my_courses_course_item

    @property
    def course_dashboard_resources_tab(self) -> Element:
        """
        Get course dashboard resources tab
        """

        return self._course_dashboard_resources_tab

    @property
    def course_dashboard_course_tab(self) -> Element:
        """
        Get course dashboard courses tab
        """

        return self._course_dashboard_course_tab

    @property
    def course_dashboard_dates_tab(self) -> Element:
        """
        Get course dashboard dates tab
        """

        return self._course_dashboard_dates_tab

    @property
    def course_dashboard_videos_tab(self) -> Element:
        """
        Get course dashboard videos tab
        """

        return self._course_dashboard_videos_tab

    @property
    def course_dashboard_discussions_tab(self) -> Element:
        """
        Get course dashboard discussions tab
        """

        return self._course_dashboard_discussions_tab

    @property
    def course_dashboard_more_tab(self) -> Element:
        """
        Get course dashboard more tab
        """

        return self._course_dashboard_more_tab
