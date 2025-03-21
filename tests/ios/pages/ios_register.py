"""
    Login Page Module
"""
from appium.webdriver.common.appiumby import AppiumBy

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosRegister(IosBasePage):
    """
    Register screen
    """

    def get_register_button(self):
        """
        Get register button

        Returns:
            webdriver element: Register Element
        """

        register_button = self.global_contents.get_all_views_on_ios_screen(
            self.driver, ios_elements.all_buttons
        )[1]
        return register_button

    def get_register_screen_heading(self):
        """
        Get register screen heading

        Returns:
            webdriver element: Register screen heading Element
        """

        register_heading = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_screen_heading
        )
        return register_heading

    def get_password_field(self):
        """
        Get password fields element

        Returns:
            webdriver element: editfield element
        """

        password_field = self.driver.find_element(
            AppiumBy.CLASS_NAME, ios_elements.password_field
        )
        return password_field

    def get_signup_text(self):
        """
        Get signup text

        Returns:
            webdriver element: signup text element
        """

        signup_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_signup_text
        )
        return signup_text

    def get_signup_subtitle_text(self):
        """
        Get signup subtitle text

        Returns:
            webdriver element: signup subtitle text element
        """

        signup_subtitle_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_signup_subtitle_text
        )
        return signup_subtitle_text

    def get_name_text(self):
        """
        Get name text

        Returns:
            webdriver element: name text element
        """

        name_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_name_text
        )
        return name_text

    def get_name_textfield(self):
        """
        Get name textfield

        Returns:
            webdriver element: name textfield element
        """

        name_textfield = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_name_textfield
        )
        return name_textfield

    def get_name_instructions_text(self):
        """
        Get name instructions text

        Returns:
            webdriver element: name instructions text element
        """

        name_instructions_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_name_instructions_text
        )
        return name_instructions_text

    def get_username_text(self):
        """
        Get username text

        Returns:
            webdriver element: username text element
        """

        username_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_username_text
        )
        return username_text

    def get_username_textfield(self):
        """
        Get username textfield

        Returns:
            webdriver element: username textfield element
        """

        username_textfield = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_username_textfield
        )
        return username_textfield

    def get_username_instructions_text(self):
        """
        Get username instructions text

        Returns:
            webdriver element: username instructions text element
        """

        username_instructions_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_username_instructions_text
        )
        return username_instructions_text

    def get_email_text(self):
        """
        Get email text

        Returns:
            webdriver element: email text element
        """

        email_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_email_text
        )
        return email_text

    def get_email_textfield(self):
        """
        Get email textfield

        Returns:
            webdriver element: email textfield element
        """

        email_textfield = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_email_textfield
        )
        return email_textfield

    def get_email_instructions_text(self):
        """
        Get email instructions text

        Returns:
            webdriver element: email instructions text element
        """

        email_instructions_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_email_instructions_text
        )
        return email_instructions_text

    def get_password_text(self):
        """
        Get password text

        Returns:
            webdriver element: password text element
        """

        password_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_password_text
        )
        return password_text

    def get_password_textfield(self):
        """
        Get password textfield

        Returns:
            webdriver element: password textfield element
        """

        password_textfield = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_password_textfield
        )
        return password_textfield

    def get_password_instructions_text(self):
        """
        Get password instructions text

        Returns:
            webdriver element: password instructions text element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver, ios_elements.register_password_instructions_text
        )

        password_instructions_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_password_instructions_text
        )
        return password_instructions_text

    def get_country_text(self):
        """
        Get country text

        Returns:
            webdriver element: country text element
        """

        country_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_country_text
        )
        return country_text

    def get_country_textfield(self):
        """
        Get country textfield

        Returns:
            webdriver element: country textfield element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver, ios_elements.register_country_picker_button
        )

        country_textfield = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_country_picker_button
        )
        return country_textfield

    def get_country_instructions_text(self):
        """
        Get country instructions text

        Returns:
            webdriver element: country instructions text element
        """

        country_instructions_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_country_instructions_text
        )
        return country_instructions_text

    def get_show_optional_fields(self):
        """
        Get show optional fields

        Returns:
            webdriver element: show optional fields element
        """

        show_optional_fields = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_show_optional_fields
        )
        return show_optional_fields

    def get_create_account_button(self):
        """
        Get create account button

        Returns:
            webdriver element: create account button element
        """

        create_account_button = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_signup_button
        )
        return create_account_button

    def get_social_auth_title_text(self):
        """
        Get social auth title text

        Returns:
            webdriver element: social auth title text element
        """

        social_auth_title_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_social_auth_title_text
        )
        return social_auth_title_text

    def select_country(self):
        """
        Get country spinner

        Returns:
            webdriver elements: country search field
        """

        country_field = self.global_contents.get_elements_by_name_ios(
            self.driver, ios_elements.register_picker_search_textfield
        )[1]
        return country_field

    def get_picker_accept_button(self):
        """
        Get picker accept button

        Returns:
            webdriver elements: picker accept button
        """

        picker_accept_button = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_picker_accept_button
        )
        return picker_accept_button

    def get_picker_title_text(self):
        """
        Get picker title text

        Returns:
            webdriver elements: picker title text
        """

        picker_title_text = self.global_contents.wait_and_get_element(
            self.driver, ios_elements.register_country_picker_title
        )
        return picker_title_text
