"""Discover Screen: Filters"""

import allure
import pytest

from framework import Element, expect
from tests.common import values
from tests.common.enums import ElementAttribute, ScrollDirections
from tests.common.enums.general_enums import Subjects
from tests.ios.pages.discover_filters_page import DiscoverFilters
from tests.ios.pages.ios_discover_page import IosDiscoverPage
from tests.ios.pages.ios_landing import IosLanding


@allure.epic("DISCOVERY")
@allure.feature("Filters")
@allure.story("user can use filter results by popular subjects")
@allure.suite("IOS REGRESSION")
@pytest.mark.IOS
@pytest.mark.IOS_DISCOVERY
@pytest.mark.IOS_REGRESSION
class TestIosDiscoveryFilters:
    """Discover Screen: Filters"""

    def test_discovery_popular_subjects_filter(self, set_capabilities, setup_logging):
        """
        Scenarios:
            1. Go to Discovery page and scroll down to the popular subjects section.
               - Verify subject tiles are displayed.
            2. Scroll on the subject carousel from right to left.
            3. Click on the math tile.
               - Discovery results page is loaded with courses related to maths.
            4. Scroll down to the programs section.
               - Programs related to the math subject are shown.
            5. Scroll to the All filters button.
               - Label shows “(1 selected)”.
               - Clear all button is shown.
            6. Click on the all filters button.
               - Verify heading "All filters".
               - Clear all and Apply buttons are visible.
            7. Click on the cross icon.
               - Discover page is loaded with filter still applied.
            8. Go back to filter selection drop down.
            9. Click on subject drop down.
               - Verify maths checkbox is checked.
            10. Click on clear all button.
            - Maths is unchecked.
            11. Click on cross icon.
            - Discovery is loaded with filter still applied.
            12. Go back to filter selection.
            13. Uncheck maths by clicking on it.
            14. Click on cross icon.
            - Discovery is loaded with filter still applied.
            15. Go back to filter selection.
            16. Uncheck maths by clicking on it.
            17. Click on apply.
            - Discover page is loaded without any filter applied.
            18. Filter by any popular subject again.
            - Verify results are displayed.
            19. Click on clear all button.
            - Discover page is loaded without any filter applied.
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        ios_discover_page = IosDiscoverPage()
        discover_filters = DiscoverFilters()
        ios_landing = IosLanding()

        with allure.step("Click on explore all courses button"):
            ios_landing.explore_all_courses_button.click()
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("Verify discover screen is loaded successfully"):
            expect(ios_discover_page.navigation_bar_title).to_have(
                values.DISCOVER_SCREEN_HEADING, ElementAttribute.NAME
            )
            expect(ios_discover_page.back_button).to_have(values.BACK_BUTTON, ElementAttribute.LABEL)
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("Close AI expert dialogue"):
            if ios_discover_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                ios_discover_page.ai_assistant_dismiss_button.click()
            expect(ios_discover_page.ai_assistant_dismiss_button).not_.to_exist()

        with allure.step("scroll to popular subjects filter section"):
            ios_discover_page.popular_subjects_filter_section.scroll_and_find()
            ios_discover_page.find_by_text_on_screen(values.DISCOVERY_FIRST_POPULAR_COURSE)
            ios_discover_page.find_by_text_on_screen(values.DISCOVERY_BUSINESS_MANAGEMENT_POPULAR_COURSE, scroll=True)
            ios_discover_page.scroll_horizontally_on_popular_subject_carousel()
            ios_discover_page.find_by_text_on_screen(values.DISCOVERY_POPULAR_MATH_COURSE)

        with allure.step("click on math tile"):
            ios_discover_page.find_by_text_on_screen(values.DISCOVERY_POPULAR_MATH_COURSE).click()
            ios_discover_page.progress_bar.wait_to_disappear()
            ios_discover_page.verify_courses_are_related_to_subject()

        with allure.step("Scroll down to programs section"):
            ios_discover_page.programs_section.scroll_and_find()
            ios_discover_page.verify_courses_are_related_to_subject()

        with allure.step("Scroll to All filters button"):
            ios_discover_page.all_filters_parent_element.scroll_and_find(scroll_direction=ScrollDirections.DOWN)
            buttons = ios_discover_page.all_filters_parent_element.get_child_elements(ios_discover_page.button)
            expect(buttons[0]).to_have(values.X_SELECTER_FILTERS.format("1"), ElementAttribute.LABEL)
            expect(ios_discover_page.discover_results_page_clear_all_filters_button).to_have(
                values.CLEAR_ALL, ElementAttribute.LABEL
            )

        with allure.step("Click on all filters button"):
            ios_discover_page.all_filters_parent_element.click()
            expect(discover_filters.all_filters_heading_text).to_have(
                values.ALL_FILTERS_HEADING, ElementAttribute.LABEL
            )
            expect(discover_filters.clear_all_button).to_have(values.CLEAR_ALL_BUTTON, ElementAttribute.LABEL)
            expect(discover_filters.apply_button).to_have(values.APPLY_BUTTON, ElementAttribute.LABEL)
            expect(discover_filters.close_button).to_have(values.CLOSE_BUTTON, ElementAttribute.LABEL)

        with allure.step("Click on close button"):
            discover_filters.close_button.click()
            expect(ios_discover_page.find_by_text_on_screen(values.X_SELECTER_FILTERS.format("1"))).to_exist()

        with allure.step("Click on all filters button"):
            ios_discover_page.all_filters_parent_element.click()
            discover_filters.subject_dropdown.click()

        with allure.step("Verify math option is selected"):
            discover_filters.subject_option_maths.scroll_and_find()
            expect(discover_filters.subject_option_maths).to_have(values.CHECKED, ElementAttribute.VALUE)

        with allure.step("Click on clear all button"):
            discover_filters.clear_all_button.click()
            expect(discover_filters.subject_option_maths).to_have(values.UNCHECKED, ElementAttribute.VALUE)

        with allure.step("Click on close button"):
            discover_filters.close_button.click()
            expect(ios_discover_page.find_by_text_on_screen(values.X_SELECTER_FILTERS.format("1"))).to_exist()

        with allure.step("Click on all filters button"):
            ios_discover_page.all_filters_parent_element.click()

        with allure.step("Verify math option is selected"):
            discover_filters.subject_option_maths.scroll_and_find()
            expect(discover_filters.subject_option_maths).to_have(values.CHECKED, ElementAttribute.VALUE)

        with allure.step("Uncheck math option"):
            discover_filters.subject_option_maths.click()
            expect(discover_filters.subject_option_maths).to_have(values.UNCHECKED, ElementAttribute.VALUE)

        with allure.step("Click on close button"):
            discover_filters.close_button.click()
            expect(ios_discover_page.find_by_text_on_screen(values.X_SELECTER_FILTERS.format("1"))).to_exist()

        with allure.step("Click on all filters button"):
            ios_discover_page.all_filters_parent_element.click()

        with allure.step("Uncheck math option"):
            discover_filters.subject_option_maths.scroll_and_find()
            discover_filters.subject_option_maths.click()
            expect(discover_filters.subject_option_maths).to_have(values.UNCHECKED, ElementAttribute.VALUE)

        with allure.step("Click on apply button"):
            discover_filters.apply_button.click()
            expect(ios_discover_page.all_filters_dropdown).not_.to_exist()
            expect(ios_discover_page.search_field).to_exist()

        with allure.step("scroll to popular subjects filter section"):
            ios_discover_page.popular_subjects_filter_section.scroll_and_find()
            ios_discover_page.find_by_text_on_screen(values.DISCOVERY_FIRST_POPULAR_COURSE).click()
            ios_discover_page.progress_bar.wait_to_disappear()

        with allure.step("verify courses are related to subject"):
            ios_discover_page.verify_courses_are_related_to_subject(Subjects.DATA_SCIENCE)

        with allure.step("Click on clear all button"):
            ios_discover_page.discover_results_page_clear_all_filters_button.click()
            expect(ios_discover_page.all_filters_dropdown).not_.to_exist()
            expect(ios_discover_page.search_field).to_exist()
