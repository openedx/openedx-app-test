"""Module Discovery search and trending tags"""

import allure
import pytest

from framework import Element, expect
from tests.android.pages.andriod_catalog_page import AndroidCatalogPage
from tests.android.pages.android_landing import AndroidLanding
from tests.common import values


@allure.epic("DISCOVERY")
@allure.feature("Search and trending tags")
@allure.story("user can find courses using search and treading tags")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_DISCOVERY
@pytest.mark.ANDROID_SMOKE
class TestAndroidDiscoverySearchAndTrendingTags:
    """Discovery screen: search and trending tags"""

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
        android_landing = AndroidLanding()

        with allure.step("Goto Discover page"):
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
            expect(android_landing.explore_all_courses_button).to_have(values.LANDING_EXPLORE_COURSES)
            android_landing.explore_all_courses_button.click()
            expect(android_landing.back_navigation_button).to_be_displayed()
            expect(catalog_page.catalog_screen_heading_msg, timeout=20).to_exist()

        with allure.step("verify search field and search button exists"):
            search_field = catalog_page.search_field
            expect(search_field, timeout=20).to_have(values.DISCOVERY_SEARCH_FIELD_HINT, "hint")
            expect(catalog_page.search_button).to_have(values.DISCOVERY_SEARCH_BUTTON)

        with allure.step("verify trending tags exist"):
            expect(catalog_page.trending_tag(values.DISCOVERY_TRENDING_LABEL)).to_exist()
            expect(catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_PYTHON)).to_exist()
            expect(catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_EXCEL)).to_exist()
            expect(catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_DATA)).to_exist()
            expect(catalog_page.trending_tag(values.DISCOVERY_TRENDING_COURSE_MARKETING)).to_exist()
