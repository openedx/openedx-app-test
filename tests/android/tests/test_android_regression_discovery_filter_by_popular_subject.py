"""
Discovery Test Module
"""

from time import sleep

import allure
import pytest

from tests.common.enums.general_enums import ScrollDirections
from framework import expect
from framework.element import Element
from tests.android.pages.andriod_catalog_page import AndroidCatalogPage
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
from tests.android.pages.android_landing import AndroidLanding


@allure.epic("DISCOVERY")
@allure.feature("Filters")
@allure.story("user can use filter results by popular subjects")
@allure.suite("ANDROID REGRESSION")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_DISCOVERY
@pytest.mark.ANDROID_REGRESSION
class TestAndroidDiscovery:
    """
    Discovery screen's Test Case
    """

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
        android_landing = AndroidLanding()

        with allure.step("Goto Discover page"):
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
            expect(android_landing.explore_all_courses_button).to_have(values.LANDING_EXPLORE_COURSES)
            android_landing.explore_all_courses_button.click()
            expect(android_landing.back_navigation_button).to_be_displayed()
            expect(catalog_page.catalog_screen_heading_msg, timeout=20).to_exist()

        catalog_page.search_button.wait_for_clickable()
        expect(catalog_page.find_by_text_on_screen(values.DISCOVERY_FILTER_BY_POPULAR_COURSES)).to_exist()
        expect(catalog_page.find_by_text_on_screen(values.DISCOVERY_SCREEN_MESSAGE)).to_exist()
        if catalog_page.find_by_text_on_screen(values.DISCOVERY_AI_CHAT_CLOSE_BUTTON, raise_error=False):
            catalog_page.find_by_text_on_screen(values.DISCOVERY_AI_CHAT_CLOSE_BUTTON).click()
        expect(catalog_page.first_popular_course).to_have(
            values.DISCOVERY_FIRST_POPULAR_COURSE, ElementAttribute.CONTENT_DESC
        )
        expect(catalog_page.second_popular_course).to_have(
            values.DISCOVERY_SECOND_POPULAR_COURSE, ElementAttribute.CONTENT_DESC
        )
        catalog_page.course_carousel.swipe_vertical_full_page(ScrollDirections.UP, start_y_pc=70, end_y_pc=30)
        assert catalog_page.second_popular_course.click()
        sleep(10)
        assert catalog_page.find_by_text_on_screen("All filters(1 selected)")
