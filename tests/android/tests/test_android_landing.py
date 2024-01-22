"""
    New Landing Test Module
"""

from tests.android.pages.android_landing import AndroidLanding
from tests.common import values
from tests.common.globals import Globals


class TestAndroidNewLanding:
    """
    New Landing screen's Test Case
    """

    def test_start_new_landing_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify New Landing screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidNewLanding.__name__} Test Case')
        android_new_landing = AndroidLanding(set_capabilities, setup_logging)

        assert android_new_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_new_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
        assert android_new_landing.get_discovery_search().text == values.LANDING_SEARCH_RESULTS_TITLE
        android_new_landing.navigate_back_on_screen()

        assert android_new_landing.get_explore_courses().text == values.LANDING_EXLPORE_COURSES
        assert android_new_landing.get_register_button()
        assert android_new_landing.load_register_screen().text == values.REGISTER
        android_new_landing.get_back_button().click()

        assert android_new_landing.get_signin_button()
        assert android_new_landing.load_signin_screen().text == values.LOGIN
        android_new_landing.get_back_button().click()
        assert android_new_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
