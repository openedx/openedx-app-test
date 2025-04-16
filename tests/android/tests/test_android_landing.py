"""
Landing Test Module
"""

from framework import expect
from framework.element import Element
from tests.android.pages.andriod_catalog_page import AndroidCatalogPage
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.common import values


class TestAndroidLanding:
    """
    Landing screen's Test Case
    """

    def test_start_landing_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Landing screen is loaded successfully
        """

        setup_logging.info(f"Starting {TestAndroidLanding.__name__} Test Case")
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        android_landing = AndroidLanding()
        android_sign_in = AndroidSignIn()
        android_catalog_page = AndroidCatalogPage()

        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
        expect(android_landing.get_search_label).to_have(values.LANDING_SEARCH_TITLE)
        assert android_landing.discovery_search.click()
        assert android_landing.discovery_search.send_keys("Automation")
        Element.press_keycode(66)
        expect(android_catalog_page.catalog_screen_toolbar_title).to_have(values.DISCOVERY_SCREEN_TITLE)
        assert android_catalog_page.back_navigation_button.click()

        expect(android_landing.get_explore_courses).to_have(values.LANDING_EXLPORE_COURSES)
        assert android_landing.get_register_button.exists()
        assert android_landing.load_register_screen()
        expect(android_sign_in.screen_title).to_have(values.REGISTER)
        assert android_landing.back_navigation_button.click()

        assert android_landing.signin_button.exists()
        assert android_landing.load_signin_screen()
        expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)
        assert android_landing.back_navigation_button.click()
        expect(android_landing.screen_title).to_have(values.LANDING_MESSAGE)
