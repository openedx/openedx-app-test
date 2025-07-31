"""Discovery screen: search and trending tags"""

import allure
import pytest

from framework import Element, expect
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.ios.pages.ios_discover_page import IosDiscoverPage
from tests.ios.pages.ios_landing import IosLanding


@pytest.mark.IOS
@pytest.mark.IOS_DISCOVERY
@pytest.mark.IOS_SMOKE
class TestIosDiscoverySearchAndTrendingTags:
    """Discovery screen: search and trending tags"""

    def test_discovery_search_and_trending(self, set_capabilities, setup_logging):
        """
        Scenarios:
            1. Go to Discover page.
            - Verify search bar exists.
            - Verify search bar placeholder text: "What do you want to learn?"
            - Verify search button exists with label "Search".
            - Verify "Trending" label under search bar exists.
            - Verify tags exist: Python, Excel, Data Science, Marketing.
            2. Click on Marketing tag.
            - Verify search results are showing marketing courses.
            - Verify search bar contains "marketing".
            3. Click on back button.
            - Verify landing page is loaded.
            4. Click on explore all courses button.
            - Discover page is loaded.
            5. Click on search bar.
            - "Most popular programs" heading is shown with a list of courses.
            6. Type text: "Demo X".
            - Verify clear button appears on search bar.
            7. Click on clear button.
            - Search bar is cleared.
            - Course suggestion is removed.
            8. Type text: "python" and hit search button.
            - Verify search bar shows text "python".
            - Verify All filters button exists.
            - Verify course title contains keyword python.
            - Verify "Courses" heading is displayed.
            - Verify text x results for "python".
            9. Swipe left on course carousel.
            - Verify course heading contains text python.
            - Verify register and sign in button are shown.
            10. Click on back button.
            - Landing page is loaded.
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

        with allure.step("Close AI expert dialogue"):
            if ios_discover_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                ios_discover_page.ai_assistant_dismiss_button.click()
            expect(ios_discover_page.ai_assistant_dismiss_button).not_.to_exist()

        with allure.step("verify search bar exists"):
            expect(ios_discover_page.search_field).to_exist()
            expect(ios_discover_page.search_field).to_have(values.DISCOVERY_SEARCH_FIELD_HINT, ElementAttribute.VALUE)

        with allure.step("verify search button exists with label “Search”"):
            expect(ios_discover_page.search_button).to_exist()
            expect(ios_discover_page.search_button).to_have(values.DISCOVERY_SEARCH_BUTTON, ElementAttribute.LABEL)

        with allure.step("verify trending label exists with text “Trending”"):
            expect(ios_discover_page.trending_tag_label).to_have(
                values.DISCOVERY_TRENDING_LABEL_IOS, ElementAttribute.LABEL
            )

        with allure.step("verify trending tags exists with label"):
            expect(ios_discover_page.trending_tag_python).to_have(
                values.DISCOVERY_TRENDING_COURSE_PYTHON, ElementAttribute.LABEL
            )
            expect(ios_discover_page.trending_tag_excel).to_have(
                values.DISCOVERY_TRENDING_COURSE_EXCEL, ElementAttribute.LABEL
            )
            expect(ios_discover_page.trending_tag_data_sciences).to_have(
                values.DISCOVERY_TRENDING_COURSE_DATA, ElementAttribute.LABEL
            )
            expect(ios_discover_page.trending_tag_marketing).to_have(
                values.DISCOVERY_TRENDING_COURSE_MARKETING, ElementAttribute.LABEL
            )

        with allure.step("Click on trending tag: marketing"):
            ios_discover_page.trending_tag_marketing.click()
            expect(ios_discover_page.results_for_text).to_contain(
                values.DISCOVERY_TRENDING_COURSE_MARKETING, ElementAttribute.LABEL
            )

        with allure.step("verify search bar contains “marketing”"):
            expect(ios_discover_page.search_field).to_have(
                values.DISCOVERY_TRENDING_COURSE_MARKETING, ElementAttribute.VALUE
            )

        with allure.step("verify search results are showing marketing courses"):
            ios_discover_page.verify_search_results_with_keyword(values.DISCOVERY_TRENDING_COURSE_MARKETING)

        with allure.step("Click on back button to return to landing page"):
            ios_discover_page.back_button.click()
            expect(ios_landing.edx_logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)

        with allure.step("Click on explore all courses button"):
            ios_landing.explore_all_courses_button.click()
            ios_discover_page.progress_bar.wait_to_disappear()
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(ios_discover_page.all_filters_dropdown).to_exist()

        with allure.step("Click on search bar"):
            ios_discover_page.search_field.click()

        with allure.step("“Most popular programs” heading is shown with a list of courses"):
            expect(ios_discover_page.most_popular_programs).to_exist()
            expect(ios_discover_page.most_popular_programs).to_be_greater_than("0")

        with allure.step("type text Demo X in search field"):
            ios_discover_page.search_field.send_keys("Demo X")
            expect(ios_discover_page.search_field_clear_button).to_have(
                values.DISCOVER_SEARCH_FIELD_CLEAR_BUTTON, ElementAttribute.LABEL
            )

        with allure.step("Click on clear button"):
            ios_discover_page.search_field_clear_button.click()
            expect(ios_discover_page.search_field).to_have(values.DISCOVERY_SEARCH_FIELD_HINT, ElementAttribute.VALUE)
            expect(ios_discover_page.most_popular_programs).not_.to_exist()

        with allure.step("type text Python in search field"):
            ios_discover_page.search_field.send_keys(values.DISCOVERY_TRENDING_COURSE_PYTHON)
            expect(ios_discover_page.search_field).to_have(
                values.DISCOVERY_TRENDING_COURSE_PYTHON, ElementAttribute.VALUE
            )
            ios_discover_page.search_button.click()

        with allure.step("verify search results are showing python courses"):
            ios_discover_page.verify_search_results_with_keyword(values.DISCOVERY_TRENDING_COURSE_PYTHON)
            expect(ios_discover_page.results_for_text).to_contain(
                values.DISCOVERY_TRENDING_COURSE_PYTHON, ElementAttribute.LABEL
            )
            expect(ios_discover_page.search_field).to_have(
                values.DISCOVERY_TRENDING_COURSE_PYTHON, ElementAttribute.VALUE
            )
            expect(ios_discover_page.all_filters_dropdown).to_exist()
            expect(ios_discover_page.discover_results_page_courses_heading).to_have(
                values.MAIN_DASHBOARD_COURSES, ElementAttribute.LABEL
            )

        with allure.step("verify register and sign in button exists"):
            expect(ios_landing.register_button).to_have(values.REGISTER, ElementAttribute.LABEL)
            expect(ios_landing.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)

        with allure.step("Click on back button to return to landing page"):
            ios_discover_page.back_button.click()
            expect(ios_landing.edx_logo_image).to_have(values.LANDING_LOGO_IMAGE, ElementAttribute.LABEL)
            expect(ios_landing.welcome_message).to_have(values.LANDING_MESSAGE, ElementAttribute.LABEL)
