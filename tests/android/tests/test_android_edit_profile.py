"""
Edit Profile Screen Test Module
"""

import pytest

from framework import expect
from tests.android.pages.android_edit_profile import AndroidEditProfile
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.common import values
from tests.common.enums.attributes import ElementAttribute


@pytest.mark.ANDROID
class TestAndroidEditProfile:
    """
    Profile screen's Test Case
    """

    def test_validate_ui_elements(self, android_login, setup_logging):
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
                Username
                Location label
                Location
                Spoken Language label
                Spoken Language
                About Me label
                About Me placeholder
        """

        main_dashboard_page = AndroidMainDashboard()
        profile_page = AndroidProfile()
        edit_profile_page = AndroidEditProfile()

        profile_tab = main_dashboard_page.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB, ElementAttribute.CONTENT_DESC)
        expect(profile_tab).not_.to_be_selected()
        assert profile_tab.click()
        expect(profile_page.settings_button).to_have(
            values.PROFILE_SETTINGS_UPPER_TEXT, attribute=ElementAttribute.CONTENT_DESC
        )
        expect(profile_page.profile_img_profile).to_contain(
            values.PROFILE_NAME_TEXT, attribute=ElementAttribute.CONTENT_DESC
        )
        expect(profile_page.profile_txt_name).to_have(values.PROFILE_NAME_TEXT)
        expect(profile_page.profile_username).to_have(values.PROFILE_USERNAME_TEXT)
        expect(profile_page.edit_profile_button_text).to_have(values.EDIT_PROFILE_TITLE)
        assert profile_page.edit_profile_button_text.click()
        expect(edit_profile_page.edit_profile_title).to_have(values.EDIT_PROFILE_TITLE)
        expect(edit_profile_page.back_navigation_button).to_be_displayed()
        expect(edit_profile_page.edit_profile_type_label).to_have(values.EDIT_PROFILE_TYPE_LIMITED_PROFILE_LABEL)
        expect(edit_profile_page.edit_profile_user_name).to_have(values.EDIT_PROFILE_USER_NAME)
        expect(edit_profile_page.edit_profile_limited_profile_message).to_have(values.LIMITED_PROFILE_MESSAGE)
        expect(edit_profile_page.edit_profile_txt_label_location).to_have(values.EDIT_PROFILE_LOCATION_LABEL)
        expect(edit_profile_page.profile_tf_select_location).to_have(values.PROFILE_LOCATION_US)
        expect(edit_profile_page.edit_profile_txt_label_spoken_language).to_have(values.EDIT_PROFILE_LANGUAGE_LABEL)
        expect(edit_profile_page.edit_profile_placeholder_select_spoken_language).to_have(
            values.EDIT_PROFILE_LANGUAGE_PLACEHOLDER
        )
        expect(edit_profile_page.edit_profile_txt_label_about_me).to_have(values.EDIT_PROFILE_ABOUT_ME_LABEL)
        expect(edit_profile_page.edit_profile_txt_placeholder_about_me).to_have(values.EDIT_PROFILE_ABOUT_ME)
