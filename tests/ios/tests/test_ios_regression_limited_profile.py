"""Test limited profile"""

import allure
import pytest

from framework import Element, expect
from tests.common import values
from tests.common.enums.attributes import ElementAttribute
from tests.ios.pages.ios_edit_profile_page import IosEditProfilePage
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile


@allure.epic("Accounts")
@allure.feature("Profile")
@allure.story("Limited profile")
@allure.suite("REGRESSION")
@pytest.mark.IOS
@pytest.mark.IOS_REGRESSION
class TestLimitedProfile:
    """Test limited profile"""

    def test_limited_profile(self, ios_login, setup_logging):
        """Test Limited Profile"""

        driver = ios_login
        Element.set_driver(driver)
        Element.set_logger(setup_logging)
        profile_page = IosProfile()
        edit_profile_page = IosEditProfilePage()
        main_dashboard_page = IosMainDashboard()

        with allure.step("Click on profile tab"):
            main_dashboard_page.profile_tab.click()

        with allure.step("Verify profile fullname and username"):
            expect(profile_page.username_label).to_have(values.PROFILE_USERNAME_TEXT, ElementAttribute.LABEL)
            expect(profile_page.full_name_label).to_have(values.EDIT_PROFILE_USER_NAME, ElementAttribute.LABEL)

        with allure.step("Click on edit profile button"):
            profile_page.edit_profile_button.click()
            expect(edit_profile_page.screen_title).to_have(values.EDIT_PROFILE_TITLE, ElementAttribute.LABEL)
            expect(edit_profile_page.profile_type_label).to_have(
                values.EDIT_PROFILE_TYPE_LIMITED_PROFILE_LABEL_IOS, ElementAttribute.LABEL
            )
            expect(edit_profile_page.username_label).to_have(values.EDIT_PROFILE_USER_NAME, ElementAttribute.LABEL)
            expect(edit_profile_page.switch_profile_type_button).not_.to_exist()
            expect(edit_profile_page.find_by_text_on_screen(values.LIMITED_PROFILE_MESSAGE)).to_exist()

        with allure.step("verify change profile image button is not enabled"):
            expect(edit_profile_page.change_profile_img_button).not_.to_be_enabled()

        with allure.step("Verify location field is present but not editable"):
            expect(edit_profile_page.location_picker_label).to_have(
                values.EDIT_PROFILE_LOCATION_LABEL, ElementAttribute.LABEL
            )
            expect(edit_profile_page.location_picker_button).to_have(
                values.PROFILE_LOCATION_US_IOS, ElementAttribute.LABEL
            )
            expect(edit_profile_page.location_picker_button).not_.to_be_enabled()

        with allure.step("Verify email field is present but not editable"):
            expect(edit_profile_page.spoken_language_picker_label).to_have(
                values.EDIT_PROFILE_LANGUAGE_LABEL_IOS, ElementAttribute.LABEL
            )
            expect(edit_profile_page.spoken_language_picker_button).not_.to_be_enabled()

        with allure.step("Verify about me field is present but not editable"):
            expect(edit_profile_page.user_bio_label).to_have(values.PROFILE_BIO_LABEL, ElementAttribute.LABEL)
            expect(edit_profile_page.user_bio_value).not_.to_be_enabled()
            edit_profile_page.back_navigation_button.click()
