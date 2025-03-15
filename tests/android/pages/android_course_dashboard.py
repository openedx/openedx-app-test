"""
    Course Dashboard Page Module
"""

from framework.element import Element
from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.appiumby import AppiumBy


class AndroidCourseDashboard(AndroidBasePage):
    """
    Course Dashbaord screen
    """

    def __init__(self):
        super().__init__()
        self._course_progress_bar_view = Element(AppiumBy.CLASS_NAME, 'android.widget.ProgressBar')
        self._course_view = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("org.edx.mobile:id/view_pager")')
        self._course_dashboard_videos_tab = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Videos")')
        self._course_dashboard_discussions_tab = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Discussions")')
        self._course_dashboard_more_tab = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("More")')
        self._course_dashboard_dates_tab = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Dates")')
        self._empty_state_title = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_empty_state_title")')
        self._all_courses_label = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All Courses")')
        self._all_label = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All")')
        self._in_progress_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("In Progress")')
        self._completed_course = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Completed")')
        self._expired_courses = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Expired")')
        self._learn_online_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("How to Learn Online")')
        self._course_dashboard_home_tab = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Home")')
        self._back_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Back")')

    @property
    def back_button(self) -> Element:
        """"""
        return self._back_button

    @property
    def course_progress_bar_view(self) -> Element:
        """
        course progress bar view element
        """
        return self._course_progress_bar_view

    @property
    def empty_state_title(self) -> Element:
        """
        course progress bar view element
        """
        return self._empty_state_title

    def all_progress_bar_views(self) -> Element:
        """"""
        return self.course_progress_bar_view.find_all()

    @property
    def course_view(self) -> Element:
        """
        """
        return self._course_view.find_all()[1]

    def get_all_text_views_inside_course_view(self) -> Element:
        """Get all text views which are child of course view
        """
        return self.course_view.get_child_elements(self.text_view)

    @property
    def all_courses_label(self) -> Element:
        """"""
        return self._all_courses_label

    @property
    def all_label(self)-> Element:
        """"""
        return self._all_label

    @property
    def in_progress(self) -> Element:
        """"""
        return self._in_progress_text

    @property
    def completed_course(self) -> Element:
        """"""
        return self._completed_course

    @property
    def expired_courses(self) -> Element:
        """"""
        return self._expired_courses

    @property
    def learn_online_label(self) -> Element:
        """"""
        return self._learn_online_text

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

    @property
    def course_dashboard_home_tab(self):
        """
        Get course dashboard home tab
        """
        return self._course_dashboard_home_tab

    @property
    def course_dashboard_dates_tab(self):
        """
        Get course dashboard dates tab
        """

        return self._course_dashboard_dates_tab

    @property
    def course_dashboard_videos_tab(self):
        """
        Get course dashboard videos tab
        """

        return self._course_dashboard_videos_tab

    @property
    def course_dashboard_discussions_tab(self):
        """
        Get course dashboard discussions tab
        """

        return self._course_dashboard_discussions_tab

    @property
    def course_dashboard_more_tab(self):
        """
        Get course dashboard more tab
        """

        return self._course_dashboard_more_tab
