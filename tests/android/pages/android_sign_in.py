"""
Sign In Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidSignIn(AndroidBasePage):
    """
    Sign in screen
    """

    def __init__(self):
        super().__init__()
        self._txt_sign_in_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_sign_in_title")',
        )
        self._sign_in_screen_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_sign_in_description")',
        )
        self._sign_in_email_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_email_label")',
        )
        self._sign_in_password_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_password_label")',
        )
        self._show_password_eye_icon = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Show password")'
        )
        self._sign_in_tf_email = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_email")'
        )
        self._sign_in_tf_password = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_password")'
        )
        self._landing_signin_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_sign_in")'
        )
        self._google_signin_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Sign in with Google")',
        )
        self._facebook_signin_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Sign in with Facebook")',
        )
        self._microsoft_signin_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Sign in with Microsoft")',
        )
        self._sign_in_forgot_password_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_forgot_password")',
        )
        self._forgot_password_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_forgot_password_title")',
        )
        self._forgot_password_reset_button_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_reset_password")',
        )
        self._email_field_error = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_email_error")',
        )
        self._forgot_password_reset_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("btn_reset_password")',
        )
        self._password_field_error = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_password_error")',
        )
        self._check_email_title_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Check your email")'
        )
        self._password_recovery_sign_in_btn = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_sign_in")'
        )
        self._forgot_password_email_placeholder = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_email_placeholder")',
        )

    @property
    def signin_title(self) -> "Element":
        """Get the sign-in title element.

        Returns
            Element: The Element object representing the sign-in title
        """

        return self._txt_sign_in_title

    @property
    def show_password_eye_icon(self) -> "Element":
        """Get the show password eye icon title element.

        Returns
            Element: The Element object representing the sign-in title
        """

        return self._show_password_eye_icon

    @property
    def sign_in_description(self) -> Element:
        """Get sign in description

        Returns:
            Element: sign in description element
        """

        return self._sign_in_screen_description

    @property
    def sign_in_email_label(self) -> Element:
        """Get sign in email label

        Returns:
            Element: sign in email label element
        """

        return self._sign_in_email_label

    @property
    def forgot_password_email_label(self) -> Element:
        """Get sign in email label

        Returns:
            Element: sign in email label element
        """

        return self._sign_in_email_label

    @property
    def sign_in_tf_email(self) -> Element:
        """Get sign in email text field

        Returns:
            Element: sign in email text field element
        """

        return self._sign_in_tf_email

    @property
    def sign_in_password_label(self) -> Element:
        """Get sign in password label

        Returns:
            Element: sign in password label element
        """

        return self._sign_in_password_label

    @property
    def sign_in_password_field(self) -> Element:
        """Get sign in password field

        Returns:
            Element: sign in password field element
        """

        return self._sign_in_tf_password

    @property
    def forgot_password_button(self) -> Element:
        """Get sign in forgot password

        Returns:
            Element: sign in forgot password element
        """

        return self._sign_in_forgot_password_button

    @property
    def google_auth_button(self) -> Element:
        """Get google auth button

        Returns:
            Element: google auth button element
        """

        return self._google_signin_button

    @property
    def get_facebook_auth_button(self) -> Element:
        """Get facebook auth button

        Returns:
            Element: facebook auth button element
        """

        return self._facebook_signin_button

    @property
    def get_microsoft_auth_button(self) -> Element:
        """Get microsoft auth button

        Returns:
            Element: microsoft auth button element
        """

        return self._microsoft_signin_button

    @property
    def signin_button(self) -> Element:
        """Get signin button

        Returns:
            Element: Signin button element
        """

        return self._landing_signin_button

    @property
    def forgot_password_title(self) -> Element:
        """Get forgot password title

        Returns:
            Element: forgot password title element
        """

        return self._forgot_password_title

    @property
    def forgot_password_reset_button(self) -> Element:
        """Get forgot password reset button

        Returns:
            Element: forgot password reset button element
        """

        return self._forgot_password_reset_button

    @property
    def forgot_password_reset_button_label(self) -> Element:
        """Get forgot password reset button

        Returns:
            Element: forgot password reset button element
        """

        return self._forgot_password_reset_button_text

    @property
    def email_field_error(self) -> Element:
        """Get forgot password email error

        Returns:
            Element: forgot password email error element
        """

        return self._email_field_error

    @property
    def password_field_error(self) -> Element:
        """Get forgot password email error

        Returns:
            Element: forgot password email error element
        """

        return self._password_field_error

    @property
    def password_recovery_sign_in_btn(self) -> Element:
        """Get password recovery sign in button

        Returns:
            Element: password recovery sign in button element
        """

        return self._password_recovery_sign_in_btn

    @property
    def forgot_password_email_placeholder(self) -> Element:
        """Get forgot password email placeholder

        Returns:
            Element: forgot password email placeholder element
        """

        return self._forgot_password_email_placeholder
