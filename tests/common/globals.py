"""
   Module covers Android & iOS screens' global contents
"""

import yaml


class Globals:
    """
    Contains all global level contents, accessible in Pages & Tests
    """

    AUT_PACKAGE_NAME = 'org.openedx.app'

    def __init__(self):
        # Read user_preferences.yml and set globals accordingly
        self.setup_global_environment()

        # CAPABILITIES
        self.ios_device_name = 'iPhone 14'
        self.android_device_name = 'Android Phone'

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
