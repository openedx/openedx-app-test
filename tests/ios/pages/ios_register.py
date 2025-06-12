"""
Login Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.common.enums.general_enums import GenderOptions, EducationLevel
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
        self._name_text_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "name_text")
        self._name_text_field = Element(AppiumBy.ACCESSIBILITY_ID, "name_textfield")
        self._name_text_field_instructions_text = Element(AppiumBy.ACCESSIBILITY_ID, "name_instructions_text")
        self._username_text_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "username_text")
        self._username_text_field = Element(AppiumBy.ACCESSIBILITY_ID, "username_textfield")
        self._username_text_field_instructions_text = Element(AppiumBy.NAME, "username_instructions_text")
        self._email_text_field_label = Element(AppiumBy.NAME, "email_text")
        self._email_text_field = Element(AppiumBy.ACCESSIBILITY_ID, "email_textfield")
        self._email_text_field_instructions_text = Element(AppiumBy.ACCESSIBILITY_ID, "email_instructions_text")
        self._password_text_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "password_text")
        self._password_secure_text_field = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeSecureTextField[`name == 'password_textfield'`]"
        )
        self._password_text_field_instructions_text = Element(AppiumBy.NAME, "password_instructions_text")
        self._country_text_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "country_text")
        self._country_picker_button = Element(AppiumBy.ACCESSIBILITY_ID, "country_picker_button")
        self._country_picker_instructions_text = Element(AppiumBy.NAME, "country_instructions_text")
        self._create_account_button = Element(AppiumBy.ACCESSIBILITY_ID, "Create account")
        self._register_screen_heading = Element(AppiumBy.ACCESSIBILITY_ID, "register_text")
        self._register_signup_text = Element(AppiumBy.ACCESSIBILITY_ID, "signup_text")
        self._signup_subtitle_text = Element(AppiumBy.ACCESSIBILITY_ID, "signup_subtitle_text")
        self._country_picker_title_label = Element(AppiumBy.ACCESSIBILITY_ID, "picker_title_text")
        self._optional_fields_toggle_button = Element(AppiumBy.NAME, "optional_fields_text")
        self._highest_level_of_education_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "level_of_education_text")
        self._highest_level_of_education_picker_button = Element(
            AppiumBy.ACCESSIBILITY_ID, "level_of_education_picker_button"
        )
        self._gender_field_label = Element(AppiumBy.ACCESSIBILITY_ID, "gender_text")
        self._gender_picker_button = Element(AppiumBy.ACCESSIBILITY_ID, "gender_picker_button")
        self._gender_male_option = Element(AppiumBy.ACCESSIBILITY_ID, "gender_male_option")
        self._gender_female_option = Element(AppiumBy.ACCESSIBILITY_ID, "gender_female_option")
        self._gender_other_option = Element(AppiumBy.ACCESSIBILITY_ID, "gender_other_option")
        self._register_screen_title = Element(AppiumBy.ACCESSIBILITY_ID, "register_text")
        self._marketing_checkbox_selected = Element(AppiumBy.ACCESSIBILITY_ID, "checkmark.square.fill")
        self._marketing_checkbox_unselected = Element(AppiumBy.ACCESSIBILITY_ID, "square")
        self._signin_social_auth_google_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_google_button")
        self._signin_social_auth_facebook_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_facebook_button")
        self._signin_social_auth_microsoft_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_microsoft_button")
        self._signin_social_auth_apple_button = Element(AppiumBy.ACCESSIBILITY_ID, "social_auth_apple_button")

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
    def name_text_field_label(self) -> Element:
        """
        Get name text

        Returns:
            webdriver element: name text element
        """

        return self._name_text_field_label

    @property
    def name_text_field(self) -> Element:
        """
        Get name textfield

        Returns:
            webdriver element: name textfield element
        """

        return self._name_text_field

    @property
    def name_instructions_text(self) -> Element:
        """
        Get name instructions text

        Returns:
            webdriver element: name instructions text element
        """

        return self._name_text_field_instructions_text

    @property
    def username_text_field_label(self) -> Element:
        """
        Get username text

        Returns:
            webdriver element: username text element
        """

        return self._username_text_field_label

    @property
    def username_text_field(self) -> Element:
        """
        Get username textfield

        Returns:
            webdriver element: username textfield element
        """

        return self._username_text_field

    @property
    def username_instructions_text(self) -> Element:
        """
        Get username instructions text

        Returns:
            webdriver element: username instructions text element
        """

        return self._username_text_field_instructions_text

    @property
    def email_text_field_label(self) -> Element:
        """
        Get email text

        Returns:
            webdriver element: email text element
        """

        return self._email_text_field_label

    @property
    def email_text_field(self) -> Element:
        """
        Get email textfield

        Returns:
            webdriver element: email textfield element
        """

        return self._email_text_field

    @property
    def email_instructions_text(self) -> Element:
        """
        Get email instructions text

        Returns:
            webdriver element: email instructions text element
        """

        return self._email_text_field_instructions_text

    @property
    def password_text_field_label(self) -> Element:
        """
        Get password text

        Returns:
            webdriver element: password text element
        """

        return self._password_text_field_label

    @property
    def password_text_field(self) -> Element:
        """
        Get password textfield

        Returns:
            webdriver element: password textfield element
        """

        return self._password_secure_text_field

    @property
    def password_instructions_text(self) -> Element:
        """
        Get password instructions text

        Returns:
            webdriver element: password instructions text element
        """

        return self._password_text_field_instructions_text

    @property
    def country_text_field_label(self) -> Element:
        """
        Get country text

        Returns:
            webdriver element: country text element
        """

        return self._country_text_field_label

    @property
    def country_picker_button(self):
        """
        Get country textfield

        Returns:
            webdriver element: country textfield element
        """

        return self._country_picker_button

    @property
    def country_instructions_text(self) -> Element:
        """
        Get country instructions text

        Returns:
            webdriver element: country instructions text element
        """

        return self._country_picker_instructions_text

    @property
    def optional_fields_toggle_buttons(self):
        """
        Get show optional fields


        Returns:
            webdriver element: show optional fields element
        """

        return self._optional_fields_toggle_button

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
    def social_auth_google_button(self) -> Element:
        """
        Get social auth google button text

        Returns:
            Element: signin social auth google button
        """

        return self._signin_social_auth_google_button

    @property
    def social_auth_facebook_button(self) -> Element:
        """
        Get social auth facebook button text

        Returns:
            Element: signin social auth facebook button
        """

        return self._signin_social_auth_facebook_button

    @property
    def social_auth_microsoft_button(self) -> Element:
        """
        Get social auth microsoft button text

        Returns:
            Element: signin social auth microsoft button
        """
        return self._signin_social_auth_microsoft_button

    @property
    def social_auth_apple_button(self) -> Element:
        """
        Get social auth apple button text

        Returns:
            Element: signin social auth apple button
        """

        return self._signin_social_auth_apple_button

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

    @property
    def highest_level_of_education_label(self):
        """
        highest level of education

        Returns:
            Element: highest level of education label element
        """
        return self._highest_level_of_education_field_label

    @property
    def gender_picker_button(self):
        """
        gender picker button

        Returns:
            Element: gender picker button element
        """
        return self._gender_picker_button

    @property
    def gender_field_label(self) -> Element:
        """
        Get gender field label

        Returns:
            Element: gender field label element
        """
        return self._gender_field_label

    @property
    def highest_level_of_education_picker_button(self) -> Element:
        """
        highest level of education picker button

        Returns:
            Element: highest level of education picker button element
        """
        return self._highest_level_of_education_picker_button

    def search_and_verify_gender_option_exists(self, gender_option: GenderOptions):
        """Search and verify gender option exists

        Args:
            gender_option(GenderOptions): gender option to search for
        """
        self.search_and_verify_option_exists(gender_option)

    def search_and_verify_education_level_exists(self, education_level: EducationLevel):
        """Search and verify education level exists

        Args:
            education_level(EducationLevel): education option to search for
        """
        self.search_and_verify_option_exists(education_level)
