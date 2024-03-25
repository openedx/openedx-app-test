"""
    Landing Test Module
"""

from tests.android.pages.android_landing import AndroidLanding
from tests.common import values
from tests.common.globals import Globals


class TestAndroidLanding:
    """
    Landing screen's Test Case
    """

    def test_start_landing_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Landing screen is loaded successfully
        """

        setup_logging.info(f'Starting {TestAndroidLanding.__name__} Test Case')
        android_landing = AndroidLanding(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)

        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
        assert android_landing.get_search_label().text == values.LANDING_SEARCH_TITLE
        assert android_landing.get_discovery_search().text == values.DISCOVERY_SCREEN_TITLE
        global_contents.get_back_button(set_capabilities).click()

        assert android_landing.get_explore_courses().text == values.LANDING_EXLPORE_COURSES
        assert android_landing.get_register_button()
        assert android_landing.load_register_screen().text == values.REGISTER
        global_contents.get_back_button(set_capabilities).click()

        assert android_landing.get_signin_button()
        assert android_landing.load_signin_screen().text == values.LOGIN
        global_contents.get_back_button(set_capabilities).click()
        assert android_landing.get_screen_title().text == values.LANDING_MESSAGE_IOS
