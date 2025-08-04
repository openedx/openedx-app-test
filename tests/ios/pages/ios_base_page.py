"""
Module covers iOS base page
"""

from enum import Enum

from appium.webdriver.common.appiumby import AppiumBy

from framework import Element, expect
from tests.common.enums.general_enums import IosClassViews


class IosBasePage:
    """
    Base page for all iOS Pages
    """

    def __init__(self):
        self._back_button_navigation = Element(AppiumBy.ACCESSIBILITY_ID, "back_button")
        self._notification_allow_button = Element(AppiumBy.ACCESSIBILITY_ID, "Allow")
        self._screen_heading_title = Element(AppiumBy.ACCESSIBILITY_ID, "title_text")
        self._navigation_bar_title = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeNavigationBar")
        self._snackbar_text_message = Element(AppiumBy.ACCESSIBILITY_ID, "snackbar_text")
        self._progress_bar = Element(AppiumBy.ACCESSIBILITY_ID, "progress_bar")
        self._picker_title_label = Element(AppiumBy.ACCESSIBILITY_ID, "picker_title_text")
        self._picker_search_textfield = Element(
            AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`name == "picker_search_textfield"`]'
        )
        self._static_text = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeStaticText")
        self._button = Element(AppiumBy.CLASS_NAME, "XCUIElementTypeButton")
        self._picker_accept_button = Element(AppiumBy.NAME, "picker_accept_button")
        self._choose_button = Element(AppiumBy.ACCESSIBILITY_ID, "Choose")
        self._accept_cookies_button = Element(AppiumBy.ACCESSIBILITY_ID, "Accept Cookies")
        self._reject_cookies_button = Element(AppiumBy.ACCESSIBILITY_ID, "Reject All")
        self._privacy_choices_button = Element(AppiumBy.ACCESSIBILITY_ID, "Your Privacy Choices")
        self._ai_assistant_dismiss_button = Element(AppiumBy.ACCESSIBILITY_ID, "Close proactive message")
        self._openedx_ai_chat_bot = Element(AppiumBy.ACCESSIBILITY_ID, "Open XPERT Chatbot")
        self._openedx_ai_chat_bot_web_alert = Element(AppiumBy.ACCESSIBILITY_ID, "web alert dialogue")
        self._openedx_ai_chat_bot_dialogue_msg = Element(
            AppiumBy.IOS_PREDICATE, 'label == "I\'m Xpert, an AI assistant to help you find things."'
        )

    @property
    def static_text(self) -> Element:
        """
        Get static text element
        Returns:
            Element: static text element locator
        """
        return self._static_text

    @property
    def button(self) -> Element:
        """
        Get button element
        Returns:
            Element: button element locator
        """
        return self._button

    @property
    def back_navigation_button(self) -> Element:
        """
        Get main dashboard back icon
        Returns:
            Element: back navigation button element locator
        """

        return self._back_button_navigation

    @property
    def allow_notifications_button(self) -> Element:
        """
        Get Allow button

        Returns:
            Element: Allow Element
        """

        return self._notification_allow_button

    @property
    def screen_heading_title(self):
        """
        Get heading title elements

        Returns:
            Element: screen heading title element
        """

        return self._screen_heading_title

    @property
    def navigation_bar_title(self):
        """
        Get discovery title

        Returns:
            Element: discovery title element
        """

        return self._navigation_bar_title

    @property
    def snackbar_text_message(self):
        """
        Get snackbar text message

        Returns:
            Element: snackbar text message element
        """

        return self._snackbar_text_message

    @property
    def progress_bar(self):
        """
        Get progress bar

        Returns:
            Element: progress bar element
        """

        return self._progress_bar

    @property
    def picker_title_text(self) -> Element:
        """
        picker title text

        Returns:
            Element: picker title text
        """

        return self._picker_title_label

    @property
    def option_picker_search_field(self) -> Element:
        """
        option picker search field

        Returns:
            Element: option picker search field
        """

        return self._picker_search_textfield

    @property
    def get_picker_accept_button(self) -> Element:
        """picker accept button

        Returns:
            Element: picker accept button
        """

        return self._picker_accept_button

    @property
    def img_picker_choose_button(self) -> Element:
        """image picker choose button

        Element: picker choose button
        """
        return self._choose_button

    def search_and_verify_option_exists(self, option: Enum):
        """
        Search and verify that a picker option exists

        Args:
            option: Any enum-like object with a .value attribute
        """

        self.option_picker_search_field.clear_and_type(option.value)
        option_element = Element(
            AppiumBy.IOS_CLASS_CHAIN, f'**/XCUIElementTypePickerWheel[`value == "{option.value}"`]'
        )
        expect(option_element).to_exist()

    @staticmethod
    def find_all_views_on_screen(view_name: IosClassViews) -> Element:
        """
        Find all views on the screen by their class name

        Args:
            view_name (IosClassViews): The class view to search for

        Returns:
            Element: An element representing the collection of all matching views
        """
        return Element(AppiumBy.CLASS_NAME, f"XCUIElementType{view_name.value}").find_all()

    @staticmethod
    def find_by_text_on_screen(text: str, partial: bool = False, scroll=False) -> Element:
        """
        Find an element on the screen by its text

        Args:
            text (str): element text to search for
            partial (bool): whether to search for a partial match
            scroll (bool): whether to scroll and find the element

        Returns:
            Element: found element
        """
        if text:
            selector = f'label == "{text}"'
            if partial:
                selector = f'label CONTAINS "{text}"'
            element_locator = Element(AppiumBy.IOS_PREDICATE, selector)
            return element_locator.scroll_and_find() if scroll else element_locator.find()
        raise ValueError("text cannot be empty")

    @property
    def accept_cookies_button(self) -> Element:
        """
        Get Accept Cookies button

        Returns:
            Element: Accept Cookies button element
        """
        return self._accept_cookies_button

    @property
    def reject_cookies_button(self) -> Element:
        """
        Get Reject Cookies button

        Returns:
            Element: Reject Cookies button element
        """
        return self._reject_cookies_button

    @property
    def privacy_choices_button(self) -> Element:
        """
        Get Privacy Choices button

        Returns:
            Element: Privacy Choices button element
        """
        return self._privacy_choices_button

    @property
    def ai_assistant_dismiss_button(self) -> Element:
        """
        Get AI Assistant Dismiss button

        Returns:
            Element: AI Assistant Dismiss button element
        """
        return self._ai_assistant_dismiss_button

    @property
    def openedx_ai_chat_bot(self) -> Element:
        """
        Get Open edX AI Chat Bot button

        Returns:
            Element: Open edX AI Chat Bot button element
        """
        return self._openedx_ai_chat_bot

    @property
    def openedx_ai_chat_bot_web_alert(self) -> Element:
        """
        Get Open edX AI Chat Bot web alert

        Returns:
            Element: Open edX AI Chat Bot web alert element
        """
        return self._openedx_ai_chat_bot_web_alert

    @property
    def openedx_ai_chat_bot_dialogue_msg(self) -> Element:
        """
        Get Open edX AI Chat Bot dialogue message

        Returns:
            Element: Open edX AI Chat Bot dialogue message element
        """
        return self._openedx_ai_chat_bot_dialogue_msg
