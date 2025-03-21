"""
    Course Dashboard Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidCourseDashboard(AndroidBasePage):
    """
    Course Dashboard screen
    """

    def __init__(self):
        super().__init__()
        self._course_progress_bar_view = Element(
            AppiumBy.CLASS_NAME, "android.widget.ProgressBar"
        )
        self._course_view = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("org.edx.mobile:id/view_pager")',
        )
        self._course_dashboard_videos_tab = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Videos")'
        )
        self._course_dashboard_discussions_tab = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Discussions")'
        )
        self._course_dashboard_more_tab = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("More")'
        )
        self._course_dashboard_dates_tab = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Dates")'
        )
        self._empty_state_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_empty_state_title")',
        )
        self._all_courses_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All Courses")'
        )
        self._all_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("All")'
        )
        self._in_progress_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("In Progress")'
        )
        self._completed_course = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Completed")'
        )
        self._expired_courses = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Expired")'
        )
        self._learn_online_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("How to Learn Online")'
        )
        self._course_dashboard_home_tab = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("Home")'
        )
        self._back_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("Back")'
        )
        self._my_courses_course_item = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("btn_course_item")',
        )
        self._my_courses_course_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_courses_description")'
        )


    @property
    def back_button(self) -> Element:
        """Back Button element
        Returns:
            Element: Back button element
        """
        return self._back_button

    @property
    def course_progress_bar_view(self) -> Element:
        """Course progress bar view element.

        Returns:
            Element: The course progress bar view element

        Get the course progress bar view element in the course dashboard screen.
        """
        return self._course_progress_bar_view

    @property
    def empty_state_title(self) -> Element:
        """empty state title
        Returns:
            Element: Empty state title element

        This element is visible when there are no courses available in the course dashboard screen.
        """
        return self._empty_state_title

    def all_progress_bar_views(self) -> Element:
        """Get all progress bar views

        Returns:
            Element: Element object containing a list of all progress bar views

        This method fetches all progress bar views in the course dashboard screen.
        """
        return self.course_progress_bar_view.find_all()

    @property
    def course_view(self) -> Element:
        """
        Returns:
            Element: The course view element from the list of elements.

        This property fetches the course view element, which is the second element in the list of
        elements found by _course_view.
        """
        return self._course_view.find_all()[1]

    def get_all_text_views_inside_course_view(self) -> Element:
        """Get all text views which are child of course view
        Returns:
            Element: Element object containing an attribute with list of all text views
        """
        return self.course_view.get_child_elements(self.text_view)

    @property
    def all_courses_label(self) -> Element:
        """Get all courses label
        Returns:
            Element: all courses label element
        """
        return self._all_courses_label

    @property
    def all_label(self) -> Element:
        """all label element
        Returns:
            Element: all label element
        """
        return self._all_label

    @property
    def in_progress(self) -> Element:
        """in progress text element
        Returns:
            Element: in progress text
        """
        return self._in_progress_text

    @property
    def completed_course(self) -> Element:
        """completed course element
        Returns:
            Element: completed course
        """
        return self._completed_course

    @property
    def expired_courses(self) -> Element:
        """Expired courses element
        Returns:
            Element: expired courses
        """
        return self._expired_courses

    @property
    def learn_online_label(self) -> Element:
        """learn online label
        Returns:
            Element: learn online label
        """
        return self._learn_online_text

    @property
    def my_courses_list(self) -> Element:
        """Get courses list

        Returns:
            Element: my courses list
        """

        self._my_courses_course_description.exists()

        return self._my_courses_course_item.find_all()

    @property
    def course_dashboard_home_tab(self) -> Element:
        """Get course dashboard home tab
        Returns:
            Element: course dashboard home tab
        """
        return self._course_dashboard_home_tab

    @property
    def course_dashboard_dates_tab(self) -> Element:
        """Get course dashboard dates tab
        Returns:
            Element: course dashboard dates tab
        """

        return self._course_dashboard_dates_tab

    @property
    def course_dashboard_videos_tab(self) -> Element:
        """Get course dashboard videos tab
        Returns:
            Element: course dashboard videos tab
        """

        return self._course_dashboard_videos_tab

    @property
    def course_dashboard_discussions_tab(self) -> Element:
        """Get course dashboard discussions tab
        Returns:
            Element: course dashboard discussions tab
        """

        return self._course_dashboard_discussions_tab

    @property
    def course_dashboard_more_tab(self) -> Element:
        """Get course dashboard more tab
        Returns:
            Element: course dashboard more tab
        """

        return self._course_dashboard_more_tab
