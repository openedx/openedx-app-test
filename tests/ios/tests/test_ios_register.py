"""
Register Screen Test Module
"""

from tests.common import values
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

        setup_logging.info("Starting Test Case")
        register_page = IosRegister(set_capabilities, setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)

        if ios_landing.get_allow_notifications_button():
            ios_landing.get_allow_notifications_button().click()
        register_button = register_page.get_register_button()
        assert register_page.get_register_button().text == values.REGISTER
        register_button.click()

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

        register_page = IosRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)
        ios_login = IosLogin(set_capabilities, setup_logging)

        assert register_page.get_register_screen_heading().text == values.REGISTER
        back_button = ios_landing.get_header_back_button()
        assert back_button.text == values.LANDING_BACK_BUTTON
        sign_up_heading = register_page.get_signup_text()
        assert sign_up_heading.text == values.REGISTER

        create_account_message = register_page.get_signup_subtitle_text()
        assert create_account_message.text == values.REGISTER_CREATE_ACCOUNT_MESSAGE

        full_name_title = register_page.get_name_text()
        assert full_name_title.text == values.REGISTER_FULL_NAME_TITLE

        name_textfield = register_page.get_name_textfield()
        assert name_textfield.get_attribute("visible") == values.TRUE_LOWERCASE

        name_instructions_text = register_page.get_name_instructions_text()
        assert name_instructions_text.text == values.REGISTER_FULL_NAME_MESSAGE

        user_name_content = register_page.get_username_text()
        assert user_name_content.text == values.REGISTER_PUBLIC_USERNAME_TITLE

        username_textfield = register_page.get_username_textfield()
        assert username_textfield.get_attribute("visible") == values.TRUE_LOWERCASE

        username_instructions_text = register_page.get_username_instructions_text()
        assert username_instructions_text.text == values.REGISTER_PUBLIC_USERNAME_MESSAGE

        email_text = register_page.get_email_text()
        assert email_text.text == values.REGISTER_EMAIL_TITLE

        email_textfield = register_page.get_email_textfield()
        assert email_textfield.get_attribute("visible") == values.TRUE_LOWERCASE

        email_instructions_text = register_page.get_email_instructions_text()
        assert email_instructions_text.text == values.REGISTER_EMAIL_MESSAGE

        password_text = register_page.get_password_text()
        assert password_text.text == values.REGISTER_PASSWORD_TITLE

        password_text_field = register_page.get_password_textfield()
        assert password_text_field.get_attribute("visible") == values.TRUE_LOWERCASE

        password_instructions_text = register_page.get_password_instructions_text()
        assert password_instructions_text.text == values.REGISTER_PASSWORD_MESSAGE

        country_text = register_page.get_country_text()
        assert country_text.text == values.REGISTER_COUNTRY_TITLE

        country_textfield = register_page.get_country_textfield()
        assert country_textfield

        country_instructions_text = register_page.get_country_instructions_text()
        assert country_instructions_text.text == values.REGISTER_COUNTRY_MESSAGE

        show_optional_fields = register_page.get_show_optional_fields()
        assert show_optional_fields.text == values.REGISTER_SHOW_OPTIONAL_FIELDS

        register_button = register_page.get_create_account_button()
        assert register_button.text == values.REGISTER_CREATE_ACCOUNT_BUTTON

        social_auth_title_text = register_page.get_social_auth_title_text()
        assert social_auth_title_text.text == values.REGISTER_OPTIONS_TITLE

        global_contents.scroll_from_element(set_capabilities, password_text_field)

        google_signin = ios_login.get_signin_social_auth_google_button()
        assert google_signin.text == values.REGISTER_GOOGLE_SIGNUP

        facebook_signin = ios_login.get_signin_social_auth_facebook_button()
        assert facebook_signin.text == values.REGISTER_FACEBOOK_SIGNUP

        microsoft_signin = ios_login.get_signin_social_auth_microsoft_button()
        assert microsoft_signin.text == values.REGISTER_MICROSOFT_SIGNUP

        apple_signin = ios_login.get_signin_social_auth_apple_button()
        assert apple_signin.text == values.REGISTER_APPLE_SIGNUP

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

        register_page = IosRegister(set_capabilities, setup_logging)
        global_contents = Globals(setup_logging)
        whats_new_page = IosWhatsNew(set_capabilities, setup_logging)

        user_name = global_contents.generate_random_credentials(5)
        email = user_name + "@example.com"
        first_name = global_contents.generate_random_credentials(4)
        last_name = global_contents.generate_random_credentials(4)
        full_name = first_name + " " + last_name
        password = "qwERt12#$5" + global_contents.generate_random_credentials(8)

        name_textfield = register_page.get_name_textfield()
        username_textfield = register_page.get_username_textfield()
        email_textfield = register_page.get_email_textfield()
        register_button = register_page.get_create_account_button()

        name_textfield.send_keys(full_name)
        username_textfield.send_keys(user_name)
        email_textfield.click()
        email_textfield.send_keys(email)

        password_field = register_page.get_password_textfield()
        password_field.send_keys(password)

        global_contents.scroll_screen(set_capabilities, register_button, name_textfield)
        country_textfield = register_page.get_country_textfield()
        country_textfield.click()
        picker_title_text = register_page.get_picker_title_text()
        assert picker_title_text.text == values.REGISTER_COUNTRY_PICKER_TITLE

        country_field = register_page.select_country()
        assert country_field
        country_field.click()
        country_field.send_keys(values.REGISTER_COUNTRY_SELECT)

        accept_button = register_page.get_picker_accept_button()
        assert accept_button.text == values.REGISTER_COUNTRY_ACCEPT_BUTTON
        accept_button.click()
        country_textfield = register_page.get_country_textfield()
        assert country_textfield.text == values.REGISTER_COUNTRY_SELECT

        register_button.click()
        password_instructions_text = register_page.get_password_instructions_text()
        assert password_instructions_text.text == values.REGISTER_PASSWORD_MESSAGE

        if global_contents.whats_new_enable:
            assert whats_new_page.navigate_features().text == "Done"
            whats_new_page.get_next_btn().click()
            setup_logging.info("Whats New screen is successfully loaded")

        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)
        discover_tab = main_dashboard.get_main_dashboard_discover_tab()
        assert discover_tab.text == values.DISCOVER_SCREEN_HEADING

    def test_sign_out_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify that clicking logout button should load logout dialog
            Verify that tapping close button should leave logout dialog
            Verify that tapping logout button should logout from main dashboard screen
        """

        ios_profile = IosProfile(set_capabilities, setup_logging)
        ios_landing = IosLanding(set_capabilities, setup_logging)
        main_dashboard = IosMainDashboard(set_capabilities, setup_logging)

        profile_tab = main_dashboard.get_main_dashboard_profile_tab()
        assert profile_tab.text == values.MAIN_DASHBOARD_PROFILE_TAB
        profile_tab.click()
        assert ios_profile.get_profile_settings_button().text == values.PROFILE_SETTINGS_TEXT
        ios_profile.get_profile_settings_button().click()
        assert ios_profile.get_profile_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_profile_logout_button().click()
        assert ios_profile.get_logout_close_button().text == "Close"
        assert ios_profile.get_logout_dialog_title().text == values.LOGOUT_DIALOG_TITLE
        assert ios_profile.get_logout_button().text.lower() == values.PROFILE_LOGOUT_BUTTON
        ios_profile.get_logout_button().click()
        assert ios_landing.get_welcome_message().text == values.LANDING_MESSAGE
