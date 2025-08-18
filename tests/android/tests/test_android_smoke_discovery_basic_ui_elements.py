"""Module Discovery Basic UI"""

import allure
import pytest

from framework import Element, expect
from tests.android.pages.andriod_catalog_page import AndroidCatalogPage
from tests.android.pages.android_landing import AndroidLanding
from tests.common import values


@allure.epic("DISCOVERY")
@allure.feature("Discover Page")
@allure.story("user can interact and view basic elements of discover page")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_DISCOVERY
@pytest.mark.ANDROID_SMOKE
class TestAndroidDiscoveryBasicUiElements:
    """Discovery screen basic UI Elements"""

    def test_android_smoke_discovery_basic_ui_elements(self, set_capabilities, setup_logging):
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

        setup_logging.info(f"Starting {TestAndroidDiscoveryBasicUiElements.__name__} Test Case")
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        catalog_page = AndroidCatalogPage()

        with allure.step("Goto Discover page"):
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
            expect(android_landing.explore_all_courses_button).to_have(values.LANDING_EXPLORE_COURSES)
            android_landing.explore_all_courses_button.click()
            expect(android_landing.back_navigation_button).to_be_displayed()
            expect(catalog_page.catalog_screen_heading_msg, timeout=30).to_exist()
