"""
   Module covers Android base page
"""

from framework.element import Element
from appium.webdriver.common.appiumby import AppiumBy
from tests.android.pages import android_elements
from tests.common.globals import Globals


class AndroidBasePage:
    """
     Base page for all Android Pages
    """

    def __init__(self):
        # self.driver = driver
        # self.global_contents = Globals(setup_logging)
        # self.log = setup_logging
        self.textview_drawer_account_option = None
        # self.global_contents.flag = False
        self.account_logout_option = None
        self.target_activity = None
        self._screen_title = Element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("txt_screen_title")')
        self._back_navigation_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().description("ib_back")')
        self._text_view = Element(AppiumBy.CLASS_NAME, 'android.widget.TextView')
        self._android_native_permissoin_allow_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_allow_button")')
        self._android_native_permissoin_revoke_button = Element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.android.permissioncontroller:id/permission_deny_button")')
    
    @property
    def screen_title(self) -> Element:
        """
        Get screen title
        return: screen title
        """
        return self._screen_title

    @property
    def back_navigation_button(self) -> Element:
        """
        Navigate back
        return: back navigation button
        """
        return self._back_navigation_button
    
    @property
    def text_view(self) -> Element:
        """"""
        return self._text_view

    @property
    def allow_notifications_button(self) -> Element:
        """Get Allow button

        Returns:
            Element: allow permissions button
        """

        return self._android_native_permissoin_allow_button
    
    @property
    def revoke_notifications_button(self) -> Element:
        """Get revoke button

        Returns:
            Element: revoke permissoin button
        """

        return self._android_native_permissoin_allow_button

    def find_by_text_on_screen(self, text: str) -> Element:
        """"""
        if text:
            return Element(AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")').find()        
        raise ValueError('text cannot be empty')
        