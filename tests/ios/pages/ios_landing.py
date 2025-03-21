"""
    New Landing Page Module
"""

from tests.ios.pages import ios_elements
from tests.ios.pages.ios_base_page import IosBasePage


class IosLanding(IosBasePage):
    """
    New Landing screen
    """

    def get_logo_image(self):
        """
        Get logo image

        Returns:
            webdriver element: logo image element
        """

        logo_image = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.landing_logo_image
            )
        return logo_image

    def get_search_courses_field(self):
        """
        Get search courses field

        Returns:
            webdriver element: search courses field element
        """

        search_courses_field = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.landing_explore_search_textfield
            )
        return search_courses_field

    def get_welcome_message(self):
        """
        Get welcome message

        Returns:
            webdriver element: welcome message element
        """

        welcome_message = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.landing_heading_text
            )
        return welcome_message

    def get_search_title(self):
        """
        Get search title

        Returns:
            webdriver element: search title element
        """

        search_title = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.landing_search_title
            )
        return search_title

    def get_discovery_title(self):
        """
        Get discovery title

        Returns:
            webdriver element: discovery title element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.navigation_bar_title
            )

        navigation_bar = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.navigation_bar_title
            )
        return navigation_bar

    def get_back_button(self):
        """
        Get discovery title

        Returns:
            webdriver element: discovery title element
        """

        back_button = self.global_contents.wait_and_get_element(
            self.driver,
            'Start'
            )
        return back_button

    def get_header_back_button(self):
        """
        Returns:
            element: back button element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.back_button_navigation
        )

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.back_button_navigation
        )

    def load_landing_screen(self):
        """
        Get discovery screen

        Returns:
            webdriver element: discovery title element
        """

        self.get_back_button().click()
        # self.global_contents.wait_and_get_element(self.driver, 'Back').click()
        return self.get_logo_image()

    def get_register_button(self):
        """
        Get register button

        Returns:
            webdriver element: register button element
        """

        register_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.logistration_register_button
            )
        return register_button

    def get_register_screen_title(self):
        """
        Get register button

        Returns:
            webdriver element: register button element
        """

        register_title = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.register_screen_title
            )
        return register_title

    def get_sign_in_button(self):
        """
        Get Sing In

        Returns:
            webdriver element: Sing In Element
        """

        sign_in_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.logistration_signin_button
        )
        return sign_in_button

    def get_allow_notifications_button(self):
        """
        Get Allow button

        Returns:
            webdriver element: Allow Element
        """

        self.global_contents.wait_for_element_visibility(
            self.driver,
            ios_elements.notification_allow_button)

        return self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.notification_allow_button)

    def get_get_explore_courses_button(self):
        """
        Get Explore Courses button

        Returns:
            webdriver element: Explore Courses Element
        """

        explore_courses_button = self.global_contents.wait_and_get_element(
            self.driver,
            ios_elements.landing_explore_courses_button
        )
        return explore_courses_button
