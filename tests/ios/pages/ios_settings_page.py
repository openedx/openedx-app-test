"""
Settings Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element, expect
from tests.ios.pages.ios_base_page import IosBasePage


class IosSettings(IosBasePage):
    """
    Settings screen
    """

    def __init__(self):
        super().__init__()
        self._screen_title = Element(AppiumBy.ACCESSIBILITY_ID, "register_text")
        self._manage_account_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Manage Account'`]"
        )
        self._manage_account_screen_title = Element(AppiumBy.ACCESSIBILITY_ID, "manage_account_text")
        self._manage_account_username = Element(AppiumBy.ACCESSIBILITY_ID, "user_name_text")
        self._manage_account_useremail = Element(AppiumBy.ACCESSIBILITY_ID, "user_username_text")
        self._manage_account_edit_profile_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Edit Profile'`]"
        )
        self._manage_account_delete_account_button = Element(AppiumBy.ACCESSIBILITY_ID, "delete_account_button")
        self._are_you_sure_text = Element(AppiumBy.ACCESSIBILITY_ID, "are_you_sure_text")
        self._delete_account_desc_text = Element(AppiumBy.ACCESSIBILITY_ID, "delete_account_description_text")
        self._password_filed_title = Element(AppiumBy.ACCESSIBILITY_ID, "password_text")
        self._password_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "password_textfield")
        self._yes_delete_account_button = Element(AppiumBy.ACCESSIBILITY_ID, "Yes, delete account")
        self._back_arrow_button = Element(AppiumBy.ACCESSIBILITY_ID, "arrowLeft")
        self._back_to_profile_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Back to profile'`]"
        )
        self._delete_account_screen_back_navigation_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'back_button'`]"
        )
        self._settings_category_text = Element(AppiumBy.ACCESSIBILITY_ID, "settings_text")
        self._purchase_category_text = Element(AppiumBy.ACCESSIBILITY_ID, "purchases_heading_text")
        self._video_settings_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`label == 'Video settings'`]"
        )
        self._video_settings_screen_title = Element(AppiumBy.ACCESSIBILITY_ID, "manage_account_text")
        self._download_agreement_switch = Element(AppiumBy.ACCESSIBILITY_ID, "download_agreement_switch")
        self._video_stream_quality_button = Element(AppiumBy.ACCESSIBILITY_ID, "video_stream_quality_button")
        self._video_stream_quality_arrow_icon = Element(AppiumBy.ACCESSIBILITY_ID, "video_stream_quality_image")
        self._video_download_quality_button = Element(AppiumBy.ACCESSIBILITY_ID, "video_download_quality_button")
        self._video_download_quality_arrow_icon = Element(AppiumBy.ACCESSIBILITY_ID, "video_download_quality_image")
        self._quality_option_auto = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'select_quality_button'`][1]"
        )
        self._quality_option_360p = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'select_quality_button'`][2]"
        )
        self._quality_option_540p = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'select_quality_button'`][3]"
        )
        self._quality_option_720p = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'select_quality_button'`][4]"
        )
        self._restore_purchase_title = Element(AppiumBy.ACCESSIBILITY_ID, "restore_title_text")
        self._restore_message_text = Element(AppiumBy.ACCESSIBILITY_ID, "restore_message_text")
        self._restore_purchase_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Restore purchases'`]"
        )
        self._restore_purchase_dialogue_title = Element(
            AppiumBy.IOS_CLASS_CHAIN,
            "**/XCUIElementTypeStaticText[`name == 'Purchases have been successfully restored'`]",
        )
        self._restore_purchase_get_help_button = Element(AppiumBy.ACCESSIBILITY_ID, "Get help")
        self._restore_purchase_cancel_button = Element(AppiumBy.ACCESSIBILITY_ID, "Close")
        self._support_info_text = Element(AppiumBy.ACCESSIBILITY_ID, "support_info_text")
        self._help_us_improve_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Help us Improve'`]"
        )
        self._contact_support_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Contact support'`]"
        )
        self._terms_of_use_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Terms of use'`]"
        )
        self._privacy_policy_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Privacy policy'`]"
        )
        self._cookie_policy_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Cookie policy'`]"
        )
        self._donot_sell_my_info_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'Do not sell my personal information'`]"
        )
        self._view_faq_button = Element(AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'View FAQ'`]")
        self._edx_terms_of_use_heading_text = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'edX terms of service'`]"
        )
        self._edx_privacy_policy_heading_text = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'edX privacy policy'`]"
        )
        self._edx_cookie_policy_heading_text = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'edX’s cookie policy'`]"
        )
        self._learner_help_center_search_bar = Element(AppiumBy.ACCESSIBILITY_ID, "search")
        self._app_version_upto_date_checkmark = Element(AppiumBy.ACCESSIBILITY_ID, "checkmark")
        self._logout_arrow_icon = Element(AppiumBy.ACCESSIBILITY_ID, "rectangle.portrait.and.arrow.right")

    @property
    def screen_title(self) -> Element:
        """The screen title element.

        Returns:
            Element: The screen title element.
        """
        return self._screen_title

    @property
    def manage_account_button(self) -> Element:
        """The 'Manage Account' button element.

        Returns:
            Element: The 'Manage Account' button element.
        """
        return self._manage_account_button

    @property
    def manage_account_screen_title(self) -> Element:
        """The 'Manage Account' screen title element.

        Returns:
            Element: The 'Manage Account' screen title element.
        """
        return self._manage_account_screen_title

    @property
    def manage_account_username(self) -> Element:
        """The 'Manage Account' username element.

        Returns:
            Element: The 'Manage Account' username element.
        """
        return self._manage_account_username

    @property
    def manage_account_useremail(self) -> Element:
        """The 'Manage Account' user email element.

        Returns:
            Element: The 'Manage Account' user email element.
        """
        return self._manage_account_useremail

    @property
    def manage_account_edit_profile_button(self) -> Element:
        """The 'Edit Profile' button element in the 'Manage Account' section.

        Returns:
            Element: The 'Edit Profile' button element.
        """
        return self._manage_account_edit_profile_button

    @property
    def manage_account_delete_account_button(self) -> Element:
        """The 'Delete Account' button element in the 'Manage Account' section.

        Returns:
            Element: The 'Delete Account' button element.
        """
        return self._manage_account_delete_account_button

    @property
    def are_you_sure_text(self) -> Element:
        """The 'Are you sure?' text element.

        Returns:
            Element: The 'Are you sure?' text element.
        """
        return self._are_you_sure_text

    @property
    def delete_account_desc_text(self) -> Element:
        """The 'Delete Account' description text element.

        Returns:
            Element: The 'Delete Account' description text element.
        """
        return self._delete_account_desc_text

    @property
    def password_filed_title(self) -> Element:
        """The 'Password' field title element.

        Returns:
            Element: The 'Password' field title element.
        """
        return self._password_filed_title

    @property
    def password_textfield(self) -> Element:
        """The 'Password' text field element.

        Returns:
            Element: The 'Password' text field element.
        """
        return self._password_textfield

    @property
    def yes_delete_account(self) -> Element:
        """The 'Yes, delete account' button element.

        Returns:
            Element: The 'Yes, delete account' button element.
        """
        return self._yes_delete_account_button

    @property
    def back_arrow_button(self) -> Element:
        """The back arrow button element.

        Returns:
            Element: The back arrow button element.
        """
        return self._back_arrow_button

    @property
    def delete_account_screen_back_navigation_button(self) -> Element:
        """The back button element on the delete account screen.

        Returns:
            Element: The back button element on the delete account screen.
        """
        return self._delete_account_screen_back_navigation_button

    @property
    def back_to_profile_button(self):
        """back to profile button

        Returns:
            Element: The back to profile button
        """
        return self._back_to_profile_button

    @property
    def settings_category_text(self) -> Element:
        """The settings category text element.

        Returns:
            Element: The settings category text element.
        """
        return self._settings_category_text

    @property
    def video_settings_button(self) -> Element:
        """The 'Video Settings' button element.

        Returns:
            Element: The 'Video Settings' button element.
        """
        return self._video_settings_button

    @property
    def video_settings_screen_title(self) -> Element:
        """The 'Video Settings' screen title element.

        Returns:
            Element: The 'Video Settings' screen title element.
        """
        return self._video_settings_screen_title

    @property
    def download_agreement_switch(self) -> Element:
        """The 'Download Agreement' switch element.

        Returns:
            Element: The 'Download Agreement' switch element.
        """
        return self._download_agreement_switch

    @property
    def video_stream_quality_button(self) -> Element:
        """The 'Video Stream Quality' button element.

        Returns:
            Element: The 'Video Stream Quality' button element.
        """
        return self._video_stream_quality_button

    @property
    def video_download_quality_button(self) -> Element:
        """The 'Video Download Quality' button element.

        Returns:
            Element: The 'Video Download Quality' button element.
        """
        return self._video_download_quality_button

    @property
    def video_stream_quality_arrow_icon(self) -> Element:
        """The 'Video Stream Quality' arrow icon element.

        Returns:
            Element: The 'Video Stream Quality' arrow icon element.
        """
        return self._video_stream_quality_arrow_icon

    @property
    def video_download_quality_arrow_icon(self) -> Element:
        """The 'Video Download Quality' arrow icon element.

        Returns:
            Element: The 'Video Download Quality' arrow icon element.
        """
        return self._video_download_quality_arrow_icon

    @property
    def quality_option_auto(self) -> Element:
        """The 'Auto' quality option element.

        Returns:
            Element: The 'Auto' quality option element.
        """
        return self._quality_option_auto

    @property
    def quality_option_360p(self) -> Element:
        """The '360p' quality option element.

        Returns:
            Element: The '360p' quality option element.
        """
        return self._quality_option_360p

    @property
    def quality_option_540p(self) -> Element:
        """The '540p' quality option element.

        Returns:
            Element: The '540p' quality option element.
        """
        return self._quality_option_540p

    @property
    def quality_option_720p(self) -> Element:
        """The '720p' quality option element.

        Returns:
            Element: The '720p' quality option element.
        """
        return self._quality_option_720p

    @property
    def purchase_category_text(self) -> Element:
        """The 'Purchases' category text element.

        Returns:
            Element: The 'Purchases' category text element.
        """
        return self._purchase_category_text

    @property
    def restore_purchase_title(self) -> Element:
        """The 'Restore Purchases' title element.

        Returns:
            Element: The 'Restore Purchases' title element.
        """
        return self._restore_purchase_title

    @property
    def restore_message_text(self) -> Element:
        """The 'Restore Purchases' message text element.

        Returns:
            Element: The 'Restore Purchases' message text element.
        """
        return self._restore_message_text

    @property
    def restore_purchase_button(self) -> Element:
        """The 'Restore Purchases' button element.

        Returns:
            Element: The 'Restore Purchases' button element.
        """
        return self._restore_purchase_button

    @property
    def restore_purchase_dialogue_title(self) -> Element:
        """The 'Restore Purchases' dialogue title element.

        Returns:
            Element: The 'Restore Purchases' dialogue title element.
        """
        return self._restore_purchase_dialogue_title

    @property
    def restore_purchase_get_help_button(self) -> Element:
        """The 'Get Help' button element in the 'Restore Purchases' dialogue.

        Returns:
            Element: The 'Get Help' button element.
        """
        return self._restore_purchase_get_help_button

    @property
    def restore_purchase_cancel_button(self) -> Element:
        """The 'Close' button element in the 'Restore Purchases' dialogue.

        Returns:
            Element: The 'Close' button element.
        """
        return self._restore_purchase_cancel_button

    @property
    def support_info_category_text(self) -> Element:
        """support info text

        Returns:
            Element: Support info text element
        """

        return self._support_info_text

    @property
    def help_us_improve_button(self) -> Element:
        """The 'Help Us Improve' button element.

        Returns:
            Element: The 'Help Us Improve' button element.
        """
        return self._help_us_improve_button

    @property
    def contact_support_button(self) -> Element:
        """The 'Contact Support' button element.

        Returns:
            Element: The 'Contact Support' button element.
        """
        return self._contact_support_button

    @property
    def terms_of_use_button(self) -> Element:
        """The 'Terms of Use' button element.

        Returns:
            Element: The 'Terms of Use' button element.
        """
        return self._terms_of_use_button

    @property
    def privacy_policy_button(self) -> Element:
        """The 'Privacy Policy' button element.

        Returns:
            Element: The 'Privacy Policy' button element.
        """
        return self._privacy_policy_button

    @property
    def cookie_policy_button(self) -> Element:
        """The 'Cookie Policy' button element.

        Returns:
            Element: The 'Cookie Policy' button element.
        """
        return self._cookie_policy_button

    @property
    def donot_sell_my_info_button(self) -> Element:
        """The 'Do Not Sell My Personal Information' button element.

        Returns:
            Element: The 'Do Not Sell My Personal Information' button element.
        """
        return self._donot_sell_my_info_button

    @property
    def view_faq_button(self) -> Element:
        """The 'View FAQ' button element.

        Returns:
            Element: The 'View FAQ' button element.
        """
        return self._view_faq_button

    @property
    def edx_terms_of_use_heading_text(self) -> Element:
        """The 'edX Terms of Service' heading text element.

        Returns:
            Element: The 'edX Terms of Service' heading text element.
        """
        return self._edx_terms_of_use_heading_text

    @property
    def edx_privacy_policy_heading_text(self) -> Element:
        """The 'edX Privacy Policy' heading text element.

        Returns:
            Element: The 'edX Privacy Policy' heading text element.
        """
        return self._edx_privacy_policy_heading_text

    @property
    def edx_cookie_policy_heading_text(self) -> Element:
        """The 'edX Cookie Policy' heading text element.

        Returns:
            Element: The 'edX Cookie Policy' heading text element.
        """
        return self._edx_cookie_policy_heading_text

    @property
    def learner_help_center_search_bar(self) -> Element:
        """The 'Learner Help Center' search bar element.

        Returns:
            Element: The 'Learner Help Center' search bar element.
        """
        return self._learner_help_center_search_bar

    @property
    def app_version_upto_date_checkmark(self) -> Element:
        """The app version up-to-date checkmark element.

        Returns:
            Element: The app version up-to-date checkmark element.
        """
        return self._app_version_upto_date_checkmark

    @property
    def logout_arrow_icon(self) -> Element:
        """The logout arrow icon element.

        Returns:
            Element: The logout arrow icon element.
        """
        return self._logout_arrow_icon

    def verify_app_version(self, expected_version: str):
        """
        Verify the app version.
        Args:
            expected_version (str): The expected app version
        """
        expect(self.find_by_text_on_screen(f"Version: {expected_version}")).to_exist()
        expect(self.find_by_text_on_screen("Up-to-date")).to_exist()
        expect(self.app_version_upto_date_checkmark).to_exist()
