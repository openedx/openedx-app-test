"""Module covers Android Settings Page"""

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element, expect
from tests.android.pages.android_base_page import AndroidBasePage
from tests.common import values


class AndroidSettingsPage(AndroidBasePage):
    """Class covers Android Settings Page"""

    def __init__(self):
        super().__init__()
        self._title_text_settings = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings").instance(0)'
        )
        self._settings_category_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Settings").instance(1)'
        )
        self._manage_account_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Manage Account")')
        self._video_button_text = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Video")')
        self._restore_purchases_button_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Restore Purchases")'
        )
        self._wifi_only_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_wifi_only_label")'
        )
        self._wifi_only_description_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_wifi_only_description")'
        )
        self._wifi_only_toggle_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("sw_wifi_only")'
        )
        self._video_quality_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_video_quality")'
        )
        self._auto_text_label = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Auto")')
        self._video_quality_button_auto = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_video_quality_auto")'
        )
        self._video_quality_button_360p = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_video_quality_360p")'
        )
        self._video_quality_button_540p = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_video_quality_540p")'
        )
        self._video_quality_button_720p = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("btn_video_quality_720p")'
        )
        self._video_quality_button_auto_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_quality_title_auto")'
        )
        self._video_quality_button_360p_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_quality_title_360p")'
        )
        self._video_quality_button_540p_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_quality_title_540p")'
        )
        self._video_quality_button_720p_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_quality_title_720p")'
        )
        self._video_quality_button_auto_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_quality_description_auto")'
        )
        self._video_quality_button_360p_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_quality_description_360p")'
        )
        self._video_quality_button_720p_description = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_video_quality_description_720p")'
        )
        self._selected_video_quality_check_mark_auto = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ic_video_quality_selected_auto")'
        )
        self._selected_video_quality_check_mark_360p = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ic_video_quality_selected_360p")'
        )
        self._selected_video_quality_check_mark_540p = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ic_video_quality_selected_540p")'
        )
        self._selected_video_quality_check_mark_720p = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ic_video_quality_selected_720p")'
        )
        self._help_us_improve_link = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Help us Improve")')
        self._share_my_info_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().text("Share My Information with Third Parties for Personalized Advertising")',
        )
        self._video_quality_option_buttons = {
            values.AUTO: self._video_quality_button_auto,
            values.LOWEST_QUALITY: self._video_quality_button_360p,
            values.MEDIUM_QUALITY: self._video_quality_button_540p,
            values.HIGHEST_QUALITY: self._video_quality_button_720p,
        }
        self._video_quality_option_titles = [
            (self._video_quality_button_auto_title, values.AUTO),
            (self._video_quality_button_360p_title, values.LOWEST_QUALITY),
            (self._video_quality_button_540p_title, values.MEDIUM_QUALITY),
            (self._video_quality_button_720p_title, values.HIGHEST_QUALITY),
        ]
        self._video_quality_option_descriptions = [
            (self._video_quality_button_auto_description, "Recommended"),
            (self._video_quality_button_360p_description, "Lower data usage"),
            (self._video_quality_button_720p_description, "Best quality"),
        ]
        self._video_quality_check_marks = {
            values.AUTO: self._selected_video_quality_check_mark_auto,
            values.LOWEST_QUALITY: self._selected_video_quality_check_mark_360p,
            values.MEDIUM_QUALITY: self._selected_video_quality_check_mark_540p,
            values.HIGHEST_QUALITY: self._selected_video_quality_check_mark_720p,
        }

    @property
    def title_text_settings(self):
        """Gets the Settings title text element.

        Returns:
            Element: The Settings title text element.
        """
        return self._title_text_settings

    @property
    def settings_category_text(self):
        """Gets the Settings category text element.

        Returns:
            Element: The Settings category text element.
        """
        return self._settings_category_text

    @property
    def settings_manage_account_text(self):
        """
        Getter for the 'Manage Account' element on the settings page.

        Returns:
            Element: The 'Manage Account' element.
        """
        return self._manage_account_text

    @property
    def video_button_text(self):
        """
        Getter for the Video button text element.

        Returns:
            Element: The Video button text element.
        """
        return self._video_button_text

    @property
    def restore_purchases_button_text(self):
        """
        Getter for the restore purchases button text element.

        Returns:
            Element: The restore purchases button text element.
        """
        return self._restore_purchases_button_text

    @property
    def wifi_only_label(self):
        """
        Getter for the Wi-Fi only label element on the settings page.

        Returns:
            Element: The Wi-Fi only label element.
        """
        return self._wifi_only_label

    @property
    def wifi_only_description_label(self):
        """
        Getter for the Wi-Fi only label element on the settings page.

        Returns:
            Element: The Wi-Fi only label element.
        """
        return self._wifi_only_description_label

    @property
    def wifi_only_toggle_button(self):
        """
        Getter for the Wi-Fi only toggle button element on the settings page.

        Returns:
            Element: The Wi-Fi only toggle button element.
        """
        return self._wifi_only_toggle_button

    @property
    def video_quality_button(self):
        """
        Getter for the Wi-Fi only label element on the settings page.

        Returns:
            Element: The Wi-Fi only label element.
        """
        return self._video_quality_button

    @property
    def help_us_improve_link(self):
        """
        Getter for the help us improve link element on the settings page.

        Returns:
            Element: The help us improve link element.
        """
        return self._help_us_improve_link

    @property
    def share_my_info_button(self):
        """
        Getter for the share my info button element on the settings page.

        Returns:
            Element: The share my info button element.
        """
        return self._share_my_info_button

    def get_video_quality_button(self, quality_option):
        """
        Get the required video quality button element

        Returns:
            Element: video quality button element.
        """
        if not quality_option or quality_option not in self._video_quality_option_buttons.keys():
            raise ValueError("quality_option parameter value is either empty or invalid")
        return self._video_quality_option_buttons[quality_option]

    def verify_video_download_quality_sub_text(self, expected_text):
        """
        Verify the video quality sub text.

        Args:
            expected_text (str): The expected sub text.
        """
        expected_text_element = self.video_quality_button.get_child_element(
            Element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{expected_text}")')
        )
        expect(expected_text_element).to_exist()

    def verify_all_video_quality_option_button_exist(self):
        """
        Verify that the video quality option exists in the Video quality list.

        """
        for video_quality_option_button in self._video_quality_option_buttons.values():
            expect(video_quality_option_button).to_exist()

    def verify_all_video_quality_option_titles(self):
        """
        Verify that the video quality option have expected title in the Video quality list.
        """
        for video_quality_option_title, expected_title in self._video_quality_option_titles:
            expect(video_quality_option_title).to_have(expected_title)

    def verify_all_video_quality_option_descriptions(self):
        """
        Verify that the video quality option have expected title in the Video quality list.
        """
        for video_quality_option_desc, expected_desc in self._video_quality_option_descriptions:
            expect(video_quality_option_desc).to_have(expected_desc)

    def verify_video_quality_button_is_selected(self, quality_option: str):
        """
        Verify that the video quality option is selected.

        Args:
            quality_option (str): The video quality option.
        """
        if not quality_option or quality_option not in self._video_quality_option_buttons.keys():
            raise ValueError("quality_option parameter value is either empty or invalid")
        quality_option_button: Element = self._video_quality_option_buttons[quality_option]
        quality_option_button.get_child_element(self._video_quality_check_marks[quality_option])

    def verify_app_version(self, expected_version: str):
        """
        Verify the app version.
        Args:
            expected_version (str): The expected app version
        """
        expect(self.find_by_text_on_screen(f"Version: {expected_version}")).to_exist()
        expect(self.find_by_text_on_screen("Up-to-date")).to_exist()

    @staticmethod
    def verify_video_streaming_quality_sub_text(expected_text):
        """
        Verify the video streaming quality sub text.

        Args:
            expected_text (str): The expected sub text.
        """
        expected_text_element = Element(
            AppiumBy.XPATH,
            f"//android.widget.TextView[@text='Video streaming quality']/following-sibling::*[@text='{expected_text}']",
        )
        expect(expected_text_element).to_exist()
