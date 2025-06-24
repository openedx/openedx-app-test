"""Test limited profile"""

import allure
import pytest

from framework import Element, expect
from tests.android.pages.android_edit_profile import AndroidEditProfile
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.common import values


@allure.epic("Accounts")
@allure.feature("Profile")
@allure.story("Limited profile")
@allure.suite("REGRESSION")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_REGRESSION
class TestLimitedProfile:
    """Test limited profile"""

    def test_limited_profile(self, android_login, setup_logging):
        """Test Limited Profile"""

        driver = android_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        profile_page = AndroidProfile()
        edit_profile_page = AndroidEditProfile()
        main_dashboard_page = AndroidMainDashboard()

        with allure.step("Click on profile tab"):
            main_dashboard_page.profile_tab.click()

        with allure.step("Verify profile fullname and username"):
            expect(profile_page.profile_username).to_have(values.PROFILE_NAME_TEXT)
            expect(profile_page.profile_txt_name).to_have(values.PROFILE_USERNAME_TEXT)

        with allure.step("Click on edit profile button"):
            profile_page.edit_profile_button.click()
            expect(edit_profile_page.edit_profile_title).to_have(values.EDIT_PROFILE_TITLE)
            expect(edit_profile_page.edit_profile_type_label).to_have(values.EDIT_PROFILE_TYPE_LIMITED_PROFILE_LABEL)
            expect(edit_profile_page.edit_profile_user_name).to_have(values.PROFILE_NAME_TEXT)
            expect(edit_profile_page.edit_profile_limited_profile_message).to_have(values.LIMITED_PROFILE_MESSAGE)

        with allure.step("Click on profile image"):
            edit_profile_page.get_edit_profile_user_image.click()
            expect(edit_profile_page.select_from_gallery_button).not_.to_exist()

        with allure.step("Verify location field is present but not editable"):
            expect(edit_profile_page.edit_profile_txt_label_location).to_have(values.EDIT_PROFILE_LOCATION_LABEL)
            expect(edit_profile_page.profile_tf_select_location).to_have(values.PROFILE_LOCATION_US)
            expect(edit_profile_page.profile_tf_select_location).not_.to_be_enabled()

        with allure.step("Verify email field is present but not editable"):
            expect(edit_profile_page.edit_profile_txt_label_spoken_language).to_have(values.EDIT_PROFILE_LANGUAGE_LABEL)
            expect(edit_profile_page.select_spoken_language).to_have(values.PROFILE_LANGUAGE)
            expect(edit_profile_page.select_spoken_language).not_.to_be_enabled()

        with allure.step("Verify about me field is present but not editable"):
            expect(edit_profile_page.edit_profile_txt_label_about_me).to_have(values.EDIT_PROFILE_ABOUT_ME_LABEL)
            expect(edit_profile_page.about_me_input).to_have(values.PROFILE_ABOUT_ME_TEXT)
            expect(edit_profile_page.about_me_input).not_.to_be_enabled()
