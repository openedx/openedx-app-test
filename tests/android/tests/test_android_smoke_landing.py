"""
Landing Test Module
"""

import allure
import pytest

from framework import expect
from framework.element import Element
from tests.android.pages.andriod_catalog_page import AndroidCatalogPage
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.common import values


@allure.epic("ANDROID SMOKE")
@allure.feature("Landing Page")
@allure.story("landing page components work correctly")
@allure.suite("ANDROID SMOKE")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_SMOKE
class TestAndroidLanding:
    """
    Landing screen's Test Case
    """

    def test_smoke_landing_page(self, set_capabilities, setup_logging):
        """
        test smoke landing page
        """

        setup_logging.info(f"Starting {TestAndroidLanding.__name__} Test Case")
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_sign_in = AndroidSignIn()
        android_catalog_page = AndroidCatalogPage()

        with allure.step("verify landing page heading"):
            expect(android_landing.screen_title).to_exist()
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)

        with allure.step("verify search bar title text"):
            expect(android_landing.get_search_label).to_have(values.LANDING_SEARCH_TITLE)

        with allure.step("verify login & registration button"):
            expect(android_landing.register_button).to_exist()
            expect(android_landing.signin_button).to_exist()

        with allure.step("verify explore all courses button exist"):
            expect(android_landing.explore_all_courses_button).to_have(values.LANDING_EXPLORE_COURSES)
            expect(android_landing.explore_all_courses_button).to_be_enabled()

        with allure.step("verify search bar and placeholder text for search bar"):
            expect(android_landing.discovery_search).to_exist()
            expect(android_landing.search_bar_placeholder_text).to_have(values.LANDING_SEARCH_COURSES)

        with allure.step("click on search bar"):
            android_landing.search_using_landing_discovery_search("python")

        with allure.step("verify screen title and page loaded"):
            expect(android_catalog_page.catalog_screen_toolbar_title).to_have(values.DISCOVERY_SCREEN_TITLE)
            expect(android_catalog_page.all_filters_button).to_exist()

        with allure.step("close Ai expert prompt if exists"):
            if android_catalog_page.ai_assistant_dismiss_button.exists(raise_exception=False):
                android_landing.ai_assistant_dismiss_button.click()

        with allure.step("verify courses heading exists"):
            expect(android_catalog_page.find_by_text_on_screen(values.MAIN_DASHBOARD_COURSES)).to_exist()
            expect(android_catalog_page.search_bar_text).to_have("python")
            expect(android_catalog_page.find_by_partial_text_on_screen("results for")).to_contain("python")

        with allure.step("click on back button"):
            android_catalog_page.back_navigation_button.click()
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)

        with allure.step("click on explore all courses button"):
            android_landing.explore_all_courses_button.click()
            expect(android_catalog_page.catalog_screen_toolbar_title).to_have(values.DISCOVERY_SCREEN_TITLE)
            expect(android_catalog_page.find_by_text_on_screen(values.DISCOVERY_SCREEN_MESSAGE)).to_exist()

        with allure.step("verify signin and register button exists"):
            expect(android_landing.register_button).to_exist()
            expect(android_landing.signin_button).to_exist()
            expect(android_landing.signin_button_text).to_have(values.SIGN_IN_TEXT)
            expect(android_landing.register_button_text).to_have(values.REGISTER)

        # TODO: no element in DOM is exposing the place holder text
        with allure.step("verify search button and place holder text for search bar"):
            expect(android_catalog_page.search_button).to_exist()

        with allure.step("click on back button"):
            android_catalog_page.back_navigation_button.click()
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)

        with allure.step("click on register button and verify registration page is loaded"):
            android_landing.load_register_screen()
            expect(android_sign_in.screen_title).to_have(values.REGISTER)

        with allure.step("Go back to landing page"):
            android_landing.back_navigation_button.click()

        with allure.step("click on sign in button and verify registration page is loaded"):
            android_landing.load_signin_screen()
            expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.SIGN_IN_TEXT)

        with allure.step("Go back to landing page"):
            android_landing.back_navigation_button.click()
            expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
