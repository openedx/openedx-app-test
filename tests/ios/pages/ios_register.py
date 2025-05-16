"""
Login Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.ios.pages.ios_base_page import IosBasePage


class IosRegister(IosBasePage):
    """
    Register screen
    """

    def __init__(self):
        super().__init__()
        self._signin_password_text_field = Element(AppiumBy.ACCESSIBILITY_ID, "password_textfield")
        self._password_field = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeSecureTextField")
        self._signin_social_auth_title_text = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_title_text")
        self._register_name_text = Element(AppiumBy.ACCESSIBILITY_ID, "name_text")
        self._register_name_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "name_textfield")
        self._register_name_instructions_text = Element(AppiumBy.ACCESSIBILITY_ID, "name_instructions_text")
        self._register_username_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "username_textfield")
        self._register_email_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "email_textfield")
        self._register_password_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "password_textfield")
        self._register_password_text = Element(AppiumBy.ACCESSIBILITY_ID, "password_text")
        self._register_email_instructions_text = Element(AppiumBy.ACCESSIBILITY_ID, "email_instructions_text")
        self._register_country_text = Element(AppiumBy.ACCESSIBILITY_ID, "country_text")
        self._register_country_picker_button = Element(AppiumBy.ACCESSIBILITY_ID, "country_picker_button")
        self._create_account_button = Element(AppiumBy.ACCESSIBILITY_ID, "signup_button")
        self._register_screen_heading = Element(AppiumBy.ACCESSIBILITY_ID, "register_text")
        self._register_signup_text = Element(AppiumBy.ACCESSIBILITY_ID, "signup_text")
        self._signup_subtitle_text = Element(AppiumBy.ACCESSIBILITY_ID, "signup_subtitle_text")
        self._register_username_text = Element(AppiumBy.ACCESSIBILITY_ID, "username_text")
        self._register_country_picker_title = Element(AppiumBy.ACCESSIBILITY_ID, "picker_title_text")
        self._picker_search_textfield = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`name == "picker_search_textfield"`]'
        )
        self._register_picker_accept_button = Element(AppiumBy.NAME, "picker_accept_button")
        self._register_password_instructions_text = Element(AppiumBy.NAME, "password_instructions_text")
        self._register_country_instructions_text = Element(AppiumBy.NAME, "country_instructions_text")
        self._register_show_optional_fields = Element(AppiumBy.NAME, "optional_fields_text")
        self._register_username_instructions_text = Element(AppiumBy.NAME, "username_instructions_text")
        self._register_email_text = Element(AppiumBy.NAME, "email_text")
        self._register_screen_title = Element(AppiumBy.ACCESSIBILITY_ID, "register_text")
        self._marketing_checkbox_selected = Element(AppiumBy.ACCESSIBILITY_ID, "checkmark.square.fill")
        self._marketing_checkbox_unselected = Element(AppiumBy.ACCESSIBILITY_ID, "square")

    @property
    def get_register_screen_heading(self) -> Element:
        """
        Get register screen heading

        Returns:
            webdriver element: Register screen heading Element
        """

        return self._register_screen_heading

    @property
    def password_field(self) -> Element:
        """
        Get password fields element

        Returns:
            webdriver element: editfield element
        """

        return self._password_field

    @property
    def get_signup_text(self) -> Element:
        """
        Get signup text

        Returns:
            webdriver element: signup text element
        """

        return self._register_signup_text

    @property
    def get_signup_subtitle_text(self) -> Element:
        """
        Get signup subtitle text

        Returns:
            webdriver element: signup subtitle text element
        """

        return self._signup_subtitle_text

    @property
    def get_name_text(self) -> Element:
        """
        Get name text

        Returns:
            webdriver element: name text element
        """

        return self._register_name_text

    @property
    def get_name_textfield(self) -> Element:
        """
        Get name textfield

        Returns:
            webdriver element: name textfield element
        """

        return self._register_name_textfield

    @property
    def get_name_instructions_text(self) -> Element:
        """
        Get name instructions text

        Returns:
            webdriver element: name instructions text element
        """

        return self._register_name_instructions_text

    @property
    def get_username_text(self) -> Element:
        """
        Get username text

        Returns:
            webdriver element: username text element
        """

        return self._register_username_text

    @property
    def get_username_textfield(self) -> Element:
        """
        Get username textfield

        Returns:
            webdriver element: username textfield element
        """

        return self._register_username_textfield

    @property
    def get_username_instructions_text(self) -> Element:
        """
        Get username instructions text

        Returns:
            webdriver element: username instructions text element
        """

        return self._register_username_instructions_text

    @property
    def get_email_text(self) -> Element:
        """
        Get email text

        Returns:
            webdriver element: email text element
        """

        return self._register_email_text

    @property
    def get_email_textfield(self) -> Element:
        """
        Get email textfield

        Returns:
            webdriver element: email textfield element
        """

        return self._register_email_textfield

    @property
    def get_email_instructions_text(self) -> Element:
        """
        Get email instructions text

        Returns:
            webdriver element: email instructions text element
        """

        return self._register_email_instructions_text

    @property
    def get_password_text(self) -> Element:
        """
        Get password text

        Returns:
            webdriver element: password text element
        """

        return self._register_password_text

    @property
    def get_password_textfield(self) -> Element:
        """
        Get password textfield

        Returns:
            webdriver element: password textfield element
        """

        return self._register_password_textfield

    @property
    def get_password_instructions_text(self) -> Element:
        """
        Get password instructions text

        Returns:
            webdriver element: password instructions text element
        """

        return self._register_password_instructions_text

    @property
    def get_country_text(self) -> Element:
        """
        Get country text

        Returns:
            webdriver element: country text element
        """

        return self._register_country_text

    @property
    def get_country_textfield(self):
        """
        Get country textfield

        Returns:
            webdriver element: country textfield element
        """

        return self._register_country_picker_button

    @property
    def get_country_instructions_text(self) -> Element:
        """
        Get country instructions text

        Returns:
            webdriver element: country instructions text element
        """

        return self._register_country_instructions_text

    @property
    def get_show_optional_fields(self):
        """
        Get show optional fields

        Returns:
            webdriver element: show optional fields element
        """

        return self._register_show_optional_fields

    @property
    def create_account_button(self) -> Element:
        """
        Get create account button

        Returns:
            webdriver element: create account button element
        """

        return self._create_account_button

    @property
    def get_social_auth_title_text(self) -> Element:
        """
        Get social auth title text

        Returns:
            webdriver element: social auth title text element
        """

        return self._signin_social_auth_title_text

    @property
    def select_country(self) -> Element:
        """
        Get country spinner

        Returns:
            webdriver elements: country search field
        """

        return self._picker_search_textfield

    @property
    def get_picker_accept_button(self):
        """
        Get picker accept button

        Returns:
            webdriver elements: picker accept button
        """

        return self._register_picker_accept_button

    @property
    def get_picker_title_text(self) -> Element:
        """
        Get picker title text

        Returns:
            webdriver elements: picker title text
        """

        return self._register_country_picker_title

    @property
    def register_screen_title(self):
        """
        Get register button

        Returns:
            webdriver element: register button element
        """

        return self._register_screen_title

    @property
    def marketing_checkbox_selected(self):
        """
        Get marketing checkbox selected state

        Returns:
            Element: marketing checkbox selected element
        """
        return self._marketing_checkbox_selected

    @property
    def marketing_checkbox_unselected(self):
        """
        Get marketing checkbox unselected state

        Returns:
            Element: marketing checkbox unselected element
        """
        return self._marketing_checkbox_unselected
