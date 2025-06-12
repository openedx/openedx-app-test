"""
Profile Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element, expect
from tests.ios.pages.ios_base_page import IosBasePage


class IosProfile(IosBasePage):
    """
    Profile screen
    """

    def __init__(self):
        super().__init__()
        self._profile_screen_title = Element(AppiumBy.NAME, "Profile")
        self._profile_edit_button = Element(AppiumBy.ACCESSIBILITY_ID, "edit_profile_button")
        self._profile_settings_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeButton[`name == 'edit_profile_button'`]"
        )
        self._profile_user_avatar_image = Element(AppiumBy.ACCESSIBILITY_ID, "user_avatar_image")
        self._full_name_label = Element(AppiumBy.ACCESSIBILITY_ID, "user_name_text")
        self._username_label = Element(AppiumBy.ACCESSIBILITY_ID, "user_username_text")
        self._profile_bio_label = Element(AppiumBy.ACCESSIBILITY_ID, "profile_info_text")
        self._profile_bio_value = Element(AppiumBy.ACCESSIBILITY_ID, "bio_text")
        self._profile_settings_text = Element(AppiumBy.ACCESSIBILITY_ID, "settings_text")
        self._profile_logout_button = Element(AppiumBy.ACCESSIBILITY_ID, "logout_button")
        self._profile_prompt_logout_button = Element(AppiumBy.ACCESSIBILITY_ID, "Log out")
        self._profile_logout_dialogue_title = Element(AppiumBy.NAME, "Are you sure you want to log out?")
        self._profile_logout_close_button = Element(AppiumBy.NAME, "xmark")
        self._profile_logout_confirmation = Element(AppiumBy.ACCESSIBILITY_ID, "logout_confirmation")
        self._profile_logout_confirmation_button = Element(AppiumBy.ACCESSIBILITY_ID, "logout_confirmation_button")
        self._profile_video_settings_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Video settings'`]"
        )
        self._profile_manage_account_label = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeOther[`name == 'Manage Account'`]"
        )
        self._profile_manage_account_title = Element(
            AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'manage_account_text'`]"
        )
        self._profile_dates_calendar_label = Element(AppiumBy.ACCESSIBILITY_ID, "Dates & Calendar")
        self._profile_support_info_text = Element(AppiumBy.ACCESSIBILITY_ID, "support_info_text")
        self._profile_tos_text = Element(AppiumBy.NAME, "tos")
        self._manage_account_text = Element(AppiumBy.ACCESSIBILITY_ID, "manage_account_text")
        self._main_dashboard_profile_tab = Element(AppiumBy.ACCESSIBILITY_ID, "Profile")
        self._arrow_left_back_button = Element(AppiumBy.ACCESSIBILITY_ID, "arrowLeft")
        self._version_info = Element(AppiumBy.ACCESSIBILITY_ID, "version_info")
        self._profile_view_faq = Element(AppiumBy.ACCESSIBILITY_ID, "view_faq")
        self._profile_contact_support = Element(AppiumBy.ACCESSIBILITY_ID, "Contact support")
        self._profile_dont_sell_data = Element(AppiumBy.ACCESSIBILITY_ID, "dont_sell_data")
        self._profile_cookies_policy = Element(AppiumBy.ACCESSIBILITY_ID, "cookies_policy")
        self._profile_privacy_policy = Element(AppiumBy.ACCESSIBILITY_ID, "privacy_policy")
        self._edit_profile_button = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`name == "Edit Profile"`]'
        )
        self._delete_account_button = Element(AppiumBy.ACCESSIBILITY_ID, "delete_account_button")
        self._delete_account_password_textfield = Element(AppiumBy.ACCESSIBILITY_ID, "password_textfield")
        self._settings_screen_title = Element(AppiumBy.ACCESSIBILITY_ID, "register_text")

    @property
    def edit_profile_button(self) -> Element:
        """
        Returns:
            Element: The element representing the edit profile title.
        """
        return self._edit_profile_button

    @property
    def profile_bio_label(self) -> Element:
        """
        Get profile bio label

        Returns:
            Element: Profile bio label element
        """

        return self._profile_bio_label

    @property
    def profile_bio_value(self) -> Element:
        """
        Get profile bio label

        Returns:
            Element: Profile bio label element
        """

        return self._profile_bio_value

    @property
    def get_profile_screen_title(self) -> Element:
        """
        Get profile screen title

        Returns:
            webdriver element: Profile screen title element
        """

        return self._profile_screen_title

    @property
    def get_profile_edit_button(self) -> Element:
        """
        Get profile edit button

        Returns:
            webdriver element: Profile edit button element
        """

        return self._profile_edit_button

    @property
    def profile_settings_button(self) -> Element:
        """
        Get profile settings button

        Returns:
            webdriver element: Profile settings button element
        """

        return self._profile_settings_button

    @property
    def profile_img_profile(self) -> Element:
        """
        Get profile image

        Returns:
            webdriver element: Profile image element
        """

        return self._profile_user_avatar_image

    @property
    def full_name_label(self) -> Element:
        """
        Get user's name text

        Returns:
            webdriver element: User's name text element
        """

        return self._full_name_label

    @property
    def username_label(self) -> Element:
        """
        Get user's username text

        Returns:
            Element: User's username text element
        """

        return self._username_label

    @property
    def get_profile_settings_text(self) -> Element:
        """
        Get settings text

        Returns:
            webdriver element: Settings text element
        """

        return self._profile_settings_text

    @property
    def get_profile_video_settings_button(self) -> Element:
        """
        Get video settings button

        Returns:
            webdriver element: Video settings button element
        """

        return self._profile_video_settings_button

    @property
    def profile_manage_account_label(self) -> Element:
        """
        Get manage account label

        Returns:
            Element: Manage account label element
        """
        return self._profile_manage_account_label

    @property
    def profile_manage_account_title(self) -> Element:
        """
        Get manage account screen title

        Returns:
            Element: Manage account screen title element
        """
        return self._profile_manage_account_title

    @property
    def get_profile_dates_calendar_label(self) -> Element:
        """
        Get dates calendar label

        Returns:
            webdriver element: Dates & Calendar element
        """

        return self._profile_dates_calendar_label

    @property
    def get_profile_support_info_text(self) -> Element:
        """
        Get support info text

        Returns:
            webdriver element: Support info text element
        """

        return self._profile_support_info_text

    @property
    def get_profile_tos_text(self) -> Element:
        """
        Get tos text

        Returns:
            webdriver element: Tos text element
        """

        return self._profile_tos_text

    @property
    def get_profile_privacy_policy(self) -> Element:
        """
        Get privacy policy

        Returns:
            webdriver element: Privacy policy element
        """

        return self._profile_privacy_policy

    @property
    def get_profile_cookies_policy(self) -> Element:
        """
        Get cookies policy

        Returns:
            webdriver element: Cookies policy element
        """

        return self._profile_cookies_policy

    @property
    def get_profile_dont_sell_data(self) -> Element:
        """
        Get dont sell data

        Returns:
            webdriver element: Dont sell data element
        """

        return self._profile_dont_sell_data

    @property
    def get_profile_contact_support(self) -> Element:
        """
        Get contact support

        Returns:
            webdriver element: Contact support element
        """

        return self._profile_contact_support

    @property
    def get_profile_view_faq(self) -> Element:
        """
        Get view faq

        Returns:
            webdriver element: View faq element
        """

        return self._profile_view_faq

    @property
    def get_profile_version_info(self) -> Element:
        """
        Get version info

        Returns:
            webdriver element: Version info element
        """

        return self._version_info

    @property
    def get_profile_logout_button(self) -> Element:
        """
        Get logout button

        Returns:
            webdriver element: Logout button element
        """

        return self._profile_logout_button

    @property
    def get_logout_close_button(self) -> Element:
        """
        Get close button

        Returns:
            webdriver element: Close button element
        """

        return self._profile_logout_close_button

    @property
    def get_logout_dialog_title(self) -> Element:
        """
        Get dialog title

        Returns:
            webdriver element: Dialog title element
        """

        return self._profile_logout_dialogue_title

    @property
    def get_logout_button_from_prompt(self) -> Element:
        """
        Get logout button

        Returns:
            webdriver element: Logout button element
        """

        return self._profile_prompt_logout_button

    @property
    def get_back_button(self) -> Element:
        """
        Get discovery title

        Returns:
            webdriver element: discovery title element
        """

        return self._arrow_left_back_button

    @property
    def get_manage_account_title(self) -> Element:
        """
        Returns:
            element: manage account title element
        """

        return self._manage_account_text

    @property
    def delete_account_button(self):
        """
        Returns:
            Element: delete account button Element
        """
        return self._delete_account_button

    @property
    def delete_account_password_textfield(self):
        """
        Returns:
            Element: delete account page password text field
        """
        return self._delete_account_password_textfield

    @property
    def settings_screen_title(self):
        """
        Returns:
            Element: delete account page password text field
        """
        return self._settings_screen_title

    def verify_app_version(self, expected_version: str):
        """
        Verify the app version.
        Args:
            expected_version (str): The expected app version
        """
        expect(Element(AppiumBy.ACCESSIBILITY_ID, f"Version: {expected_version}")).to_exist()
        expect(Element(AppiumBy.ACCESSIBILITY_ID, "Up-to-date")).to_exist()
