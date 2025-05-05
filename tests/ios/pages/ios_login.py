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
        self._signin_username_text = Element(AppiumBy.ACCESSIBILITY_ID, "username_text")
        self._signin_username_text_field = Element(AppiumBy.ACCESSIBILITY_ID, "username_textfield")
        self._signin_password_text = Element(AppiumBy.ACCESSIBILITY_ID, "password_text")
        self._signin_password_text_field = Element(AppiumBy.ACCESSIBILITY_ID, "password_textfield")
        self._signin_forgot_password_button = Element(AppiumBy.ACCESSIBILITY_ID, "forgot_password_button")
        self._signin_button = Element(AppiumBy.ACCESSIBILITY_ID, "signin_button")
        self._signin_social_auth_title_text = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_title_text")
        self._signin_social_auth_google_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_google_button")
        self._signin_social_auth_facebook_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_facebook_button")
        self._signin_social_auth_microsoft_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_microsoft_button")
        self._signin_social_auth_apple_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_apple_button")
        self._forgot_title_text = Element(AppiumBy.ACCESSIBILITY_ID, "forgot_title_text")
        self._forgot_description_text = Element(AppiumBy.ACCESSIBILITY_ID, "forgot_description_text")
        self._forgot_email_text = Element(AppiumBy.ACCESSIBILITY_ID, "email_text")
        self._forgot_email_text_field = Element(AppiumBy.ACCESSIBILITY_ID, "email_textfield")
        self._reset_password_button = Element(AppiumBy.ACCESSIBILITY_ID, "reset_password_button")
        self._check_email_image = Element(AppiumBy.ACCESSIBILITY_ID, "check_email_image")
        self._recover_title_text = Element(AppiumBy.ACCESSIBILITY_ID, "recover_title_text")
        self._recover_description_text = Element(AppiumBy.ACCESSIBILITY_ID, "recover_description_text")

    @property
    def sign_in_title(self) -> Element:
        """
        Get Sing In

        Returns:
            webdriver element: Sing In Element
        """

        return self._sign_in_title

    @property
    def password_field(self) -> Element:
        """
        Get password fields element

        Returns:
            webdriver element: editfield element
        """

        return self._password_field

    @property
    def signin_welcome_text(self) -> Element:
        """
        Get Sing In welcome text

        Returns:
            webdriver element: Singin welcome text element
        """

        return self._signin_welcome_text

    @property
    def signin_username_text(self) -> Element:
        """
        Get username text

        Returns:
            webdriver element: username text element
        """

        return self._signin_username_text

    @property
    def signin_username_textfield(self) -> Element:
        """
        Get username textfield

        Returns:
            webdriver element: username textfield element
        """

        return self._signin_username_text_field.find_all()[1]

    @property
    def signin_password_text(self) -> Element:
        """
        Get password text

        Returns:
            webdriver element: password text element
        """

        return self._signin_password_text

    @property
    def signin_password_textfield(self) -> Element:
        """
        Get password textfield

        Returns:
            webdriver element: password textfield element
        """

        return self._signin_password_text_field.find_all()[1]

    @property
    def get_signin_forgot_password_button(self) -> Element:
        """
        Get forgot password button

        Returns:
            webdriver element: forgot password button element
        """

        return self._signin_forgot_password_button

    @property
    def signin_button(self) -> Element:
        """
        Get signin button

        Returns:
            webdriver element: signin button element
        """

        return self._signin_button

    @property
    def signin_social_auth_title_text(self) -> Element:
        """
        Get social auth title text

        Returns:
            webdriver element: social auth title text element
        """

        return self._signin_social_auth_title_text

    @property
    def signin_social_auth_google_button(self) -> Element:
        """
        Get social auth google button text

        Returns:
            webdriver element: signin social auth google button
        """

        return self._signin_social_auth_google_button

    @property
    def signin_social_auth_facebook_button(self) -> Element:
        """
        Get social auth facebook button text

        Returns:
            webdriver element: signin social auth facebook button
        """

        return self._signin_social_auth_facebook_button

    @property
    def signin_social_auth_microsoft_button(self) -> Element:
        """
        Get social auth microsoft button text

        Returns:
            webdriver element: signin social auth microsoft button
        """
        return self._signin_social_auth_microsoft_button

    @property
    def signin_social_auth_apple_button(self) -> Element:
        """
        Get social auth apple button text

        Returns:
            webdriver element: signin social auth apple button
        """

        return self._signin_social_auth_apple_button

    @property
    def forgot_title_text(self) -> Element:
        """
        Get forgot title text

        Returns:
            webdriver element: forgot title text element
        """

        return self._forgot_title_text

    @property
    def forgot_description_text(self) -> Element:
        """
        Get forgot description text

        Returns:
            webdriver element: forgot description text element
        """

        return self._forgot_description_text

    @property
    def forgot_email_text(self) -> Element:
        """
        Get forgot email text

        Returns:
            webdriver element: forgot email text element
        """

        return self._forgot_email_text

    @property
    def forgot_email_textfield(self) -> Element:
        """
        Get forgot email textfield

        Returns:
            webdriver element: forgot email textfield element
        """

        return self._forgot_email_text_field.find_all()[1]

    @property
    def forgot_reset_password_button(self) -> Element:
        """
        Get forgot reset password button

        Returns:
            webdriver element: forgot reset password button element
        """

        return self._reset_password_button

    @property
    def forgot_check_email_image(self) -> Element:
        """
        Get forgot check email image

        Returns:
            webdriver element: forgot check email image element
        """

        return self._check_email_image

    @property
    def forgot_recover_title_text(self) -> Element:
        """
        Get forgot recover title text

        Returns:
            webdriver element: forgot recover title text element
        """

        return self._recover_title_text

    @property
    def forgot_recover_description_text(self) -> Element:
        """
        Get forgot recover description text

        Returns:
            webdriver element: forgot recover description text element
        """

        return self._recover_description_text
