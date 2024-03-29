"""
    Register Page Module
"""

from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidRegister(AndroidBasePage):
    """
    Register screen
    """

    def get_back_button(self):
        """
        Get back button

        Returns:
            element: Back button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_back_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_back_button
        )

    def get_register_title(self):
        """
        Get register title
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_sign_up_title
        )

    def get_register_description(self):
        """
        Get register description

        Returns:
            element: Register description element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_description
        )

    def get_register_txt_name_label(self):
        """
        Get register name label

        Returns:
            element: Register name label element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_name_label
        )

    def get_register_tf_name(self):
        """
        Get register name text field
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_tf_name
        )

    def get_register_txt_name_description(self):
        """
        Get register description label
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_txt_name_description
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_name_description
        )

    def get_register_txt_username_label(self):
        """
        Get register username label
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_username_label
        )

    def get_register_tf_username(self):
        """
        Get register username text field
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_tf_username
        )

    def get_register_txt_username_description(self):
        """
        Get register username description
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_username_description
        )

    def get_register_txt_email_label(self):
        """
        Get register email label
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_email_label
        )

    def get_register_tf_email(self):
        """
        Get register email text field
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_tf_email
        )

    def get_register_txt_email_description(self):
        """
        Get register email description
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_email_description
        )

    def get_register_txt_password_label(self):
        """
        Get register password label
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_password_label
        )

    def get_register_tf_password(self):
        """
        Get register password text field
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_tf_password
        )

    def get_register_txt_password_description(self):
        """
        Get register password description
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_password_description
        )

    def get_register_txt_country_label(self):
        """
        Get register country label
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_country_label
        )

    def get_register_tf_country(self):
        """
        Get register country text field
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_tf_country
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_tf_country
        )

    def get_register_txt_country_description(self):
        """
        Get register country description
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_country_description
        )

    def get_register_txt_honor_code(self):
        """
        Get register honor code
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_txt_honor_code
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_honor_code
        )

    def get_register_txt_optional_field(self):
        """
        Get register optional field
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_optional_field
        )

    def get_register_btn_create_account(self):
        """
        Get register create account button
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_btn_create_account
        )

    def get_register_education_level(self):
        """
        Get register education level
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_education_level
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_education_level
        )

    def get_register_education_level_placeholder(self):
        """
        Get register education level placeholder
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_education_level_placeholder
        )

    def get_register_gender_label(self):
        """
        Get registern gender label
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_gender_label
        )

    def get_gender_label_placeholder(self):
        """
        Get gender label placeholder
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_gender_label_placeholder
        )

    def get_register_country_selection_dialogue(self):
        """
        Get register country selection dialogue
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_country_selection_dialogue
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_country_selection_dialogue
        )

    def get_register_country_search(self):
        """
        Get register country search
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_country_sb_search
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_country_sb_search
        )

    def get_txt_US_title(self):
        """
        Get register country search
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.register_txt_US_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.register_txt_US_title
        )

    def get_txt_google_auth(self):
        """
        Get register google auth text
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.txt_google_auth
        )

    def get_txt_facebook_auth(self):
        """
        Get register facebook auth text
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.txt_facebook_auth
        )

    def get_txt_microsoft_auth(self):
        """
        Get register microsoft auth text
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.txt_microsoft_auth
        )

    def get_main_dashboard_footer(self):
        """
        Get main dashboard footer
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.main_dashboar_home_tab
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.main_dashboar_home_tab
        )
