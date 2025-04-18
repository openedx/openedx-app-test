"""
Register Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage
from tests.common import values


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
        self._register_txt_name_label = Element(
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
        self._register_btn_create_account = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("btn_create_account")',
        )
        self._register_education_level = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("register_education_level")',
        )
        self._register_education_level_placeholder = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("register_education_level_placeholder")',
        )
        self._register_gender_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_gender_label")',
        )
        self._register_gender_label_placeholder = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_gender_placeholder")',
        )
        self._register_country_selection_dialogue = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_selection_title")',
        )
        self._register_country_sb_search = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("sb_search")'
        )
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
            f"new UiSelector().text({values.REGISTER_HONOR_POLICY_TEXT})",
        )

        self._register_marketing_messages_agreement = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckBox")'
        )

    @property
    def get_register_title(self) -> Element:
        """Get register title"""

        return self._register_text_sign_up_title

    @property
    def get_register_description(self) -> Element:
        """Get register description"""

        return self._register_txt_description

    @property
    def get_register_txt_name_label(self) -> Element:
        """Get register name label"""

        return self._register_txt_name_label

    @property
    def get_register_tf_name(self) -> Element:
        """Get register name text field"""

        return self._name_text_field

    @property
    def get_register_txt_name_description(self) -> Element:
        """Get register description label"""

        return self._name_text_field_description

    @property
    def get_register_txt_username_label(self) -> Element:
        """Get register username label"""

        return self._username_text_field_label

    @property
    def get_register_tf_username(self) -> Element:
        """Get register username text field"""

        return self._username_text_field

    @property
    def get_register_txt_username_description(self) -> Element:
        """Get register username description"""

        return self._username_text_field_description

    @property
    def get_register_txt_email_label(self) -> Element:
        """Get register email label"""

        return self._register_txt_email_label

    @property
    def get_register_tf_email(self) -> Element:
        """Get register email text field"""

        return self._register_tf_email

    @property
    def get_register_txt_email_description(self) -> Element:
        """Get register email description"""

        return self._register_txt_email_description

    @property
    def get_register_txt_password_label(self) -> Element:
        """Get register password label"""

        return self._register_txt_password_label

    @property
    def get_register_tf_password(self) -> Element:
        """Get register password text field"""

        return self._register_tf_password

    @property
    def get_register_txt_password_description(self) -> Element:
        """Get register password description"""

        return self._register_txt_password_description

    @property
    def get_register_txt_country_label(self) -> Element:
        """Get register country label"""

        return self._register_txt_country_label

    @property
    def get_register_tf_country(self) -> Element:
        """Get register country text field"""

        return self._register_tf_country

    @property
    def get_register_txt_country_description(self) -> Element:
        """Get register country description"""

        return self._register_txt_country_description

    @property
    def marketing_messages_agreement_check_box(self) -> Element:
        """Get register marketing messages agreement check box"""

        return self._register_marketing_messages_agreement

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
    def get_register_txt_optional_field(self) -> Element:
        """Get register optional field"""

        return self._register_txt_optional_field

    @property
    def get_register_btn_create_account(self) -> Element:
        """Get register create account button"""

        return self._register_btn_create_account

    @property
    def get_register_education_level(self) -> Element:
        """Get register education level"""

        return self._register_education_level

    @property
    def get_register_education_level_placeholder(self) -> Element:
        """Get register education level placeholder"""

        return self._register_education_level_placeholder

    @property
    def get_register_gender_label(self) -> Element:
        """Get register gender label"""

        return self._register_gender_label

    @property
    def get_gender_label_placeholder(self) -> Element:
        """Get gender label placeholder"""

        return self._register_gender_label_placeholder

    @property
    def get_register_country_selection_dialogue(self) -> Element:
        """Get register country selection dialogue"""

        return self._register_country_selection_dialogue

    @property
    def country_search(self) -> Element:
        """Get register country search"""

        return self._register_country_sb_search

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
