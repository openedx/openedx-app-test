"""
    Landing Page Module
"""


from tests.android.pages import android_elements
from tests.android.pages.android_base_page import AndroidBasePage


class AndroidLanding(AndroidBasePage):
    """
    Landing screen
    """

    def get_screen_title(self):
        """
        Get landing screen title

        Returns:
            element: screen title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.landing_screen_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_screen_title
        )

    def get_search_label(self):
        """
        Get search label

        Returns:
            element: Search label element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.landing_search_label
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_search_label
        )

    def get_discovery_search(self):
        """
        Get discovery search

        Returns:
            element: Discovery search element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.landing_discovery_search
        )

        search_field = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_discovery_search
        )
        search_field.click()
        search_field.send_keys('python')
        self.driver.press_keycode(self.global_contents.android_enter_key)
        search_result_title = self.global_contents.get_txt_toolbar_title(self.driver)
        return search_result_title

    def get_explore_courses(self):
        """
        Get explore courses button

        Returns:
            element: Explore courses button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.landing_explore_courses_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_explore_courses_button
        )

    def get_register_button(self):
        """
        Get register button

        Returns:
            element: Register button element
        """

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_register_button
        )

    def load_register_screen(self):
        """
        Get register button

        Returns:
            element: Register button element
        """

        register_button = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_register_button
        )
        register_button.click()
        return self.get_screen_title()

    def load_signin_screen(self):
        """
        Get sign in button

        Returns:
            element: Signin button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.landing_signin_button
        )

        signin_button = self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.landing_signin_button
        )
        signin_button.click()
        return self.get_signin_title()

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

    def navigate_back_on_screen(self):
        """
        Navigate back on screen

        Returns:
            element: Back button element
        """

        # will update this method once we have a unique id on back button
        self.driver.back()
        self.driver.back()
        self.driver.back()

    def get_back_button(self):
        """
        Get back button

        Returns:
            element: Back button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.back_button
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.back_button
        )

    def get_signin_title(self):
        """
        Get signin title

        Returns:
            element: Signin title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            android_elements.signin_title
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            android_elements.signin_title
        )
