"""
Register Screen Test Module
"""
from framework import expect, Element
from tests.common import values
from tests.common.enums import ElementAttribute
from tests.common.globals import Globals
from tests.ios.pages.ios_landing import IosLanding
from tests.ios.pages.ios_login import IosLogin
from tests.ios.pages.ios_main_dashboard import IosMainDashboard
from tests.ios.pages.ios_profile import IosProfile
from tests.ios.pages.ios_register import IosRegister
from tests.ios.pages.ios_whats_new import IosWhatsNew


class TestIosRegister:
    """
    Register screen's Test Case
    """

    def test_load_register_screen(self, set_capabilities, setup_logging):
        """
        Scenario:
            Verify Register screen is loaded successfully
        """
        Element.set_driver(set_capabilities)
        Element.set_logger(setup_logging)
        setup_logging.info("Starting Test Case")
        register_page = IosRegister()
        ios_landing = IosLanding()
        if ios_landing.allow_notifications_button.exists():
            ios_landing.allow_notifications_button.click()
        register_button = IosRegister.get_register_button()
        expect(register_page.get_register_button).to_have(values.REGISTER)
        assert register_button.click()

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify following contents are visible on screen,
                "Back icon", "Sign In" Title, "Username or e-mail address" label, Username edit-field
                Password edit-field, "Forgot your password?" option, "Sign In" button,
                "Or sing in with" label, "Facebook" button, "Google" button
            Verify all screen contents have their default values
            Verify all fields are editable
        """
        Element.set_logger(setup_logging)
        Element.set_driver(set_capabilities)
        register_page = IosRegister()
        ios_landing = IosLanding()
        ios_login = IosLogin()

        expect(register_page.get_register_screen_heading).to_have(values.REGISTER)
        back_button = ios_landing.back_navigation_button
        expect(back_button).to_have(values.LANDING_BACK_BUTTON)
        sign_up_heading = register_page.get_signup_text
        expect(sign_up_heading).to_have(values.REGISTER)
        expect(register_page.get_signup_subtitle_text).to_have(values.REGISTER_CREATE_ACCOUNT_MESSAGE)
        expect(register_page.get_name_text).to_have(values.REGISTER_FULL_NAME_TITLE)
        expect(register_page.get_name_textfield).to_be_visible()
        expect(register_page.get_name_instructions_text).to_have(values.REGISTER_FULL_NAME_MESSAGE)

        expect(register_page.get_username_text).to_have(values.REGISTER_PUBLIC_USERNAME_TITLE)
        expect(register_page.get_username_textfield).to_be_visible()
        expect(register_page.get_username_instructions_text).to_have(values.REGISTER_PUBLIC_USERNAME_MESSAGE)
        expect(register_page.get_email_text).to_have(values.REGISTER_EMAIL_TITLE)
        expect(register_page.get_email_textfield).to_be_visible()
        expect(register_page.get_email_instructions_text).to_have(values.REGISTER_EMAIL_MESSAGE)
        expect(register_page.get_password_text).to_have(values.REGISTER_PASSWORD_TITLE)
        expect(register_page.get_password_textfield).to_be_visible()
        password_instructions_text = register_page.get_password_instructions_text
        expect(password_instructions_text).to_have(values.REGISTER_PASSWORD_MESSAGE)
        expect(register_page.get_country_text).to_have(values.REGISTER_COUNTRY_TITLE)
        assert register_page.get_country_textfield.exists()
        country_instructions_text = register_page.get_country_instructions_text
        expect(country_instructions_text).to_have(values.REGISTER_COUNTRY_MESSAGE)
        expect(register_page.get_show_optional_fields).to_have(values.REGISTER_SHOW_OPTIONAL_FIELDS)
        register_button = register_page.get_create_account_button
        expect(register_button).to_have(values.REGISTER_CREATE_ACCOUNT_BUTTON)
        social_auth_title_text = register_page.get_social_auth_title_text
        expect(social_auth_title_text).to_have(values.REGISTER_OPTIONS_TITLE)
        register_page.get_password_textfield.scroll_vertically_from_element()
        expect(ios_login.signin_social_auth_title_text).to_have(values.REGISTER_OPTIONS_TITLE)
        expect(ios_login.signin_social_auth_google_button).to_have(values.GOOGLE_SIGNIN)
        expect(ios_login.signin_social_auth_facebook_button).to_have(values.FACEBOOK_SIGNIN)
        expect(ios_login.signin_social_auth_microsoft_button).to_have(values.MICROSOFT_SIGNIN)
        expect(ios_login.signin_social_auth_apple_button).to_have(values.APPLE_SIGNIN)

    def test_register_smoke(self, set_capabilities, setup_logging):
        """
        Verify that tapping "Create your account" button after filling all required input(valid) types,
            will validate all inputs and load "Whats new feature screen" with specific user logged in
        Verify that tapping "Create your account" button after filling all required input(valid) types,
            will validate all inputs and load "Whats new feature screen" with specific user logged in
        Verify that following input types are optional,
            "Gender" spinner
            "Highest level of education completed" spinner
        Verify that user should be able to log out and re-login with new created account credentials
        Verify that for new user there must be "Looking for new challenge?" heading is available on the screen
        """

        Element.set_logger(setup_logging)
        Element.set_driver(set_capabilities)
        register_page = IosRegister()
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew()

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + "@example.com"
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = first_name + " " + last_name
        password = "qwERt12#$5" + global_contents.generate_random_credentials(8)

        name_textfield = register_page.get_name_textfield
        username_textfield = register_page.get_username_textfield
        email_textfield = register_page.get_email_textfield
        register_button = register_page.get_create_account_button
        assert name_textfield.send_keys(full_name)
        assert username_textfield.send_keys(user_name)
        assert email_textfield.click()
        assert email_textfield.send_keys(email)
        assert register_page.get_password_textfield.send_keys(password)
        register_button.scroll_vertically_from_element()
        assert register_page.get_country_textfield.click()
        picker_title_text = register_page.get_picker_title_text
        expect(picker_title_text).to_have(values.REGISTER_COUNTRY_PICKER_TITLE)
        country_field = register_page.select_country
        assert country_field.exists()
        assert country_field.click()
        assert country_field.send_keys(values.REGISTER_COUNTRY_SELECT)
        accept_button = register_page.get_picker_accept_button
        expect(accept_button).to_have(values.REGISTER_COUNTRY_ACCEPT_BUTTON)
        assert accept_button.click()
        expect(register_page.get_country_textfield).to_have(values.REGISTER_COUNTRY_SELECT)
        register_button.click()
        expect(register_page.get_password_instructions_text).to_have(values.REGISTER_PASSWORD_MESSAGE)
        if global_contents.whats_new_enable:
            expect(whats_new_page.navigate_features()).to_have("Done")
            assert whats_new_page.whats_new_next_button.click()
            setup_logging.info("Whats New screen is successfully loaded")

        main_dashboard = IosMainDashboard()
        discover_tab = main_dashboard.main_dashboard_discover_tab
        expect(discover_tab).to_have(values.IOS_SELECTED_TAB_VALUE, ElementAttribute.VALUE)

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should log out from main dashboard screen
        """

        Element.set_logger(setup_logging)
        Element.set_driver(set_capabilities)
        ios_profile = IosProfile()
        ios_landing = IosLanding()
        main_dashboard = IosMainDashboard()

        profile_tab = main_dashboard.profile_tab
        expect(profile_tab).to_have(values.MAIN_DASHBOARD_PROFILE_TAB)
        assert profile_tab.click()
        expect(ios_profile.profile_settings_button).to_have(values.PROFILE_SETTINGS_TEXT)
        assert ios_profile.profile_settings_button.click()
        expect(ios_profile.get_profile_logout_button).to_have(values.PROFILE_LOGOUT_BUTTON, case="lower")
        assert ios_profile.get_profile_logout_button.click()
        expect(ios_profile.get_logout_close_button).to_have("Close")
        expect(ios_profile.get_logout_dialog_title).to_have(values.LOGOUT_DIALOG_TITLE)
        expect(ios_profile.get_logout_button_from_prompt).to_have(values.PROFILE_LOGOUT_BUTTON, case="lower")
        assert ios_profile.get_logout_button_from_prompt.click()
        expect(ios_landing.get_welcome_message).to_have(values.LANDING_MESSAGE)
