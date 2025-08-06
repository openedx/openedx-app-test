"""Discovery screen: Page Sections"""

import allure
import pytest

from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.enums.general_enums import DiscoverSections
from tests.ios.pages.ios_discover_page import IosDiscoverPage
from tests.ios.pages.ios_landing import IosLanding


@allure.epic("DISCOVERY")
@allure.feature("Discover Page")
@allure.story("user can view different sections of discover page")
@allure.suite("IOS REGRESSION")
@pytest.mark.IOS
@pytest.mark.IOS_DISCOVERY
@pytest.mark.IOS_REGRESSION
class TestIosDiscoveryPageSections:
    """Discovery screen: Page Sections"""

    def test_discovery_page_sections(self, set_capabilities, setup_logging):
        """
        Scenario:
            1. Go to Discover page.
               - Verify heading: "Explore courses and programs".
               - Verify the following sections exist:
                - "Most Popular"
                - "Executive Education"
                - "Master’s Degree"
                - "Bachelor’s Degree"
                - "New"
                - "Trending"
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_discover_page = IosDiscoverPage()
        ios_landing = IosLanding()

        with allure.step("Verify landing page is loaded successfully"):
            logo_image = ios_landing.edx_logo_image
            expect(logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.explore_all_courses_button).to_have(
                values.LANDING_EXPLORE_COURSES, ElementAttribute.LABEL
            )

        with allure.step("Click on explore all courses button"):
            ios_landing.explore_all_courses_button.click()
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("Verify discover screen is loaded successfully"):
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(ios_discover_page.back_button).to_have(values.BACK_BUTTON, ElementAttribute.LABEL)

        with allure.step("verify heading “Explore courses and programs“"):
            ios_discover_page.progress_bar.wait_to_disappear()
            if ios_discover_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                ios_discover_page.ai_assistant_dismiss_button.click()
            ios_discover_page.explore_courses_and_programs_section.scroll_and_find()

        with allure.step("verify discover sections exist"):
            ios_discover_page.progress_bar.wait_to_disappear()
            ios_discover_page.verify_section_exists(DiscoverSections.MOST_POPULAR)
            ios_discover_page.verify_section_exists(DiscoverSections.EXECUTIVE_EDUCATION)
            ios_discover_page.verify_section_exists(DiscoverSections.MASTER_DEGREE)
            ios_discover_page.verify_section_exists(DiscoverSections.BACHELOR_DEGREE)
            ios_discover_page.verify_section_exists(DiscoverSections.NEW)
            ios_discover_page.verify_section_exists(DiscoverSections.TRENDING)
