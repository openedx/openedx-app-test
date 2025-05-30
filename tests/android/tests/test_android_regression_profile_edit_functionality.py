"""Android - Regression - profile edit functionality"""

import allure
import pytest

from framework import Element, expect
from tests.android.pages.android_edit_profile import AndroidEditProfile
from tests.android.pages.android_landing import AndroidLanding
from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_profile import AndroidProfile
from tests.android.pages.android_sign_in import AndroidSignIn
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.common import values
from tests.common.enums.general_enums import CountryAbbreviation, LanguageAbbreviation
from tests.common.globals import Globals


@allure.epic("Accounts")
@allure.feature("Profile")
@allure.story("Edit profile")
@allure.suite("REGRESSION")
@pytest.mark.ANDROID
@pytest.mark.ANDROID_REGRESSION
class TestProfileEditFunctionality:
    """Test profile edit functionality"""

    def test_profile_edit_functionality(self, set_capabilities, setup_logging):
        """"""
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        profile_page = AndroidProfile()
        edit_profile_page = AndroidEditProfile()
        main_dashboard_page = AndroidMainDashboard()
        android_landing_page = AndroidLanding()
        android_sign_in = AndroidSignIn()
        whats_new_page = AndroidWhatsNew()
        global_contents = Globals(setup_logging)

        test_exception = None

        with allure.step("Click on Sign in button"):
            android_landing_page.load_signin_screen()
            expect(android_sign_in.signin_title, "Sign in screen not loaded successfully").to_have(values.LOGIN)

        with allure.step("Enter a valid email or username"):
            android_sign_in.sign_in_tf_email.send_keys("rtester99")

        with allure.step("Enter a valid password"):
            android_sign_in.sign_in_password_field.send_keys(global_contents.rtester_user_password)

        with allure.step("Click on Sign in button"):
            android_sign_in.signin_button.click()
            setup_logging.info("rtester99 is successfully logged in")
            if whats_new_page.get_close_button.exists(raise_exception=False):
                whats_new_page.get_close_button.click()

        with allure.step("Goto Profile Tab"):
            main_dashboard_page.profile_tab.click()

        with allure.step("verify username and Full name"):
            expect(profile_page.profile_username).to_have(values.RTESTER_USERNAME_TEXT)
            expect(profile_page.profile_txt_name).to_have(values.RTESTER_NAME_TEXT)
            profile_page.profile_settings_about_me.exists()
            expect(profile_page.profile_settings_about_me_body).to_have(values.PROFILE_ABOUT_ME_TEXT)
            profile_page.edit_profile_button.exists()
            expect(profile_page.edit_profile_button_text).to_have(values.EDIT_PROFILE_TITLE)

        with allure.step("Click on Edit Profile button"):
            profile_page.edit_profile_button.click()
            expect(edit_profile_page.edit_profile_title).to_have(values.EDIT_PROFILE_TITLE)
            expect(edit_profile_page.done_button).not_.to_exist()
            expect(edit_profile_page.edit_profile_type_label).to_have(values.EDIT_PROFILE_TYPE_LABEL_FULL_PROFILE)
            expect(edit_profile_page.edit_profile_user_name).to_have(values.RTESTER_NAME_TEXT)
            expect(edit_profile_page.switch_profile_type_button).to_have(values.EDIT_PROFILE_SWITCH_TO_LIMITED_PROFILE)
            expect(edit_profile_page.edit_profile_limited_profile_message).to_have(
                values.LIMITED_PROFILE_DISCLAIMER_MESSAGE
            )

            expect(edit_profile_page.edit_profile_txt_label_location).to_have(values.EDIT_PROFILE_LOCATION_LABEL)
            expect(edit_profile_page.profile_tf_select_location).to_have(values.PROFILE_LOCATION_US)
            expect(edit_profile_page.edit_profile_txt_label_spoken_language).to_have(values.EDIT_PROFILE_LANGUAGE_LABEL)
            expect(edit_profile_page.select_spoken_language).to_have(values.PROFILE_LANGUAGE)
            expect(edit_profile_page.edit_profile_txt_label_about_me).to_have(values.EDIT_PROFILE_ABOUT_ME_LABEL)
            expect(edit_profile_page.about_me_input).to_have(values.PROFILE_ABOUT_ME_TEXT)

        with allure.step("Click on location dropdown"):
            edit_profile_page.profile_tf_select_location.click()
            expect(edit_profile_page.drop_down_title).to_have(values.DROP_DOWN_HEADING_LOCATION)
            expect(edit_profile_page.sb_search_field).to_exist()

        with allure.step("Search and select a location"):
            edit_profile_page.sb_search_field.send_keys(values.CANADA)
            country_opt_canada = Globals.get_country_by_resource_id(CountryAbbreviation.CA)
            expect(country_opt_canada).to_have(values.CANADA)
            country_opt_canada.click()
            expect(edit_profile_page.profile_tf_select_location).to_have(values.CANADA)
            expect(edit_profile_page.done_button).to_exist()
            expect(edit_profile_page.done_button_tick_mark).to_exist()

        with allure.step("Click on Spoken Language dropdown"):
            edit_profile_page.select_spoken_language.click()
            expect(edit_profile_page.drop_down_title).to_have(values.DROP_DOWN_HEADING_LANGUAGE)
            expect(edit_profile_page.sb_search_field).to_exist()

        with allure.step("Search and select a Spoken Language"):
            edit_profile_page.sb_search_field.send_keys(values.FRENCH)
            language_opt_english = Globals.get_language_by_abbreviation(LanguageAbbreviation.FR)
            expect(language_opt_english).to_have(values.FRENCH)
            language_opt_english.click()
            expect(edit_profile_page.select_spoken_language).to_have(values.FRENCH)

        with allure.step("Click on about me text box"):
            edit_profile_page.about_me_input.click()
            edit_profile_page.about_me_input.send_keys("Automation Test")

        with allure.step("click on image upload icon"):
            edit_profile_page.get_edit_profile_user_image.click()
            expect(edit_profile_page.change_profile_image_title_label).to_have(values.CHANGE_PROFILE_IMAGE_TITLE_LABEL)

        with allure.step("verify buttons appear on change profile image screen"):
            expect(edit_profile_page.remove_photo_button).to_exist()
            expect(edit_profile_page.ic_remove_photo).to_exist()
            expect(edit_profile_page.text_remove_photo).to_have("Remove photo")
            expect(edit_profile_page.select_from_gallery_button).to_exist()
            expect(edit_profile_page.ic_select_from_gallery).to_exist()
            expect(edit_profile_page.text_select_from_gallery).to_have("Select from gallery")
            expect(edit_profile_page.change_profile_image_cancel_button).to_exist()
            expect(edit_profile_page.change_profile_image_cancel_button_text).to_have("Cancel")

        with allure.step("click on remove photo button"):
            edit_profile_page.remove_photo_button.click()

        with allure.step("verify photo is removed"):
            edit_profile_page.get_edit_profile_user_image.click()
            expect(edit_profile_page.remove_photo_button).not_.to_exist()

        with allure.step("click on select from gallery"):
            edit_profile_page.select_from_gallery_button.click()

        with allure.step("select a photo from gallery"):
            edit_profile_page.image_to_upload.click()
            edit_profile_page.get_edit_profile_user_image.click()
            expect(edit_profile_page.remove_photo_button).to_exist()

        with allure.step("click on cancel button"):
            edit_profile_page.change_profile_image_cancel_button.click()
            expect(edit_profile_page.remove_photo_button).not_.to_exist()
            expect(edit_profile_page.select_from_gallery_button).not_.to_exist()
            expect(edit_profile_page.change_profile_image_cancel_button).not_.to_exist()
        try:
            with allure.step("click on Done button"):
                edit_profile_page.done_button.click()
                edit_profile_page.done_button.wait_to_disappear(timeout=5)

            with allure.step("click on back button"):
                edit_profile_page.back_navigation_button.click()
                expect(profile_page.profile_settings_about_me_body).to_have("Automation Test")

            with allure.step("click on edit profile button"):
                profile_page.edit_profile_button.click()
                expect(edit_profile_page.profile_tf_select_location).to_have(values.CANADA)
                expect(edit_profile_page.select_spoken_language).to_have(values.FRENCH)
                expect(edit_profile_page.about_me_input).to_have("Automation Test")

            with allure.step("Click on switch to limited profile"):
                edit_profile_page.switch_profile_type_button.click()

            with allure.step("verify sub-heading “Limited profile"):
                expect(edit_profile_page.edit_profile_type_label).to_have(
                    values.EDIT_PROFILE_TYPE_LIMITED_PROFILE_LABEL
                )

            with allure.step("verify the fields are no longer enabled"):
                expect(edit_profile_page.profile_tf_select_location).not_.to_be_enabled()
                expect(edit_profile_page.select_spoken_language).not_.to_be_enabled()
                expect(edit_profile_page.about_me_input).not_.to_be_enabled()

            with allure.step("verify done button appears "):
                expect(edit_profile_page.done_button).to_exist()

            with allure.step("click on Switch to full profile"):
                edit_profile_page.switch_profile_type_button.click()

            with allure.step("verify sub-heading “Full profile"):
                expect(edit_profile_page.edit_profile_type_label).to_have(values.EDIT_PROFILE_TYPE_LABEL_FULL_PROFILE)

            with allure.step("verify the fields are enabled"):
                pass
                # TODO : these fields don't have any attribute to check if they are enabled or disabled
                # expect(edit_profile_page.profile_tf_select_location).to_be_enabled()
                # expect(edit_profile_page.select_spoken_language).to_be_enabled()
                # expect(edit_profile_page.about_me_input).to_be_enabled()

        except Exception as exception:
            test_exception = exception
            setup_logging.info(f"Following exception occurred: {exception}")
            setup_logging.info("Performing cleanup")
        finally:
            with allure.step("Change values to original"):
                if profile_page.edit_profile_button.exists(raise_exception=False):
                    profile_page.edit_profile_button.click()
                edit_profile_page.profile_tf_select_location.click()
                edit_profile_page.sb_search_field.send_keys(values.PROFILE_LOCATION_US)
                country_opt_canada = Globals.get_country_by_resource_id(CountryAbbreviation.US)
                expect(country_opt_canada).to_have(values.PROFILE_LOCATION_US)
                country_opt_canada.click()
                expect(edit_profile_page.profile_tf_select_location).to_have(values.PROFILE_LOCATION_US)
                edit_profile_page.select_spoken_language.click()
                edit_profile_page.sb_search_field.send_keys(values.ENGLISH)
                language_opt_english = Globals.get_language_by_abbreviation(LanguageAbbreviation.EN)
                expect(language_opt_english).to_have(values.ENGLISH)
                language_opt_english.click()
                expect(edit_profile_page.select_spoken_language).to_have(values.ENGLISH)

                edit_profile_page.about_me_input.click()
                edit_profile_page.about_me_input.send_keys(values.PROFILE_ABOUT_ME_TEXT)
                edit_profile_page.done_button.click()
                edit_profile_page.android_loading_circle.wait_to_disappear(20)

            with allure.step("click on back button"):
                edit_profile_page.back_navigation_button.click()

            if test_exception:
                raise test_exception
