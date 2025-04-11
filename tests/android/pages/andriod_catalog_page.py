"""Discover/Catalog Page Module."""

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage
from tests.common import values
from appium.webdriver.common.appiumby import AppiumBy



class AndroidCatalogPage(AndroidBasePage):
    """A Class for handling Catalog Screen UI interactions."""

    def __init__(self):
        super().__init__()
        self._catalog_screen_toolbar_title = Element(AppiumBy.ANDROID_UIAUTOMATOR,
                                                     'new UiSelector().resourceId("txt_toolbar_title")')
        self._catalog_screen_heading_msg = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Build skills. Earn a certificate. Advance your career.")',
        )
        self._trending_marketing_tag = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Marketing")'
        )
        self._trending_python_tag = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Python")'
        )
        self._trending_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Trending")'
        )
        self._trending_excel_tag = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Excel")'
        )
        self._trending_data_science = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Data Sciences")'
        )
        self._search_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("pgn-searchfield-input-7")',
        )
        self._search_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("search-landing-search-submit")',
        )
        self._first_result = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("search-landing-product-result-0")',
        )
        self._discovery_enroll_main_element = Element(
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="enroll"]/android.view.View[1]/android.view.View',
        )
        self._enroll_button = Element(
            AppiumBy.XPATH, 'new UiSelector().description("Enroll")'
        )
        self._main_content = Element(
            AppiumBy.XPATH, 'new UiSelector().resourceId("main-content")'
        )
        self._discovery_search_breakcrumbs = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("breadcrumb")'
        )
        self._first_popular_course = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("subject-filter-0")',
        )
        self._second_popular_course = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("subject-filter-1")',
        )
        self._third_popular_course = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("subject-filter-2")',
        )
        self._course_carousel = Element(
            AppiumBy.XPATH,
            '//android.view.View[@resource-id="main-content"]/android.view.View[4]',
        )

        self._trending_tags = {
            values.DISCOVERY_TRENDING_COURSE_PYTHON: self._trending_python_tag,
            values.DISCOVERY_TRENDING_COURSE_MARKETING: self._trending_marketing_tag,
            values.DISCOVERY_TRENDING_LABEL: self._trending_label,
            values.DISCOVERY_TRENDING_COURSE_EXCEL: self._trending_excel_tag,
            values.DISCOVERY_TRENDING_COURSE_DATA: self._trending_data_science,
        }

    @property
    def course_carousel(self) -> Element:
        """course carousel
        Returns:
            Element: course carousel

        """
        return self._course_carousel

    @property
    def main_content(self) -> Element:
        """Main content
        Returns:
            Element: main content
        """
        return self._main_content

    @property
    def discovery_search_breakcrumbs(self) -> Element:
        """Discovery search breakcrumbs
        Returns:
            Element: discovery search breakcrumbs

        """
        return self._discovery_search_breakcrumbs

    @property
    def first_popular_course(self) -> Element:
        """First popular course

        Returns:
            Element: first popular course

        """
        return self._first_popular_course

    @property
    def second_popular_course(self) -> Element:
        """Second popular course

        Returns:
            Element: second popular course

        """
        return self._second_popular_course

    @property
    def third_popular_course(self) -> Element:
        """Third popular course
        Returns:
            Element: third popular course
        """
        return self._third_popular_course

    @property
    def catalog_screen_toolbar_title(self) -> Element:
        """
        catalog screen toolbar title
        """
        return self._catalog_screen_toolbar_title

    @property
    def catalog_screen_heading_msg(self) -> Element:
        """catalog screen heading message
        Returns:
            Element: catalog screen heading message
        """

        return self._catalog_screen_heading_msg

    def trending_tag(self, tag: str) -> Element:
        """catalog screen trending marketing tag
        Returns:
            Element: catalog screen trending marketing tag
        """

        return self._trending_tags.get(tag)

    @property
    def search_field(self) -> Element:
        """Search field
        Returns:
            Element: search field

        """
        return self._search_field

    @property
    def search_button(self) -> Element:
        """Search button
        Returns:
            Element: search button

        """
        return self._search_button

    @property
    def first_result(self) -> Element:
        """First result
        Returns:
            Element: first result

        """
        return self._first_result

    @property
    def discovery_enroll_main_element(self) -> Element:
        """discovery enroll main element
        Returns:
            Element: discovery enroll main element

        """
        return self._discovery_enroll_main_element

    @property
    def enroll_button(self) -> Element:
        """Enroll button
        Returns:
            Element: enroll button

        """
        return self._enroll_button
