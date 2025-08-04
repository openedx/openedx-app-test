"""Discover Screen Module"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.common import values
from tests.common.enums.general_enums import Subjects, DiscoverSections
from tests.ios.pages.ios_base_page import IosBasePage


class IosDiscoverPage(IosBasePage):
    """discover page class"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IosDiscoverPage, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__()
        self._all_filters_dropdown = Element(AppiumBy.ACCESSIBILITY_ID, "All filters")
        self._all_filters_parent_locator = Element(AppiumBy.ACCESSIBILITY_ID, "filters")
        self._search_field = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeSearchField")
        self._search_button = Element(AppiumBy.ACCESSIBILITY_ID, "Search")
        self._results_for_text = Element(
            AppiumBy.IOS_PREDICATE, 'label CONTAINS "results for" AND type == "XCUIElementTypeStaticText"'
        )
        self._back_button = Element(AppiumBy.ACCESSIBILITY_ID, "Start")
        self._heading_title_part1 = Element(AppiumBy.ACCESSIBILITY_ID, "Build skills. Earn a certificate.")
        self._heading_title_part2 = Element(AppiumBy.ACCESSIBILITY_ID, "Advance your career.")
        self._trending_tag_label = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`name == "Trending"`][2]'
        )
        self._trending_tag_python = Element(AppiumBy.ACCESSIBILITY_ID, "Python")
        self._trending_tag_excel = Element(AppiumBy.ACCESSIBILITY_ID, "Excel")
        self._trending_tag_data_sciences = Element(AppiumBy.ACCESSIBILITY_ID, "Data Sciences")
        self._trending_tag_marketing = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Marketing"`]'
        )
        self._most_popular_programs = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Most popular programs"`]'
        )
        self._search_field_clear_button = Element(AppiumBy.ACCESSIBILITY_ID, "Clear your search query")
        self._discover_results_page_courses_heading = Element(AppiumBy.ACCESSIBILITY_ID, "Courses")
        self._popular_subjects_filter_section = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Filter by popular subjects"`]'
        )
        self._explore_courses_and_program_section = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Explore courses and programs"`]'
        )
        self._cs_subject = Element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeLink[`name == "Computer Science"`][1]')
        self._engineering_subject = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeLink[`name == "Engineering"`][1]'
        )
        self._programs_section = Element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`name == "Programs"`]')
        self._discover_results_page_clear_all_filters_button = Element(AppiumBy.ACCESSIBILITY_ID, "Clear all")
        self._edx_logo_image = Element(AppiumBy.ACCESSIBILITY_ID, "logo for edX")
        self._section_name_selector = '**/XCUIElementTypeStaticText[`value == "{}"`]'
        self._subject_name_keyword_selector = '**/XCUIElementTypeLink[`label CONTAINS "{}"`]'
        self._demox_course_name = Element(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeLink[`name == "DemoX"`]')

    @property
    def all_filters_dropdown(self) -> Element:
        """all filters dropdown

        Returns:
            Element: all filters dropdown element
        """
        return self._all_filters_dropdown

    @property
    def all_filters_parent_element(self) -> Element:
        """all filters dropdown

        Returns:
            Element: all filters dropdown element
        """
        return self._all_filters_parent_locator

    @property
    def search_field(self) -> Element:
        """search field

        Returns:
            Element: search field element
        """
        return self._search_field

    @property
    def search_button(self) -> Element:
        """search button

        Returns:
            Element: search button element
        """
        return self._search_button

    @property
    def results_for_text(self) -> Element:
        """results for text

        Returns:
            Element: results for text element
        """
        return self._results_for_text

    @property
    def back_button(self) -> Element:
        """
        Get discovery page back button

        Returns:
            Element: discovery back button element
        """

        return self._back_button

    @property
    def heading_title_part1(self) -> Element:
        """
        Get heading title

        Returns:
            Element: heading title element
        """
        return self._heading_title_part1

    @property
    def heading_title_part2(self) -> Element:
        """
        Get heading title

        Returns:
            Element: heading title element
        """
        return self._heading_title_part2

    @property
    def trending_tag_label(self) -> Element:
        """
        Get trending tag label

        Returns:
            Element: trending tag label element
        """
        return self._trending_tag_label

    @property
    def trending_tag_python(self) -> Element:
        """
        Get trending tag python

        Returns:
            Element: trending tag python element
        """
        return self._trending_tag_python

    @property
    def trending_tag_excel(self) -> Element:
        """
        Get trending tag excel

        Returns:
            Element: trending tag excel element
        """
        return self._trending_tag_excel

    @property
    def trending_tag_data_sciences(self) -> Element:
        """
        Get trending tag data sciences

        Returns:
            Element: trending tag data sciences element
        """
        return self._trending_tag_data_sciences

    @property
    def trending_tag_marketing(self) -> Element:
        """
        Get trending tag marketing

        Returns:
            Element: trending tag marketing element
        """
        return self._trending_tag_marketing

    @property
    def most_popular_programs(self) -> Element:
        """
        Get most popular programs

        Returns:
            Element: most popular programs element
        """
        return self._most_popular_programs

    @property
    def search_field_clear_button(self) -> Element:
        """
        Get search field clear button

        Returns:
            Element: search field clear button element
        """
        return self._search_field_clear_button

    @property
    def discover_results_page_courses_heading(self) -> Element:
        """
        Get discover results page courses heading

        Returns:
            Element: discover results page courses heading element
        """
        return self._discover_results_page_courses_heading

    @property
    def popular_subjects_filter_section(self) -> Element:
        """
        Get popular subjects filter section

        Returns:
            Element: popular subjects filter section element
        """
        return self._popular_subjects_filter_section

    @property
    def explore_courses_and_programs_section(self) -> Element:
        """
        Get explore courses and programs section
        Returns:
            Element: explore courses and programs section
        """
        return self._explore_courses_and_program_section

    @property
    def programs_section(self) -> Element:
        """
        Get programs section

        Returns:
            Element: programs section element
        """
        return self._programs_section

    @property
    def edx_logo_image(self) -> Element:
        """
        Get edx logo image

        Returns:
            Element: edx logo image element
        """
        return self._edx_logo_image

    @property
    def discover_results_page_clear_all_filters_button(self) -> Element:
        """
        Get discover results page clear all filters button

        Returns:
            Element: discover results page clear all filters button element
        """
        return self._discover_results_page_clear_all_filters_button

    @property
    def demox_course_name(self) -> Element:
        """
        demoX course name

        Returns:
            Element: DemoX course name element
        """
        return self._demox_course_name

    def scroll_horizontally_on_popular_subject_carousel(self):
        """
        Scroll horizontally on popular subject carousel

        Returns:
            Element: popular subject carousel element
        """
        cs_subject = self._cs_subject
        engineering_subject = self._engineering_subject
        x1, y1 = cs_subject.get_coordinates()
        x2, y2 = engineering_subject.get_coordinates()
        anchor_y = (y1 + y2) / 2
        end_x = 0.2 * x1
        Element.swipe_horizontal(x2, end_x, anchor_y)

    def verify_section_exists(self, section_name: DiscoverSections):
        """
        verify given section exists on discover page
        """

        Element(AppiumBy.IOS_CLASS_CHAIN, self._section_name_selector.format(section_name.value)).scroll_and_find()

    def verify_courses_are_related_to_subject(self, subject: Subjects = Subjects.MATH) -> None:
        """
        Verify that courses are related to maths

        Raises:
            AssertionError: If no courses related to maths are found
        """
        count = 0
        course_keyword_list = values.COURSE_KEYWORD_LIST.get(subject.value, [])
        for keyword in course_keyword_list:
            course_locator = Element(AppiumBy.IOS_CLASS_CHAIN, self._subject_name_keyword_selector.format(keyword))
            if course_locator.exists(raise_exception=False):
                count += 1

        if count < 1:
            raise AssertionError("No courses related to maths found in the search results.")

    def verify_search_results_with_keyword(self, keyword: str) -> None:
        """
        Verify search results with the given keyword

        Args:
            keyword (str): The keyword to verify in search results
        """
        course_keyword_locator = Element(AppiumBy.IOS_CLASS_CHAIN, self._subject_name_keyword_selector.format(keyword))
        if course_keyword_locator.find_all().count() < 1:
            raise AssertionError(f"No search results found for keyword: {keyword}")
