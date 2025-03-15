
"""
    Edit Profile Screen Test Module
"""

from framework import expect
from framework.element import Element
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_edit_profile import  AndroidEditProfile
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
from tests.common.globals import Globals


class TestAndroidEditProfile:
    """
    Profile screen's Test Case
    """

    def test_start_edit_profile_screen_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info(f'Starting {TestAndroidEditProfile.__name__} Test Case')
        global_contents = Globals(setup_logging)
        whats_new_page = AndroidWhatsNew()

        if login and global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have('Done')
            assert whats_new_page.done_button.click()

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that on clicking edit profile button,
            Edit Profile screen will show following contents:
            Verify that Edit Profile screen will show following contents:
                Back icon
                "Edit Profile" as Title
                Done button
                Profile type
                Limited profile message
                Profile Image
                User Name
                Location label
                Location
                Spoken Language label
                Spoken Language
                About Me label
                About Me placeholder
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        main_dashboard_page = AndroidMainDashboard()
        profile_page = AndroidProfile()
        edit_profile_page = AndroidEditProfile()

        profile_tab = main_dashboard_page.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB, ElementAttribute.CONTENT_DESC)
        expect(profile_tab).to_not.to_be_selected()
        assert profile_tab.click()
        expect(profile_page.settings_button).to_have(values.PROFILE_SETTINGS_TEXT, type=ElementAttribute.CONTENT_DESC)
        expect(profile_page.profile_img_profile).to_contain(values.PROFILE_NAME_TEXT, type=ElementAttribute.CONTENT_DESC)
        expect(profile_page.profile_txt_name).to_have(values.PROFILE_NAME_TEXT)
        expect(profile_page.profile_username).to_have(values.PROFILE_USERNAME_TEXT)
        expect(profile_page.edit_profile_button).to_have(values.EDIT_PROFILE_TITLE)
        assert profile_page.edit_profile_button.click()
        expect(edit_profile_page.edit_profile_title).to_have(values.EDIT_PROFILE_TITLE)
        expect(edit_profile_page.done_button).to_have(values.EDIT_PROFILE_DONE_BUTTON)
        expect(edit_profile_page.back_navigation_button).to_be_displayed()
        expect(edit_profile_page.edit_profile_type_label).to_have(values.EDIT_PROFILE_TYPE_LABEL)
        expect(edit_profile_page.edit_profile_user_name).to_have(values.EDIT_PROFILE_USER_NAME)
        expect(edit_profile_page.edit_profile_limited_profile_message).to_have(values.EDIT_PROFILE_MESSAGE)
        expect(edit_profile_page.edit_profile_txt_label_location).to_have(values.EDIT_PROFILE_LOCATION_LABEL)
        expect(edit_profile_page.profile_tf_select_location).to_have(values.EDIT_PROFILE_LOCATION)
        expect(edit_profile_page.edit_profile_txt_label_spoken_language).to_have(values.EDIT_PROFILE_LANGUAGE_LABEL)
        expect(edit_profile_page.edit_profile_select_spoken_language).to_have(values.EDIT_PROFILE_LANGUAGE)
        expect(edit_profile_page.edit_profile_txt_label_about_me).to_have(values.EDIT_PROFILE_ABOUT_ME_LABEL)
        expect(edit_profile_page.edit_profile_txt_placeholder_about_me).to_have(values.EDIT_PROFILE_ABOUT_ME)
