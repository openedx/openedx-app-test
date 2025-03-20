"""
    Login Page Module
"""

from appium.webdriver.common.appiumby import AppiumBy
from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosLogin(IosBasePage):
    """
    Login screen
    """

    def get_sign_in_title(self):
        """
        Get Sing In

        Returns:
            webdriver element: Sing In Element
        """

        sign_in_title = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_text
        )
        return sign_in_title

    def get_password_field(self):
        """
        Get password fields element

        Returns:
            webdriver element: editfield element
        """

        password_field = self.driver.find_element(
            AppiumBy.CLASS_NAME, ios_elements.password_field)
        return password_field

    def get_signin_welcome_text(self):
        """
        Get Sing In welcome text

        Returns:
            webdriver element: Singin welcome text element
        """

        signin_welcome_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_welcome_text
        )
        return signin_welcome_text

    def get_signin_username_text(self):
        """
        Get username text

        Returns:
            webdriver element: username text element
        """

        signin_username_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_username_text
        )
        return signin_username_text

    def get_signin_username_textfield(self):
        """
        Get username textfield

        Returns:
            webdriver element: username textfield element
        """

        signin_username_textfield = self.global_contents.get_elements_by_name_ios(
            self.driver,
            ios_elements.signin_username_textfield
        )[1]
        return signin_username_textfield

    def get_signin_password_text(self):
        """
        Get password text

        Returns:
            webdriver element: password text element
        """

        signin_password_text = self.global_contents.get_element_by_name_ios(
            self.driver,
            ios_elements.signin_password_text
        )
        return signin_password_text

    def get_signin_password_textfield(self):
        """
        Get password textfield

        Returns:
            webdriver element: password textfield element
        """

        signin_password_textfield = self.global_contents.get_elements_by_name_ios(
            self.driver,
            ios_elements.signin_password_textfield
        )[1]
        return signin_password_textfield

    def get_signin_forgot_password_button(self):
        """
        Get forgot password button

        Returns:
            webdriver element: forgot password button element
        """

        signin_forgot_password_button = self.global_contents.get_element_by_name_ios(
            self.driver,
            ios_elements.signin_forgot_password_button
        )
        return signin_forgot_password_button

    def get_signin_button(self):
        """
        Get signin button

        Returns:
            webdriver element: signin button element
        """

        signin_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_button
        )
        return signin_button

    def get_signin_social_auth_title_text(self):
        """
        Get social auth title text

        Returns:
            webdriver element: social auth title text element
        """

        signin_social_auth_title_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_social_auth_title_text
        )
        return signin_social_auth_title_text

    def get_signin_social_auth_google_button(self):
        """
        Get social auth google button text

        Returns:
            webdriver element: signin social auth google button
        """

        signin_social_auth_google_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_social_auth_google_button
        )
        return signin_social_auth_google_button

    def get_signin_social_auth_facebook_button(self):
        """
        Get social auth facebook button text

        Returns:
            webdriver element: signin social auth facebook button
        """

        signin_social_auth_facebook_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_social_auth_facebook_button
        )
        return signin_social_auth_facebook_button

    def get_signin_social_auth_microsoft_button(self):
        """
        Get social auth microsoft button text

        Returns:
            webdriver element: signin social auth microsoft button
        """

        sigin_social_auth_microsoft_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.sigin_social_auth_microsoft_button
        )
        return sigin_social_auth_microsoft_button

    def get_signin_social_auth_apple_button(self):
        """
        Get social auth apple button text

        Returns:
            webdriver element: signin social auth apple button
        """

        signin_social_auth_apple_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.signin_social_auth_apple_button
        )
        return signin_social_auth_apple_button

    def get_forgot_title_text(self):
        """
        Get forgot title text

        Returns:
            webdriver element: forgot title text element
        """

        forgot_title_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.forgot_title_text
        )
        return forgot_title_text

    def get_forgot_description_text(self):
        """
        Get forgot description text

        Returns:
            webdriver element: forgot description text element
        """

        forgot_description_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.forgot_description_text
        )
        return forgot_description_text

    def get_forgot_email_text(self):
        """
        Get forgot email text

        Returns:
            webdriver element: forgot email text element
        """

        forgot_email_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.forgot_email_text
        )
        return forgot_email_text

    def get_forgot_email_textfield(self):
        """
        Get forgot email textfield

        Returns:
            webdriver element: forgot email textfield element
        """

        forgot_email_textfield = self.global_contents.get_elements_by_name_ios(
            self.driver,
            ios_elements.forogt_email_textfield
        )[1]
        return forgot_email_textfield

    def get_forgot_reset_password_button(self):
        """
        Get forgot reset password button

        Returns:
            webdriver element: forgot reset password button element
        """

        forgot_reset_password_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.forgot_reset_password_button
        )
        return forgot_reset_password_button

    def get_forgot_check_email_image(self):
        """
        Get forgot check email image

        Returns:
            webdriver element: forgot check email image element
        """

        forgot_check_email_image = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.forgot_check_email_image
        )
        return forgot_check_email_image

    def get_forgot_recover_title_text(self):
        """
        Get forgot recover title text

        Returns:
            webdriver element: forgot recover title text element
        """

        forgot_recover_title_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.forgot_recover_title_text
        )
        return forgot_recover_title_text

    def get_forgot_recover_description_text(self):
        """
        Get forgot recover description text

        Returns:
            webdriver element: forgot recover description text element
        """

        forgot_recover_description_text = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.forgot_recover_description_text
        )
        return forgot_recover_description_text
