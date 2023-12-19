"""
   Module covers Android & iOS screens' global contents
"""

import sys
import string
import random
import enum
import os
import yaml

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.common import strings


class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """

    # Register
    # AUT_PACKAGE_NAME = 'org.edx.mobile'
    AUT_PACKAGE_NAME = 'org.openedx.app'
    # Android Activities Names
    LAUNCH_ACTIVITY_NAME1 = '.view.LaunchActivity'
    SPLASH_ACTIVITY_NAME = '.view.SplashActivity'
    NEW_LOGISTRATION_ACTIVITY_NAME = '.view.DiscoveryLaunchActivity'
    LOGIN_ACTIVITY_NAME = '.view.login.LoginActivity'

    def __init__(self):
        # self.whats_new_enable = True

        # Read user_preferences.yml and set globals accordingly
        self.setup_global_environment()

        # CAPABILITIES
        self.ios_device_name = 'iPhone 14'
        self.android_device_name = 'Android Phone'
        self.login_wrong_user_name = 'wrong username'

    def setup_global_environment(self):
        """
        set environment and read user_preferences for local run
        """

        with open("./tests/user_preferences.yml") as user_file:
            user_preferences = yaml.safe_load(user_file)
            user_file.close()

        self.target_environment = user_preferences.get('Settings').get('target_environment')
        self.server_url = user_preferences.get('Settings').get('appium_server')
        self.android_platform_version = user_preferences.get('Settings').get('android_platform_version')
        self.ios_platform_version = user_preferences.get('Settings').get('ios_platform_version')
        self.aut_current_path = user_preferences.get('Settings').get('aut_current_path')
        self.aut_latest_path = user_preferences.get('Settings').get('aut_latest_path')
        self.login_user_name = user_preferences.get('User').get('login_user_name')
        self.login_password = user_preferences.get('User').get('login_password')
