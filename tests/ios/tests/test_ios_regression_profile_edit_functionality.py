"""IOS - Regression - profile edit functionality"""

from logging import Logger
import allure
from appium.webdriver.webdriver import WebDriver
import pytest
import os
import base64


from framework import Element, expect
from tests.common import values
from tests.common.enums import ElementAttribute, ScrollDirections
from tests.common.enums.general_enums import Country, Language
from tests.common.globals import Globals
from tests.ios.pages.ios_edit_profile_page import IosEditProfilePage
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_whats_new import IosWhatsNew


@allure.epic("Profile & Settings")
@allure.feature("Profile")
@allure.story("user can edit profile info")
@allure.suite("IOS REGRESSION")
@pytest.mark.IOS
@pytest.mark.IOS_REGRESSION
class TestProfileEditFunctionality:
    """Test regression profile edit functionality"""

    def verify_user_details_on_profile_edit_page(self):
        """
        Verifies that all user details on the Edit Profile page are displayed correctly.

        This method checks the presence and correctness of various UI elements on the Edit Profile screen,
        including the screen title, profile type, username, profile switch button, disclaimer message,
        location and language pickers, and user bio label. It uses assertions to ensure that each element
        matches the expected values defined in the `values` module.

        Raises:
            AssertionError: If any of the UI elements do not match the expected values.
        """
        """"""

        edit_profile_page = IosEditProfilePage()

        expect(edit_profile_page.screen_title).to_have(values.EDIT_PROFILE_TITLE, ElementAttribute.LABEL)
        expect(edit_profile_page.done_button).to_have(values.FALSE_LOWERCASE, ElementAttribute.ACCESSIBLE)
        expect(edit_profile_page.profile_type_label).to_have(
            values.EDIT_PROFILE_TYPE_LABEL_FULL_PROFILE_IOS, ElementAttribute.LABEL
        )
        expect(edit_profile_page.username_label).to_have(values.RTESTER_NAME_TEXT, ElementAttribute.LABEL)
        expect(edit_profile_page.switch_profile_type_button).to_have(
            values.EDIT_PROFILE_SWITCH_TO_LIMITED_PROFILE, ElementAttribute.LABEL
        )
        expect(edit_profile_page.find_by_text_on_screen(values.LIMITED_PROFILE_DISCLAIMER_MESSAGE_IOS)).to_exist()

        expect(edit_profile_page.location_picker_label).to_have(
            values.EDIT_PROFILE_LOCATION_LABEL, ElementAttribute.LABEL
        )
        expect(edit_profile_page.location_picker_button).to_have(values.PROFILE_LOCATION_US_IOS, ElementAttribute.LABEL)
        expect(edit_profile_page.spoken_language_picker_label).to_have(
            values.EDIT_PROFILE_LANGUAGE_LABEL_IOS, ElementAttribute.LABEL
        )
        expect(edit_profile_page.spoken_language_picker_button).to_have(values.PROFILE_LANGUAGE, ElementAttribute.LABEL)
        expect(edit_profile_page.user_bio_label).to_have(values.PROFILE_BIO_LABEL, ElementAttribute.LABEL)
        # expect(edit_profile_page.user_bio_value).to_have(values.PROFILE_BIO_VALUE, ElementAttribute.LABEL)

    def verify_user_details_on_profile_page(self):
        """
        Verifies that all user details on the Profile page are displayed correctly.

        This method checks the presence and correctness of various UI elements on the Profile screen,
        including the username, full name, profile bio label, profile bio value, and edit profile button.
        It uses assertions to ensure that each element matches the expected values defined in the `values` module.

        Raises:
            AssertionError: If any of the UI elements do not match the expected values.
        """

        profile_page = IosProfile()
        expect(profile_page.username_label).to_have(values.RTESTER_USERNAME_TEXT, ElementAttribute.LABEL)
        expect(profile_page.full_name_label).to_have(values.RTESTER_NAME_TEXT, ElementAttribute.LABEL)
        profile_page.profile_bio_label.exists()
        expect(profile_page.profile_bio_label).to_have(values.PROFILE_ABOUT_ME_LABEL, ElementAttribute.LABEL)
        expect(profile_page.profile_bio_value).to_have(values.PROFILE_BIO_VALUE, ElementAttribute.LABEL)
        profile_page.edit_profile_button.exists()
        expect(profile_page.edit_profile_button).to_have(values.EDIT_PROFILE_TITLE, ElementAttribute.LABEL)

    def verify_button_on_change_profile_img_dialogue(self):
        """
        verify that all required buttons are present
        Remove img button
        Select img button
        Cancel button
        """
        edit_profile_page = IosEditProfilePage()
        expect(edit_profile_page.remove_img_button).to_exist()
        expect(edit_profile_page._ic_remove_img).to_exist()
        expect(edit_profile_page.remove_img_button).to_have("Remove photo", ElementAttribute.LABEL)
        expect(edit_profile_page.select_img_button).to_exist()
        expect(edit_profile_page.ic_select_img).to_exist()
        expect(edit_profile_page.select_img_button).to_have("Select from gallery", ElementAttribute.LABEL)
        expect(edit_profile_page.cancel_button).to_exist()
        expect(edit_profile_page.cancel_button).to_have("Cancel", ElementAttribute.LABEL)

    def test_upload_image_to_camera_roll(self, set_capabilities: WebDriver | None, setup_logging: Logger):
        """upload image as a pre-req"""
        global_contents = Globals(setup_logging)
        driver = set_capabilities
        local_image_path = "tests/image-data/dummy-pfp-image.png"

        if not os.path.exists(local_image_path):
            raise FileNotFoundError(f"Image not found at: {local_image_path}")

        remote_image_name = "dummy-pfp-image.png"
        # Read and encode the image
        with open(local_image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")

        command = "mobile: pushFile"
        args = {"remotePath": remote_image_name, "payload": image_data}

        # Push the image to the Photos app
        global_contents.execute_script(driver, command, args)

        setup_logging.info(f"Image '{remote_image_name}' pushed to simulator Camera Roll.")

    def test_ios_regression_profile_edit_functionality(self, set_capabilities: WebDriver | None, setup_logging: Logger):
        """
        Test Steps:

        1. Click on Profile tab
            - Verify username
            - Verify user full name
            - Verify About Me section is displayed
            - Verify About Me description
            - Verify edit profile button exists

        2. Click on Edit Profile button
            - Verify screen title “Edit Profile”
            - Verify Done button is greyed out
            - Verify sub-heading “Full profile“
            - Verify user full name
            - Verify option to switch to limited profile
            - Verify limited profile disclaimer “A limited profile only shares your username and profile photo.”
            - Verify Location field heading “Location”
            - Verify location field placeholder text “Location“
            - Verify language field heading “Spoken Language”
            - Verify language field value “English”
            - Verify About Me heading exists
            - Verify about me field value “About me/…”

        3. Click on location dropdown
            - Location heading appears

        4. Search any location and click on it
            - Verify location value is set in location field
            - Verify Done button appears

        5. Click on spoken language dropdown
            - Spoken Language title appears

        6. Search a language and click on it
            - Verify spoken language field value is set

        7. Click on about me text box

        8. Add some text and click on Done button
            - Verify done button disappears

        9. Click on back button

        10. Click on edit profile button
            - Verify newly added values are still present

        11. Click on image upload icon
            - Verify change profile image title
            - Verify buttons appear: Select from gallery, Remove photo, Cancel

        12. Click on remove photo button

        13. Click on image upload icon
            - Verify photo is removed (remove photo button disappears in the menu)

        14. Click on select from gallery

        15. Select a photo from gallery
            - Verify photo is updated

        16. Click on cancel button
            - Verify buttons disappear: Select from gallery, Remove photo, Cancel

        17. Click on location dropdown
            - Location heading appears

            - Search any location and click on it
            - Verify location value is set in location field
            - Verify Done button appears

            - Click on back button
            - Warning prompt appears: “Leave without saving?”
            - Subheading: “Changes you have made will be discarded”
            - Leave & Keep editing buttons are shown
            - Close button appears as a cross

            - Click on Keep editing
            - Warning disappears and Done button is visible and location change is present

            - Click on back button & click on cross button
            - Warning disappears and Done button is visible and location change is present

            - Click on back button & click on Leave button
            - Profile page is opened

            - Click on edit profile button
            - Location changes were not saved

        18. Click on switch to limited profile
            - Verify sub-heading “Limited profile”
            - Verify the fields are no longer enabled
            - Verify done button appears

        19. Click on Switch to full profile
            - Verify sub-heading “Full profile“
            - Verify fields are enabled
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        profile_page = IosProfile()
        edit_profile_page = IosEditProfilePage()
        main_dashboard_page = IosMainDashboard()
        ios_landing_page = IosLanding()
        ios_login_page = IosLogin()
        whats_new_page = IosWhatsNew()
        global_contents = Globals(setup_logging)

        with allure.step("dismiss notifications pop-up if exists"):
            if ios_landing_page.allow_notifications_button.exists(raise_exception=False):
                ios_landing_page.allow_notifications_button.click()

        with allure.step("Click on Sign in button"):
            expect(ios_landing_page.sign_in_button).to_have(values.SIGN_IN_TEXT, ElementAttribute.LABEL)
            ios_landing_page.sign_in_button.click()

        with allure.step("Enter a valid email or username"):
            ios_login_page.username_textfield.send_keys(values.RTESTER_NAME_TEXT + "\n")

        with allure.step("Enter a valid password"):
            ios_login_page.password_textfield.send_keys(global_contents.rtester_user_password + "\n")

        with allure.step("Click on Sign in button"):
            ios_login_page.signin_button.click()
            setup_logging.info("rtester99 is successfully logged in")
            if whats_new_page.whats_new_next_button.exists(raise_exception=False):
                whats_new_page.close_button.click()
                setup_logging.info("Whats New screen is successfully loaded")

        with allure.step("Goto Profile Tab"):
            main_dashboard_page.profile_tab.click()

        with allure.step("verify username and Full name"):
            self.verify_user_details_on_profile_page()

        with allure.step("Click on Edit Profile button"):
            profile_page.edit_profile_button.click()
            self.verify_user_details_on_profile_edit_page()

        with allure.step("Click on location dropdown"):
            edit_profile_page.location_picker_button.click()
            expect(edit_profile_page.picker_title_text).to_have(
                values.DROP_DOWN_HEADING_LOCATION, ElementAttribute.LABEL
            )
            expect(edit_profile_page.option_picker_search_field).to_exist()

        with allure.step("Search and select a location"):
            edit_profile_page.option_picker_search_field.send_keys(values.CANADA + "\n")
            edit_profile_page.search_and_verify_country_option_exists(Country.CANADA)
            edit_profile_page.get_picker_accept_button.click()
            expect(edit_profile_page.location_picker_button).to_have(values.CANADA, ElementAttribute.LABEL)

        with allure.step("Click on Spoken Language dropdown"):
            edit_profile_page.spoken_language_picker_button.click()
            expect(edit_profile_page.picker_title_text).to_have(
                values.EDIT_PROFILE_LANGUAGE_LABEL_IOS, ElementAttribute.LABEL
            )
            expect(edit_profile_page.option_picker_search_field).to_exist()

        with allure.step("Search and select a Spoken Language"):
            edit_profile_page.option_picker_search_field.send_keys(values.FRENCH + "\n")
            edit_profile_page.search_and_verify_language_option_exists(Language.FRENCH)
            edit_profile_page.get_picker_accept_button.click()
            expect(edit_profile_page.spoken_language_picker_button).to_have(values.FRENCH, ElementAttribute.LABEL)

        with allure.step("Click on about me text box"):
            edit_profile_page.user_bio_value.click()
            edit_profile_page.user_bio_value.clear()
            edit_profile_page.user_bio_value.send_keys("Automation Test")
            edit_profile_page.user_bio_label.click()

        with allure.step("click on image upload icon"):
            edit_profile_page.change_profile_img_button.scroll_and_find(scroll_direction=ScrollDirections.DOWN)
            edit_profile_page.change_profile_img_button.click()
            expect(edit_profile_page.change_profile_img_title_label).to_have(
                values.CHANGE_PROFILE_IMAGE_TITLE_LABEL, ElementAttribute.LABEL
            )

        with allure.step("verify buttons appear on change profile image screen"):
            self.verify_button_on_change_profile_img_dialogue()

        with allure.step("click on remove photo button"):
            edit_profile_page.remove_img_button.click()

        with allure.step("verify photo is removed"):
            # TODO: No such info available to verify
            pass

        with allure.step("click on select from gallery"):
            edit_profile_page.change_profile_img_button.click()

        with allure.step("select a photo from gallery"):
            edit_profile_page.select_img_button.click()
            edit_profile_page.select_image_from_gallery()

        with allure.step("click on Done button"):
            if not edit_profile_page.done_button.exists(raise_exception=False):
                edit_profile_page.img_picker_choose_button.click()
            edit_profile_page.img_picker_choose_button.wait_to_disappear()
            edit_profile_page.done_button.click()
            edit_profile_page.img_picker_choose_button.exists(raise_exception=False)

        with allure.step("click on back button"):
            edit_profile_page.back_navigation_button.click()
            expect(profile_page.profile_bio_value).to_have("Automation Test", ElementAttribute.LABEL)

        with allure.step("click on edit profile button"):
            profile_page.edit_profile_button.click()
            expect(edit_profile_page.location_picker_button).to_have(values.CANADA, ElementAttribute.LABEL)
            expect(edit_profile_page.spoken_language_picker_button).to_have(values.FRENCH, ElementAttribute.LABEL)

        with allure.step("Click on switch to limited profile"):
            edit_profile_page.switch_profile_type_button.click()

        with allure.step("verify sub-heading “Limited profile"):
            expect(edit_profile_page.profile_type_label).to_have(
                values.EDIT_PROFILE_TYPE_LIMITED_PROFILE_LABEL_IOS, ElementAttribute.LABEL
            )
            edit_profile_page.find_by_text_on_screen(values.LIMITED_PROFILE_DISCLAIMER_MESSAGE_IOS)

        with allure.step("verify the fields are no longer enabled"):
            expect(edit_profile_page.location_picker_button).not_.to_be_enabled()
            expect(edit_profile_page.spoken_language_picker_button).not_.to_be_enabled()
            expect(edit_profile_page.profile_bio_value).not_.to_be_enabled()

        with allure.step("click on Switch to full profile"):
            edit_profile_page.switch_profile_type_button.click()

        with allure.step("verify sub-heading “Full profile"):
            expect(edit_profile_page.profile_type_label).to_have(
                values.EDIT_PROFILE_TYPE_LABEL_FULL_PROFILE_IOS, ElementAttribute.LABEL
            )

        with allure.step("verify the fields are enabled"):
            pass
            expect(edit_profile_page.location_picker_button).to_be_enabled()
            expect(edit_profile_page.spoken_language_picker_button).to_be_enabled()
            expect(edit_profile_page.user_bio_value).to_be_enabled()

    def test_cleanup_and_restore_original_values(self, set_capabilities: WebDriver | None, setup_logging: Logger):
        """"""
        profile_page = IosProfile()
        edit_profile_page = IosEditProfilePage()

        with allure.step("Change values to original"):
            if profile_page.edit_profile_button.exists(raise_exception=False):
                profile_page.edit_profile_button.click()
            edit_profile_page.location_picker_button.click()
            edit_profile_page.option_picker_search_field.send_keys(values.PROFILE_LOCATION_US_IOS + "\n")
            edit_profile_page.get_picker_accept_button.click()
            expect(edit_profile_page.location_picker_button).to_have(
                values.PROFILE_LOCATION_US_IOS, ElementAttribute.LABEL
            )

            edit_profile_page.spoken_language_picker_button.click()
            edit_profile_page.option_picker_search_field.send_keys(values.ENGLISH + "\n")
            edit_profile_page.get_picker_accept_button.click()
            expect(edit_profile_page.spoken_language_picker_button).to_have(values.ENGLISH, ElementAttribute.LABEL)

        with allure.step("Click on about me text box"):
            edit_profile_page.user_bio_value.click()
            edit_profile_page.user_bio_value.clear()
            edit_profile_page.user_bio_value.send_keys(values.PROFILE_BIO_VALUE)
            edit_profile_page.user_bio_label.click()
            edit_profile_page.done_button.click()
            edit_profile_page.img_picker_choose_button.exists(raise_exception=False)

        with allure.step("click on back button"):
            edit_profile_page.back_navigation_button.click()
