"""
    Sign In Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage
from appium.webdriver.common.appiumby import AppiumBy


class AndroidSignIn(AndroidBasePage):
    """
    Sign in screen
    """

    def get_sign_in_description(self):
        """
        Get sign in description

        Returns:
            element: sign in description element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.sign_in_description
        )

    def get_sign_in_email_label(self):
        """
        Get sign in email label

        Returns:
            element: sign in email label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.sign_in_email_label
        )

    def get_sign_in_tf_email(self):
        """
        Get sign in email text field

        Returns:
            element: sign in email text field element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.sign_in_tf_email
        )

    def get_sign_in_password_label(self):
        """
        Get sign in password label

        Returns:
            element: sign in password label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.sign_in_password_label
        )

    def get_sign_in_password_field(self):
        """
        Get sign in password field

        Returns:
            element: sign in password field element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.sign_in_tf_password
        )

    def get_sign_in_forgot_password(self):
        """
        Get sign in forgot password

        Returns:
            element: sign in forgot password element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.sign_in_forgot_password
        )

    def get_google_auth_button(self):
        """
        Get google auth button

        Returns:
            element: google auth button element
        """

        google_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                            f'new UiSelector().description("Sign in with Google")')
        return google_btn

    def get_facebook_auth_button(self):
        """
        Get facebook auth button

        Returns:
            element: facebook auth button element
        """

        facebook_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                            f'new UiSelector().description("Sign in with Facebook")')
        return facebook_btn

    def get_microsoft_auth_button(self):
        """
        Get microsoft auth button

        Returns:
            element: microsoft auth button element
        """

        microsoft_btn = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                            f'new UiSelector().description("Sign in with Microsoft")')
        return microsoft_btn

    def get_signin_button(self):
        """
        Get signin button

        Returns:
            element: Signin button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_signin_button
        )

    def get_forgot_password_title(self):
        """
        Get forgot password title

        Returns:
            element: forgot password title element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.forgot_password_title
        )

    def get_forgot_password_reset_button(self):
        """
        Get forgot password reset button

        Returns:
            element: forgot password reset button element
        """

        reset_btn = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.forgot_password_reset_button
        )
        btn_text = reset_btn.find_element(AppiumBy.CLASS_NAME,
            android_elements.all_textviews)
        return btn_text

    def get_all_textviews(self):
        """
        Get all textviews elements

        Returns:
            List of webdriver elements: textview elements
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.all_textviews
        )
        all_textview_elements = self.global_contents.get_all_views_on_screen(
            self.driver,
            android_elements.all_textviews
        )
        return all_textview_elements
