"""
   Module covers Android & iOS screens' global contents
"""

import sys
import string
import random
import yaml

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.ios.pages import ios_elements
from tests.android.pages import android_elements
from tests.common import values

class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """

    AUT_PACKAGE_NAME = 'org.openedx.app'

    def __init__(self, project_log):
        # Read user_preferences.yml and set globals accordingly
        self.setup_global_environment()

        # CAPABILITIES
        self.ios_device_name = 'iPhone 15 Pro'
        self.android_device_name = 'Android Phone'
        self.project_log = project_log
        self.medium_timeout = 7
        self.minimum_timeout = 3
        self.maximum_timeout = 15
        self.index = 0
        self.android_enter_key = 66
        self.whats_new_enable = False

    def setup_global_environment(self):
        """
        set environment and read user_preferences for local run
        """

        with open("./tests/user_preferences.yml", "r") as user_file:
            user_preferences = yaml.safe_load(user_file)

        self.target_environment = user_preferences.get('Settings', {}).get('target_environment')
        self.server_url = user_preferences.get('Settings', {}).get('appium_server')
        self.android_platform_version = user_preferences.get('Settings', {}).get('android_platform_version')
        self.ios_platform_version = user_preferences.get('Settings', {}).get('ios_platform_version')
        self.aut_current_path = user_preferences.get('Settings', {}).get('aut_current_path')
        self.aut_latest_path = user_preferences.get('Settings', {}).get('aut_latest_path')
        self.login_user_name = user_preferences.get('User', {}).get('login_user_name')
        self.login_password = user_preferences.get('User', {}).get('login_password')

    def wait_and_get_element(self, driver, element_locator, optional_time=None):
        """
        Block until the element present on screen, then returns the element

        Arguments:
            driver (webdriver): webdriver instance variable
            element_locator (webdriver element) : target elements locator

        Return:
            webdriver element: target_element
        """
        element = None
        time_out = self.maximum_timeout

        if optional_time is not None:
            time_out = optional_time

        try:
            if self.target_environment == values.ANDROID:
                element = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                            f'new UiSelector().resourceId("{element_locator}")')
            elif self.target_environment == values.IOS:
                element = WebDriverWait(driver, time_out).until(
                    expected_conditions.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, element_locator)))

            self.project_log.info('Found - {} - {} - {} - {}'.format(
                element_locator,
                element.tag_name,
                element.text,
                element
            ))
            return element

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                element_locator,
                no_such_element_exception,
                sys.exc_info()[0]))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                element_locator,
                web_driver_exception,
                sys.exc_info()[0]))

    def get_all_views_on_screen(self, driver, target_elements):
        """
        Get list of Views on screen

        Arguments:
            driver (webdriver): webdriver instance variable
            target_elements (webdriver element): elements locator

        Return:
            webdriver elements: List of Views
        """

        all_views = None

        try:
            if self.target_environment == values.ANDROID:
                all_views = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, target_elements)))
            elif self.target_environment == values.IOS:
                all_views = WebDriverWait(driver, self.maximum_timeout).until(
                    expected_conditions.presence_of_all_elements_located((MobileBy.CLASS_NAME, target_elements)))
            self.index = 0
            if all_views:
                no_of_all_views = len(all_views)
                if no_of_all_views > 0:
                    self.project_log.info('Total {} - {} found on screen'.format(len(all_views), target_elements))
                    for view in all_views:
                        self.project_log.info('{}. {}, with value - {}'.format(self.index, view, view.text))
                        self.index += 1
                    return all_views
                else:
                    self.project_log.info('0 {} found on screen'.format(target_elements))

            return None

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                no_such_element_exception,
                sys.exc_info()[0]
            ))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                web_driver_exception,
                sys.exc_info()[0]
            ))

    def get_all_views_on_ios_screen(self, driver, target_elements):
        """
        Get list of all visible Views on ios screen

        Arguments:
            driver (webdriver): webdriver instance variable
            target_elements (webdriver element): elements locator

        Return:
            webdriver elements: List of Views
        """

        try:
            all_views = WebDriverWait(driver, self.maximum_timeout).until(
                expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, target_elements)))
            self.index = 0
            if all_views:
                no_of_all_views = len(all_views)
                if no_of_all_views > 0:
                    self.project_log.info('Total {} - {} found on screen'.format(len(all_views), target_elements))
                    for view in all_views:
                        self.project_log.info('{}. {}, with value - {}'.format(self.index, view, view.text))
                        self.index += 1

                    return all_views
                else:
                    self.project_log.info('0 {} found on screen'.format(target_elements))

            return None

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                no_such_element_exception,
                sys.exc_info()[0]
            ))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                web_driver_exception,
                sys.exc_info()[0]
            ))

    def get_all_views_on_screen_by_id(self, driver, target_elements):
        """
        Get list of Views on screen

        Arguments:
            driver (webdriver): webdriver instance variable
            target_elements (webdriver element): elements locator

        Return:
            webdriver elements: List of Views
        """

        try:
            if self.target_environment == values.ANDROID:
                all_views = driver.find_elements(MobileBy.ANDROID_UIAUTOMATOR,
                                                f'new UiSelector().resourceId("{target_elements}")')
            elif self.target_environment == values.IOS:
                all_views = driver.find_elements(MobileBy.ACCESSIBILITY_ID, target_elements)
            if all_views:
                self.project_log.info('Total {} - {} found on screen'.format(len(all_views), target_elements))
                for view in all_views:
                    self.project_log.info('{}. {}, with value - {}'.format(self.index, view, view.text))
                    self.index += 1
                return all_views
            else:
                self.project_log.error('0 {} found on screen'.format(target_elements))
                return None

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                no_such_element_exception,
                sys.exc_info()[0]
            ))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {}'.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                web_driver_exception,
                sys.exc_info()[0]
            ))

    def wait_for_element_visibility(self, driver, target_elements):
        """
        Block until the element visibility on screen, then returns True

        Arguments:
            driver (webdriver element): webdriver instance variable
            target_elements (str): specific selector of element

        Raises:
            TimeOut: The timeout is exceeded without the element successfully visible
        """
        element = None

        try:
            if self.target_environment == values.ANDROID:
                element = WebDriverWait(driver, self.medium_timeout).until(
                    expected_conditions.visibility_of_element_located((
                        By.ID,
                        target_elements
                    )))
            elif self.target_environment == values.IOS:
                element = WebDriverWait(driver, self.medium_timeout).until(
                    expected_conditions.visibility_of_element_located((
                        MobileBy.ACCESSIBILITY_ID,
                        target_elements
                    )))

            return element

        except NoSuchElementException as no_such_element_exception:
            self.project_log.error('{} - {} - {} - {} '.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                no_such_element_exception,
                sys.exc_info()[0]
            ))

        except WebDriverException as web_driver_exception:
            self.project_log.error('{} - {} - {} - {} '.format(
                values.ERROR_UTF_ELEMENT,
                target_elements,
                web_driver_exception,
                sys.exc_info()[0]
            ))

            return False

    def scroll_screen(self, driver, from_element, to_element):
        """
        Scroll from one element to other element on screen

        Arguments:
            driver (webdriver element): webdriver instance variable
            from_element (webdriver element): element from which scroll will start
            to_element (webdriver element): element where scroll will end
        """

        self.project_log.info('Scrolling screen.')
        driver.scroll(from_element, to_element)

    def scroll_from_element(self, driver, from_element):
        """
        Scroll from element

        Arguments:
            driver (webdriver element): webdriver instance variable
            from_element (webdriver element): element from which scroll will start
        """

        screen_width = driver.get_window_size()["width"]
        screen_height = driver.get_window_size()["height"]
        element_x_position = from_element.location['x']
        element_y_position = from_element.location['y']

        self.project_log.info('screen width {} - screen height {} - element_x {} - ''element_y {} '.format(
            screen_width,
            screen_height,
            element_x_position,
            element_y_position
        ))

        horizontal_start_point = int(element_x_position)
        vertical_start_point = int(element_y_position)
        horizontal_end_point = int(element_x_position)
        vertical_end_point = 0

        self.project_log.info('horizontal_start_point {} - vertical_start_point {} - horizontal_end_point {} '
                              '- vertical_end_point {} '.format(horizontal_start_point,
                                                                vertical_start_point,
                                                                horizontal_end_point,
                                                                vertical_end_point
                                                                ))

        driver.swipe(horizontal_start_point, vertical_start_point, horizontal_end_point, vertical_end_point, 500)

    def generate_random_credentials(self, length):
        """
        Generate random alphanumeric strings

        Arguments:
            length (int): length of string to generate

        Return:
            str: random string
        """

        combination = string.ascii_lowercase + string.digits
        return ''.join(random.choice(combination) for _ in range(length))

    def get_ios_all_static_text(self, driver):
        """
        Get all static text

        Returns:
            List of webdriver elements: static text elements
        """

        self.wait_for_element_visibility(driver, ios_elements.all_textviews)

        all_static_text_elements = self.get_all_views_on_ios_screen(
            driver,
            ios_elements.all_textviews
        )
        return all_static_text_elements

    def get_ios_all_editfields(self, driver):

        """
        Get all editfields elements

        Returns:
            List of webdriver elements: editfields elements
        """

        all_editfields_elements = self.get_all_views_on_ios_screen(
            driver,
            ios_elements.all_editfields
        )
        return all_editfields_elements

    def get_ios_all_buttons(self, driver):
        """
        Get all buttons elements

        Returns:
            List of webdriver elements: button elements
        """

        all_button_elements = self.get_all_views_on_ios_screen(
            driver,
            ios_elements.all_buttons
        )
        return all_button_elements

    def get_screen_heading_title(self, driver):

        """
        Get heading title elements

        Returns:
            Webdriver element: screen heading title element
        """

        heading_title = self.wait_and_get_element(
            driver,
            ios_elements.screen_heading_title
        )
        return heading_title

    def get_txt_toolbar_title(self, driver):
        """
        Get toolbar title

        Returns:
            element: toolbar title element
        """

        self.wait_for_element_visibility(
            driver,
            android_elements.txt_toolbar_title
        )

        toolbar_title = self.wait_and_get_element(
            driver,
            android_elements.txt_toolbar_title
        )
        return toolbar_title

    def get_navigation_bar_title(self, driver):
        """
        Get navigation bar

        Returns:
            element: navigation bar title element
        """

        self.wait_for_element_visibility(
            driver,
            ios_elements.navigation_bar_title
        )

        navigation_title = self.get_all_views_on_ios_screen(
            driver,
            ios_elements.navigation_bar_title
        )
        return navigation_title

    def get_back_button(self, driver):
        """
        Returns:
            element: back button element
        """

        self.wait_for_element_visibility(
            driver,
            android_elements.back_button_navigation
        )

        return self.wait_and_get_element(
            driver,
            android_elements.back_button_navigation
        )

    def get_child_element(self, parent_element, child_element_locator):
        """
        Returns:
            element: back button element
        """

        return parent_element.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                            f'new UiSelector().resourceId("{child_element_locator}")')

    def get_element_by_label_ios(self, driver, element_text):
        """
        Returns:
            element: text element
        """

        self.wait_for_element_visibility(
            driver,
            element_text
        )
        return driver.find_element(MobileBy.IOS_PREDICATE,
                                   f'label CONTAINS "{element_text}"')

    def get_elements_by_name_ios(self, driver, element_name):
        """
        Returns:
            element: name element
        """

        self.wait_for_element_visibility(
            driver,
            element_name
        )
        return driver.find_elements(MobileBy.IOS_PREDICATE,
                                   f'name CONTAINS "{element_name}"')

    def get_element_by_name_ios(self, driver, element_name):
        """
        Returns:
            element: name element
        """

        self.wait_for_element_visibility(
            driver,
            element_name
        )
        return driver.find_element(MobileBy.IOS_PREDICATE,
                                   f'name CONTAINS "{element_name}"')
