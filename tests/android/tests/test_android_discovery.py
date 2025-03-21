"""
Discovery Test Module
"""

from time import sleep
from tests.common.enums.general_enums import ScrollDirections
from framework import expect
from framework.element import Element
from tests.android.pages.andriod_catalog_page import AndroidCatalogPage
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
from tests.common.globals import Globals


class TestAndroidDiscovery:
    """
    Discovery screen's Test Case
    """

    def test_start_discovery_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify discovery screen is loaded successfully
            Verify that the screen title is correct
            Verify that the explore courses button is displayed
            Verify that the explore courses button text is correct
            Verify that the back button is displayed
            Verify that the back button text is correct
            Verify that the discovery screen message is correct
        """

        setup_logging.info(f"Starting {TestAndroidDiscovery.__name__} Test Case")
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        catalog_page = AndroidCatalogPage()

        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
        expect(android_landing.get_explore_courses).to_have(values.LANDING_EXLPORE_COURSES)
        assert android_landing.get_explore_courses.click()
        expect(android_landing.back_navigation_button).to_be_displayed()
        expect(catalog_page.catalog_screen_heading_msg).to_have(values.DISCOVERY_SCREEN_TITLE)
        assert catalog_page.catalog_screen_heading_msg.exists()

    def test_discovery_search_and_trending(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify search field is displayed
            Verify search field hint text
            Verify search button is displayed
            Verify search button text
            Verify trending label is displayed
            Verify trending label text
            Verify python course is displayed
            Verify python course text
            Verify excel course is displayed
            Verify excel course text
            Verify data course is displayed
            Verify data course text
            Verify marketing course is displayed
            Verify marketing course text
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        catalog_page = AndroidCatalogPage()

        search_field = catalog_page.search_field
        expect(search_field).to_have(values.DISCOVERY_SEARCH_FIELD_HINT, "hint")
        expect(catalog_page.search_button).to_have(values.DISCOVERY_SEARCH_BUTTON)
        assert catalog_page.trending_tag(values.DISCOVERY_TRENDING_LABEL).exists()
        assert catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_PYTHON).exists()
        assert catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_EXCEL).exists()
        assert catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_DATA).exists()
        assert catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_MARKETING).exists()

    def test_discovery_popular_subjects(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify main content is displayed
            Verify main content text
            Verify search breadcrumb is displayed
            Verify search breadcrumb text
            Verify filter by popular courses is displayed
            Verify filter by popular courses text
            Verify first popular course is displayed
            Verify first popular course text
            Verify second popular course is displayed
            Verify second popular course text
            Verify third popular course is displayed
            Verify third popular course text
            Verify third popular course is clicked
            Verify results number is displayed
            Verify results number text
            Verify show results number is displayed
            Verify show results number text
            Verify show results number is clicked
            Verify pagination results is displayed
            Verify pagination results text
            Verify pagination text is displayed
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        catalog_page = AndroidCatalogPage()

        expect(catalog_page.main_content).to_have(values.DISCOVERY_MAIN_CONTENT)
        assert catalog_page.discovery_search_breakcrumbs.exists()
        assert catalog_page.find_by_text_on_screen(values.DISCOVERY_FILTER_BY_POPULAR_COURSES).exists()
        assert catalog_page.find_by_text_on_screen(values.DISCOVERY_SCREEN_MESSAGE).exists()
        expect(catalog_page.first_popular_course).to_have(
            values.DISCOVERY_FIRST_POPULAR_COURSE, ElementAttribute.CONTENT_DESC
        )
        expect(catalog_page.second_popular_course).to_have(
            values.DISCOVERY_SECOND_POPULAR_COURSE, ElementAttribute.CONTENT_DESC
        )
        catalog_page.course_carousel.swipe_horizontal_on_element(ScrollDirections.LEFT)
        expect(catalog_page.third_popular_course).to_have(
            values.DISCOVERY_POPULAR_MATH_COURSE, ElementAttribute.CONTENT_DESC
        )
        assert catalog_page.third_popular_course.click()
        sleep(10)
        assert catalog_page.find_by_text_on_screen(values.DISCOVERY_MATH_RESULTS).exists()
        show_results_number = catalog_page.find_by_text_on_screen(values.DISCOVERY_MATH_RESULTS_BUTTON)
        assert show_results_number.exists()
        assert show_results_number.click()
        assert catalog_page.find_by_text_on_screen(values.DISCOVERY_MATH_PAGINATION_RESULTS).exists()
        assert catalog_page.find_by_text_on_screen(values.DISCOVERY_PAGINATION_TEXT).exists()

    def test_login_from_discovery(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that the user is able to login from discovery screen
            Verify that the user is able to navigate to the discover tab
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        whats_new_page = AndroidWhatsNew()
        global_contents = Globals(setup_logging)

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features).to_have("Done")
            assert whats_new_page.done_button.click()

    def test_enroll_course_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify discover tab is loaded successfully
            Verify that the back button text is correct
            Verify that the discovery screen message is correct
            Verify that the search field is displayed
            Verify that the search field hint text is correct
            Verify that the search field is clickable
            Verify that the search field is filled with text
            Verify that the search result is displayed
            Verify that the search result text is correct
            Verify that the search result is clickable
        """

        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        main_dashboard_page = AndroidMainDashboard()
        catalog_page = AndroidCatalogPage()

        discover_tab = main_dashboard_page.discover_tab
        expect(discover_tab).to_have(values.DISCOVER_SCREEN_HEADING, ElementAttribute.CONTENT_DESC)
        expect(discover_tab).not_.to_be_selected()
        assert discover_tab.click()
        expect(discover_tab).to_be_selected()

        sleep(20)
        expect(catalog_page.text_toolbar_title).to_have(values.DISCOVERY_SCREEN_TITLE)
        assert catalog_page.catalog_screen_heading_msg.exists()
        assert catalog_page.catalog_screen_heading_msg.click()
        assert catalog_page.trending_tag(values.DISCOVERY_TRENDING_LABEL).exists()

        search_field = catalog_page.search_field
        expect(search_field).to_be_displayed()
        expect(search_field).to_be_clickable()
        expect(search_field).to_have(values.DISCOVERY_SEARCH_FIELD_HINT, "hint")
        assert search_field.click()
        assert search_field.send_keys("Demo X")
        assert catalog_page.search_button.click()
        sleep(10)
        result = catalog_page.first_result
        expect(result).to_have(values.DISCOVERY_DEMOX_COURSE)
        assert result.click()

    def test_search_course_in_discovery(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that the enrollment page is loaded successfully
            Verify that the enrollment date is displayed
            Verify that the enrollment date is clickable
            Verify that the enroll button is displayed
            Verify that the enroll button text is correct
            Verify that the enroll button is clickable
            Verify that the allow notifications button is displayed
            Verify that the allow notifications button text is correct
            Verify that the allow notifications button is clickable
            Verify that the home tab is displayed
            Verify that the home tab text is correct
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        catalog_page = AndroidCatalogPage()
        course_dashboard = AndroidCourseDashboard()
        sleep(5)
        enroll_main_element = catalog_page.discovery_enroll_main_element
        enrollment_date = enroll_main_element.get_child_element(catalog_page.text_view)
        expect(enrollment_date).to_have(r".+")
        assert enrollment_date.click()
        enroll_button = catalog_page.enroll_button
        expect(enroll_button).to_have("Enroll", ElementAttribute.CONTENT_DESC)
        assert enroll_button.click()
        if catalog_page.allow_notifications_button.exists():
            assert catalog_page.allow_notifications_button.click()
        expect(course_dashboard.course_dashboard_home_tab).to_have(values.COURSE_DASHBOARD_HOME_TAB)
