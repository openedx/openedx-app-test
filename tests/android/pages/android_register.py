"""
Register Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidRegister(AndroidBasePage):
    """
    Register screen
    """

    def __init__(self):
        super().__init__()
        self._register_text_sign_up_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_sign_up_title")',
        )
        self._register_txt_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_sign_up_description")',
        )
        self._txt_name_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_name_label")',
        )
        self._name_text_field = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_name")')
        self._name_text_field_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_name_description")',
        )
        self._username_text_field_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_username_label")',
        )
        self._username_text_field = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_username")')
        self._username_text_field_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_username_description")',
        )
        self._register_txt_email_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_email_label")',
        )
        self._register_tf_email = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_email")')
        self._register_txt_email_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_email_description")',
        )
        self._register_txt_password_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_password_label")',
        )
        self._register_tf_password = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_password")')
        self._register_txt_password_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_password_description")',
        )
        self._register_txt_country_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_country_label")',
        )
        self._register_tf_country = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_country")')
        self._register_txt_country_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_country_description")',
        )
        self._register_txt_honor_code = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_honor_code")',
        )
        self._register_txt_optional_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_optional_field")',
        )
        self._btn_create_account = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("btn_create_account")',
        )
        self._register_education_level = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_level_of_education_label")',
        )
        self._register_education_level_placeholder = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_level_of_education_placeholder")',
        )
        self._education_level_dropdown = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_level_of_education")',
        )
        self._gender_field_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_gender_label")',
        )
        self._gender_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_gender")',
        )
        self._register_gender_label_placeholder = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_gender_placeholder")',
        )
        self._register_country_selection_dialogue = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_selection_title")',
        )
        self._sb_search_field = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("sb_search")')
        self._register_txt_US_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_us_title")'
        )
        self._google_auth_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Continue with Google")',
        )
        self._txt_facebook_auth = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Continue with Facebook")',
        )
        self._txt_microsoft_auth = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Continue with Microsoft")',
        )
        self._honor_policy_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("By creating an account, you agree to the edX End User Licence Agreement and'
            " edX Terms of Service and Honor Code and you acknowledge that edX and each Member process your personal "
            'data in accordance with the edX Privacy Policy.")',
        )

        self._register_marketing_messages_agreement = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckBox")'
        )
        self._highest_level_of_education_field_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_level_of_education_label")'
        )
        self._bachelor_level_education = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_b_title")'
        )
        self._gender_male_option = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_m_title")')
        self._gender_female_option = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_f_title")')
        self._gender_other_option = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_o_title")')

    @property
    def gender_male_option(self) -> Element:
        """Get gender male option"""
        return self._gender_male_option

    @property
    def gender_female_option(self) -> Element:
        """Get gender female option"""
        return self._gender_female_option

    @property
    def gender_other_option(self) -> Element:
        """Get gender other option"""
        return self._gender_other_option

    @property
    def bachelor_level_education(self) -> Element:
        """Get the bachelor level of education"""

        return self._bachelor_level_education

    @property
    def highest_level_of_education_field_label(self) -> Element:
        """Get the highest level of education field"""

        return self._highest_level_of_education_field_label

    @property
    def register_title(self) -> Element:
        """Get register title"""

        return self._register_text_sign_up_title

    @property
    def register_description(self) -> Element:
        """Get register description"""

        return self._register_txt_description

    @property
    def name_field_label(self) -> Element:
        """Get register name label"""

        return self._txt_name_label

    @property
    def name_text_field(self) -> Element:
        """Get register name text field"""

        return self._name_text_field

    @property
    def name_field_description(self) -> Element:
        """Get register description label"""

        return self._name_text_field_description

    @property
    def username_field_label(self) -> Element:
        """Get register username label"""

        return self._username_text_field_label

    @property
    def username_text_field(self) -> Element:
        """Get register username text field"""

        return self._username_text_field

    @property
    def username_field_description(self) -> Element:
        """Get register username description"""

        return self._username_text_field_description

    @property
    def email_field_label(self) -> Element:
        """Get register email label"""

        return self._register_txt_email_label

    @property
    def email_text_field(self) -> Element:
        """Get register email text field"""

        return self._register_tf_email

    @property
    def email_field_description(self) -> Element:
        """Get register email description"""

        return self._register_txt_email_description

    @property
    def password_field_label(self) -> Element:
        """Get register password label"""

        return self._register_txt_password_label

    @property
    def password_text_field(self) -> Element:
        """Get register password text field"""

        return self._register_tf_password

    @property
    def password_field_description(self) -> Element:
        """Get register password description"""

        return self._register_txt_password_description

    @property
    def country_field_label(self) -> Element:
        """Get register country label"""

        return self._register_txt_country_label

    @property
    def country_text_field(self) -> Element:
        """Get register country text field"""

        return self._register_tf_country

    @property
    def marketing_messages_agreement_check_box(self) -> Element:
        """Get register marketing messages agreement check box"""

        return self._register_marketing_messages_agreement

    @property
    def country_field_description(self) -> Element:
        """Get register country description"""

        return self._register_txt_country_description

    # TODO: seems like not related to the registration page and is using iOS selectors
    # def get_register_txt_honor_code(self) ->  Element:
    #     """
    #     Get register honor code
    #     """

    #     honor_code = self.global_contents.get_ios_all_static_text(
    #         self.driver
    #         )
    #     return honor_code[14]

    @property
    def show_optional_field(self) -> Element:
        """Get register optional field"""

        return self._register_txt_optional_field

    @property
    def btn_create_account(self) -> Element:
        """Get register create account button"""

        return self._btn_create_account

    @property
    def education_level_dropdown(self) -> Element:
        """Get register education level"""

        return self._education_level_dropdown

    @property
    def gender_field_label(self) -> Element:
        """Get register gender label"""

        return self._gender_field_label

    @property
    def gender_field_dropdown(self) -> Element:
        """Get register gender label"""

        return self._gender_field

    @property
    def get_gender_label_placeholder(self) -> Element:
        """Get gender label placeholder"""

        return self._register_gender_label_placeholder

    @property
    def get_register_country_selection_dialogue(self) -> Element:
        """Get register country selection dialogue"""

        return self._register_country_selection_dialogue

    @property
    def search_field(self) -> Element:
        """Get register country search"""

        return self._sb_search_field

    @property
    def get_txt_us_title(self) -> Element:
        """Get register country search"""

        return self._register_txt_US_title

    @property
    def get_txt_google_auth(self) -> Element:
        """Get register google auth text"""

        return self._google_auth_button

    @property
    def get_txt_facebook_auth(self) -> Element:
        """Get register facebook auth text"""

        return self._txt_facebook_auth

    @property
    def get_txt_microsoft_auth(self) -> Element:
        """Get register microsoft auth text"""

        return self._txt_microsoft_auth

    def go_back(self) -> bool:
        """Go back"""

        return self.back_navigation_button.click()

    @property
    def honor_policy_text(self) -> Element:
        """registration honor text"""

        return self._honor_policy_text
