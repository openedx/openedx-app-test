"""
Login Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy
from framework import Element
from tests.ios.pages.ios_base_page import IosBasePage


class IosLogin(IosBasePage):
    """
    Login screen
    """

    def __init__(self):
        super().__init__()
        self._back_button_navigation = Element(AppiumBy.ACCESSIBILITY_ID, "back_button")
        self._notification_allow_button = Element(AppiumBy.ACCESSIBILITY_ID, "Allow")
        self._password_field = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeSecureTextField")
        self._sign_in_title = Element(AppiumBy.ACCESSIBILITY_ID, "signin_text")
        self._signin_welcome_text = Element(AppiumBy.ACCESSIBILITY_ID, "welcome_back_text")
        self._username_text_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "username_text")
        self._username_text_field_placeholder = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'username_textfield'`]"
        )
        self._username_text_field = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeTextField[`name == 'username_textfield'`]"
        )
        self._password_text_label = Element(AppiumBy.ACCESSIBILITY_ID, "password_text")
        self._password_test_field_placeholder = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'password_textfield'`]"
        )
        self._password_text_field = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeSecureTextField[`name == 'password_textfield'`]"
        )
        self._signin_forgot_password_button = Element(AppiumBy.ACCESSIBILITY_ID, "forgot_password_button")
        self._signin_button = Element(AppiumBy.ACCESSIBILITY_ID, "signin_button")
        self._signin_social_auth_title_text = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_title_text")
        self._signin_social_auth_google_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_google_button")
        self._signin_social_auth_facebook_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_facebook_button")
        self._signin_social_auth_microsoft_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_microsoft_button")
        self._signin_social_auth_apple_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_apple_button")
        self._forgot_title_text = Element(AppiumBy.ACCESSIBILITY_ID, "forgot_title_text")
        self._forgot_description_text = Element(AppiumBy.ACCESSIBILITY_ID, "forgot_description_text")
        self._forgot_email_text_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "email_text")
        self._forgot_email_text_field = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeTextField[`name == 'email_textfield'`]"
        )
        self._forgot_email_text_field_placeholder = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'email_textfield'`]"
        )
        self._reset_password_button = Element(AppiumBy.ACCESSIBILITY_ID, "reset_password_button")
        self._check_email_image = Element(AppiumBy.ACCESSIBILITY_ID, "check_email_image")
        self._recover_title_text = Element(AppiumBy.ACCESSIBILITY_ID, "recover_title_text")
        self._recover_description_text = Element(AppiumBy.ACCESSIBILITY_ID, "recover_description_text")
        self._invalid_credentials_message = Element(AppiumBy.ACCESSIBILITY_ID, "snackbar_text")
        self._password_field_eye_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'password_textfield'`]"
        )

    @property
    def password_field_eye_button(self) -> Element:
        """
        Get password text field eye button element

        Returns:
            Element: password text field eye button element
        """

        return self._password_field_eye_button

    @property
    def sign_in_title(self) -> Element:
        """
        Get Sing In

        Returns:
            Element: Sing In Element
        """

        return self._sign_in_title

    @property
    def password_field(self) -> Element:
        """
        Get password fields element

        Returns:
            Element: editfield element
        """

        return self._password_field

    @property
    def signin_welcome_text(self) -> Element:
        """
        Get Sing In welcome text

        Returns:
            Element: Signin welcome text element
        """

        return self._signin_welcome_text

    @property
    def username_text_field_label(self) -> Element:
        """
        Get username text

        Returns:
            Element: username text element
        """

        return self._username_text_field_label

    @property
    def username_textfield(self) -> Element:
        """
        Get username textfield

        Returns:
            Element: username textfield element
        """

        return self._username_text_field

    @property
    def username_text_field_placeholder(self) -> Element:
        """
        Get username textfield

        Returns:
            Element: username textfield element
        """

        return self._username_text_field_placeholder

    @property
    def password_text_field_label(self) -> Element:
        """
        Get password label

        Returns:
            Element: password label element
        """

        return self._password_text_label

    @property
    def password_textfield(self) -> Element:
        """
        Get password textfield

        Returns:
            Element: password textfield element
        """

        return self._password_text_field

    @property
    def password_textfield_placeholder(self) -> Element:
        """
        Get password textfield placeholder

        Returns:
            Element: password textfield placeholder element
        """

        return self._password_test_field_placeholder

    @property
    def get_signin_forgot_password_button(self) -> Element:
        """
        Get forgot password button

        Returns:
            Element: forgot password button element
        """

        return self._signin_forgot_password_button

    @property
    def signin_button(self) -> Element:
        """
        Get signin button

        Returns:
            Element: signin button element
        """

        return self._signin_button

    @property
    def signin_social_auth_title_text(self) -> Element:
        """
        Get social auth title text

        Returns:
            Element: social auth title text element
        """

        return self._signin_social_auth_title_text

    @property
    def signin_social_auth_google_button(self) -> Element:
        """
        Get social auth google button text

        Returns:
            Element: signin social auth google button
        """

        return self._signin_social_auth_google_button

    @property
    def signin_social_auth_facebook_button(self) -> Element:
        """
        Get social auth facebook button text

        Returns:
            Element: signin social auth facebook button
        """

        return self._signin_social_auth_facebook_button

    @property
    def signin_social_auth_microsoft_button(self) -> Element:
        """
        Get social auth microsoft button text

        Returns:
            Element: signin social auth microsoft button
        """
        return self._signin_social_auth_microsoft_button

    @property
    def signin_social_auth_apple_button(self) -> Element:
        """
        Get social auth apple button text

        Returns:
            Element: signin social auth apple button
        """

        return self._signin_social_auth_apple_button

    @property
    def forgot_title_text(self) -> Element:
        """
        Get forgot title text

        Returns:
            Element: forgot title text element
        """

        return self._forgot_title_text

    @property
    def forgot_description_text(self) -> Element:
        """
        Get forgot description text

        Returns:
            Element: forgot description text element
        """

        return self._forgot_description_text

    @property
    def forgot_email_text_field_label(self) -> Element:
        """
        Get forgot email text

        Returns:
            Element: forgot email text element
        """

        return self._forgot_email_text_field_label

    @property
    def forgot_email_textfield(self) -> Element:
        """
        Get forgot email textfield

        Returns:
            Element: forgot email textfield element
        """

        return self._forgot_email_text_field

    @property
    def forgot_email_textfield_placeholder(self) -> Element:
        """
        Get forgot email textfield placeholder

        Returns:
            Element: forgot email textfield placeholder element
        """

        return self._forgot_email_text_field_placeholder

    @property
    def reset_password_button(self) -> Element:
        """
        Get forgot reset password button

        Returns:
            Element: forgot reset password button element
        """

        return self._reset_password_button

    @property
    def forgot_check_email_image(self) -> Element:
        """
        Get forgot check email image

        Returns:
            Element: forgot check email image element
        """

        return self._check_email_image

    @property
    def forgot_recover_title_text(self) -> Element:
        """
        Get forgot recover title text

        Returns:
            Element: forgot recover title text element
        """

        return self._recover_title_text

    @property
    def forgot_recover_description_text(self) -> Element:
        """
        Get forgot recover description text

        Returns:
            Element: forgot recover description text element
        """

        return self._recover_description_text

    @property
    def invalid_credentials_message(self) -> Element:
        """
        Get invalid credentials message

        Returns:
            Element: invalid credentials message element
        """

        return self.snackbar_text_message

    @property
    def invalid_email_message(self) -> Element:
        """
        Get invalid credentials title

        Returns:
            Element: invalid credentials title element
        """

        return self.snackbar_text_message
