"""
Edit Profile Page Module
"""

from framework.element import Element
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.appiumby import AppiumBy


class AndroidEditProfile(AndroidBasePage):
    """
    Edit Profile screen
    """

    def __init__(self):
        super().__init__()
        self._edit_profile_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_title")',
        )
        self._done_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("txt_done")')
        self._done_button_tick_mark = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("ic_done")')
        self._edit_profile_type_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_type_label")',
        )
        self._edit_profile_user_name = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_user_name")',
        )
        self._edit_profile_limited_profile_message = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_limited_profile_message")',
        )
        self._edit_profile_txt_label_location = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_label_location")',
        )
        self._edit_profile_tf_select_location = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_select_location")',
        )
        self._edit_profile_txt_label_spoken_language = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_label_spoken_language")',
        )
        self._spoken_language_text_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("tf_select_spoken_language")',
        )
        self._edit_profile_placeholder_select_spoken_language = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_placeholder_spoken_language")',
        )
        self._edit_profile_txt_label_about_me = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_label_about_me")',
        )
        self._edit_profile_txt_placeholder_about_me = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_placeholder_about_me")',
        )
        self._about_me_text_field = Element(
            AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("tf_input_about_me")'
        )
        self._profile_img_profile = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("img_profile")')
        self._profile_txt_name = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_profile_name")',
        )
        self._edit_profile_user_image = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("img_edit_profile_user_image")',
        )
        self._change_image_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_change_image_title")',
        )
        self._switch_profile_type_label = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_edit_profile_limited_profile_label")',
        )
        self._drop_down_title = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_selection_title")',
        )
        self._select_from_gallery_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("btn_select_from_gallery")',
        )
        self._ic_select_from_gallery = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("ic_select_from_gallery")',
        )
        self._text_select_from_gallery = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_select_from_gallery")',
        )
        self._remove_photo_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("btn_remove_photo")',
        )
        self._ic_remove_photo = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("ic_remove_photo")',
        )
        self._text_remove_photo = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_remove_photo")',
        )
        self._change_profile_image_cancel_button = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("btn_cancel")',
        )
        self._change_profile_image_cancel_button_text = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().resourceId("txt_cancel")',
        )
        self._image_to_upload = Element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().description("Photo taken on Feb 26, 2025 5:53 PM")',
        )

    @property
    def image_to_upload(self) -> Element:
        """
        Returns:
            Element: change profile image cancel element
        """

        return self._image_to_upload

    @property
    def change_profile_image_cancel_button_text(self) -> Element:
        """
        Returns:
            Element: change profile image cancel text element
        """

        return self._change_profile_image_cancel_button_text

    @property
    def change_profile_image_cancel_button(self) -> Element:
        """
        Returns:
            Element: change profile image cancel button element
        """

        return self._change_profile_image_cancel_button

    @property
    def ic_remove_photo(self) -> Element:
        """
        Returns:
            Element: ic remove photo element
        """

        return self._ic_remove_photo

    @property
    def text_remove_photo(self) -> Element:
        """
        Returns:
            Element: remove photo text element
        """

        return self._text_remove_photo

    @property
    def remove_photo_button(self) -> Element:
        """
        Returns:
            Element: remove photo button element
        """
        return self._remove_photo_button

    @property
    def ic_select_from_gallery(self) -> Element:
        """
        Returns:
            Element: ic select from gallery element
        """

        return self._ic_select_from_gallery

    @property
    def text_select_from_gallery(self) -> Element:
        """
        Returns:
            Element: select from gallery text element
        """

        return self._text_select_from_gallery

    @property
    def select_from_gallery_button(self) -> Element:
        """
        Returns:
            Element: select from gallery button element
        """
        return self._select_from_gallery_button

    @property
    def edit_profile_title(self) -> Element:
        """
        Returns:
            Element: edit profile title element
        """

        return self._edit_profile_title

    @property
    def get_profile_img_profile(self) -> Element:
        """
        Returns:
            Element: profile image element
        """

        return self._profile_img_profile

    @property
    def get_profile_txt_name(self) -> Element:
        """
        Returns:
            Element: profile text name element
        """

        return self._profile_txt_name

    @property
    def done_button(self) -> Element:
        """
        Returns:
            Element: Done button element
        """

        return self._done_button

    @property
    def done_button_tick_mark(self) -> Element:
        """
        Returns:
            Element: Done button tick mark element
        """

        return self._done_button_tick_mark

    @property
    def edit_profile_type_label(self) -> Element:
        """
        Returns:
            Element: edit profile type label element
        """

        return self._edit_profile_type_label

    @property
    def get_edit_profile_user_image(self) -> Element:
        """
        Returns:
            Element: edit profile user image element
        """

        return self._edit_profile_user_image

    @property
    def change_profile_image_title_label(self) -> Element:
        """
        Returns:
            Element: edit profile user image title label element
        """

        return self._change_image_title

    @property
    def edit_profile_user_name(self) -> Element:
        """
        Returns:
            Element: edit profile user name element
        """

        return self._edit_profile_user_name

    @property
    def edit_profile_limited_profile_message(self) -> Element:
        """
        Returns:
            Element: edit profile limited profile message element
        """

        return self._edit_profile_limited_profile_message

    @property
    def edit_profile_txt_label_location(self) -> Element:
        """
        Returns:
            Element: edit profile location label element
        """

        return self._edit_profile_txt_label_location

    @property
    def profile_tf_select_location(self) -> Element:
        """
        Returns:
            Element: edit profile select location element
        """

        return self._edit_profile_tf_select_location

    @property
    def edit_profile_placeholder_select_spoken_language(self) -> Element:
        """
        Returns:
            Element: edit profile select spoken language element
        """

        return self._edit_profile_placeholder_select_spoken_language

    @property
    def select_spoken_language(self) -> Element:
        """
        Returns:
            Element: edit profile select spoken language element
        """

        return self._spoken_language_text_field

    @property
    def edit_profile_txt_label_spoken_language(self) -> Element:
        """
        Returns:
            Element: edit profile label spoken language element
        """

        return self._edit_profile_txt_label_spoken_language

    @property
    def edit_profile_txt_label_about_me(self) -> Element:
        """
        Returns:
            Element: edit profile label about me element
        """

        return self._edit_profile_txt_label_about_me

    @property
    def edit_profile_txt_placeholder_about_me(self) -> Element:
        """
        Returns:
            Element: edit profile placeholder about me element
        """

        return self._edit_profile_txt_placeholder_about_me

    @property
    def switch_profile_type_button(self):
        """
        Returns:
            Element: switch profile type element
        """

        return self._switch_profile_type_label

    @property
    def about_me_input(self):
        """
        Returns:
            Element: about me input element
        """

        return self._about_me_text_field

    @property
    def drop_down_title(self):
        """
        Returns:
            Element: drop down title element
        """

        return self._drop_down_title
