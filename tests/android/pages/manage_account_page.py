"""Module covers Manage Account Page"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.android.pages.android_base_page import AndroidBasePage


class ManageAccountPage(AndroidBasePage):
    """Manage Account Page"""

    def __init__(self):
        super().__init__()

        self._profile_settings_delete_account_warning = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_delete_account_title")'
        )
        self._delete_account_screen_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_delete_account_description")'
        )
        self._edit_profile_btn = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_edit_profile")'
        )
        self._edit_profile_btn_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_edit_profile")'
        )
        self._delete_account_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_delete_account")'
        )
        self._delete_account_button_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_delete_account")'
        )
        self._delete_account_button_icon = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ic_delete_account")'
        )
        self._password_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_password_label")'
        )
        self._password_input_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_password_input")'
        )

        self._yes_delete_account_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_yes,_delete_account")'
        )
        self._profile_name_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_name")'
        )
        self._profile_username = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_profile_username")'
        )

    @property
    def password_label(self):
        """
        Getter for the password label.

        Returns:
            Element: password label.
        """
        return self._password_label

    @property
    def delete_account_screen_warning_title(self):
        """
        Getter for the delete screen waring msg.

        Returns:
            Element: delete screen waring msg.
        """
        return self._profile_settings_delete_account_warning

    @property
    def delete_account_screen_description(self):
        """
        Getter for the delete account screen description.

        Returns:
            Element: delete account screen description.
        """
        return self._delete_account_screen_description

    @property
    def delete_account_screen_title(self):
        """
        Getter for the delete account screen title.

        Returns:
            Element: delete account screen title.
        """
        return self.text_toolbar_title

    @property
    def edit_profile_button(self) -> Element:
        """
        Returns:
            Element: edit profile button element
        """

        return self._edit_profile_btn

    @property
    def edit_profile_button_text(self) -> Element:
        """
        Returns:
            Element: edit profile button element
        """

        return self._edit_profile_btn_text

    @property
    def delete_account_button(self):
        """
        Getter for the 'Delete Account' element on the profile settings page.

        Returns:
            Element: The 'Delete Account' element.
        """
        return self._delete_account_button

    @property
    def delete_account_button_text(self):
        """
        Getter for the 'Delete Account' element text.

        Returns:
            Element: The 'Delete Account text' element.
        """
        return self._delete_account_button_text

    @property
    def delete_account_icon(self):
        """
        Getter for the 'Delete Account' element text.

        Returns:
            Element: The 'Delete Account text' element.
        """
        return self._delete_account_button_icon

    @property
    def password_input_field(self):
        """
        Getter for the password input element on the profile settings page.

        Returns:
            Element: The password input element.
        """
        return self._password_input_field

    @property
    def yes_delete_account_button(self):
        """
        Getter for the password input element on the profile settings page.

        Returns:
            Element: The password input element.
        """
        return self._yes_delete_account_button

    @property
    def profile_name_text(self):
        """
        Getter for the profile name text.

        Returns:
            Element: profile name text.
        """
        return self._profile_name_text

    @property
    def profile_username(self) -> Element:
        """
        Returns:
            Element: profile username element
        """

        return self._profile_username
