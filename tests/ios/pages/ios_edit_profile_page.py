"""Edit profile page module"""

import datetime

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element
from tests.common.enums.general_enums import Country, Language
from tests.ios.pages.ios_profile import IosProfile


class IosEditProfilePage(IosProfile):
    """iOS Edit profile page"""

    def __init__(self):
        super().__init__()
        self._screen_title = Element(AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeStaticText[`name == 'Edit Profile'`]")
        self._done_button = Element(AppiumBy.IOS_CLASS_CHAIN, "**/XCUIElementTypeOther[`name == 'done_button'`]")
        self._profile_type_label = Element(AppiumBy.ACCESSIBILITY_ID, "profile_type_text")
        self._username_label = Element(AppiumBy.ACCESSIBILITY_ID, "username_text")
        self._switch_profile_type_button = Element(AppiumBy.ACCESSIBILITY_ID, "switch_profile_button")
        self._location_picker_label = Element(AppiumBy.ACCESSIBILITY_ID, "Location_text")
        self._spoken_language_picker_label = Element(AppiumBy.ACCESSIBILITY_ID, "Spoken language_text")
        self._location_picker_button = Element(AppiumBy.ACCESSIBILITY_ID, "Location_picker_button")
        self._spoken_language_picker_button = Element(AppiumBy.ACCESSIBILITY_ID, "Spoken language_picker_button")
        self._user_bio_label = Element(AppiumBy.ACCESSIBILITY_ID, "about_text")
        self._user_bio_value = Element(AppiumBy.ACCESSIBILITY_ID, "short_bio_textarea")
        self._change_profile_img_button = Element(AppiumBy.ACCESSIBILITY_ID, "change_profile_image_button")
        self._change_profile_img_title_label = Element(AppiumBy.ACCESSIBILITY_ID, "profile_bottom_sheet_title_text")
        self._remove_img_button = Element(AppiumBy.ACCESSIBILITY_ID, "remove_picture_button")
        self._ic_remove_img = Element(AppiumBy.ACCESSIBILITY_ID, "removePhoto")
        self._select_img_button = Element(AppiumBy.ACCESSIBILITY_ID, "select_picture_button")
        self._ic_select_img = Element(AppiumBy.ACCESSIBILITY_ID, "gallery")
        self._cancel_button = Element(AppiumBy.ACCESSIBILITY_ID, "cancel_button")

    @property
    def screen_title(self):
        """Get screen title

        Returns:
            Element: screen title
        """
        return self._screen_title

    @property
    def done_button(self):
        """Get done button

        Returns:
            Element: done button
        """
        return self._done_button

    @property
    def profile_type_label(self):
        """Get profile type label

        Returns:
            Element: profile type label
        """
        return self._profile_type_label

    @property
    def username_label(self):
        """Get username label

        Returns:
            Element: username label
        """
        return self._username_label

    @property
    def switch_profile_type_button(self):
        """Get switch profile type button

        Returns:
            Element: switch profile type button
        """
        return self._switch_profile_type_button

    @property
    def location_picker_label(self):
        """Get location field label

        Returns:
            Element: location field label
        """
        return self._location_picker_label

    @property
    def location_picker_button(self):
        """Get location picker button

        Returns:
            Element: location picker button
        """
        return self._location_picker_button

    @property
    def spoken_language_picker_label(self):
        """Get spoken language field label

        Returns:
            Element: spoken language field label
        """
        return self._spoken_language_picker_label

    @property
    def spoken_language_picker_button(self):
        """Get spoken language picker button

        Returns:
            Element: spoken language picker button
        """
        return self._spoken_language_picker_button

    @property
    def user_bio_label(self):
        """Get user bio label

        Returns:
            Element: user bio label
        """
        return self._user_bio_label

    @property
    def user_bio_value(self):
        """Get user bio value

        Returns:
            Element: user bio value
        """
        return self._user_bio_value

    @property
    def change_profile_img_button(self):
        """change profile img button

        Returns:
            Element: change profile img button
        """

        return self._change_profile_img_button

    @property
    def change_profile_img_title_label(self):
        """change profile img button

        Returns:
            Element: change profile img button
        """

        return self._change_profile_img_title_label

    @property
    def remove_img_button(self):
        """remove img button
        Returns:
            Element: remove img button
        """

        return self._remove_img_button

    @property
    def ic_remove_img(self):
        """icon remove img

        Returns:
            Element: icon remove img
        """

        return self._ic_remove_img

    @property
    def ic_select_img(self):
        """icon select img

        Returns:
            Element: icon select img
        """

        return self._ic_select_img

    @property
    def select_img_button(self):
        """select profile img button

        Returns:
            Element: select profile img button
        """

        return self._select_img_button

    @property
    def cancel_button(self):
        """cancel button

        Returns:
            Element: cancel button button
        """

        return self._cancel_button

    def search_and_verify_country_option_exists(self, country_option: Country):
        """Search and verify country option exists

        Args:
            country_option(Country): education option to search for
        """
        self.search_and_verify_option_exists(country_option)

    def search_and_verify_language_option_exists(self, country_option: Language):
        """Search and verify country option exists

        Args:
            country_option(Language): education option to search for
        """
        self.search_and_verify_option_exists(country_option)

    def select_image_from_gallery(self):
        """Select image from photos app"""
        formatted_date = datetime.datetime.now().strftime("%d %B")
        image_label = f"Photo, {formatted_date}"
        pfp_element = Element(AppiumBy.IOS_PREDICATE, f"label CONTAINS '{image_label}'")
        pfp_element.click()
        self.img_picker_choose_button.click()
