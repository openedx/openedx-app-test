# openedx-app-test
This repository serves as a collection of automated end-to-end test cases for the Open edX mobile applications designed for both Android and iOS platforms.
It aims to ensure the reliability and functionality of the Open edX mobile apps by automating the testing process and providing a comprehensive suite of test cases.

## Installations
- [node](https://nodejs.org/en/)
- [appium](http://appium.io/)
- [pytest](https://docs.pytest.org/en/latest/getting-started.html)
- [pytest-html](https://pypi.python.org/pypi/pytest-html/)
- [Appium-Python-Client](https://pypi.org/project/Appium-Python-Client/)
- [PyYAML](https://pypi.org/project/PyYAML/)
- [allure-pytest](https://pypi.org/project/allure-pytest/)

- Recommended to install requirements other than appium and node via pip
  -     pip install -r requirements.txt

###### iOS(Simulator)
 - Xcode with command line tools

###### Android(Phone/Tablet/Simulator)
 - [Android SDK](https://developer.android.com/studio/index.html)

 Don't forget to set environment variables for adb, platform-tools etc.*

#### Setup
- connect/start Android/iOS Device/Simulator
- Browse tests/ directory
- Rename 'user_preferences_sample.yml' to 'user_preferences.yml' and set the following values,

    - set `Android' to execute test cases on Android or 'iOS' to execute on iOS

          target_environment: Android

    - set above selected target_environment's OS Version(of specific running device/simulator) like below

          platform_version: iOS device/simulator version | Android device/emulator version

    - device name is only useful for iOS simulator, in case of multiple connected real devices use udid

          device_name: 'iPhone 15'
        or leave empty string

    - add reset option true/false
      -     full_reset: true

    - add path to apk/ipa file
      -     app_path: "path/to/file"

    - set valid credentials to login

          login_user_name: username

          login_password: password

- install edx(iOS/Android) app on specific device/simulator

#### Run
- Check out/download the source code, browse its directory

        git clone https://github.com/openedx/openedx-app-test

- `pytest` - to run all test cases

- `pytest tests/android/tests/ ` - to run all android test screens

- `pytest tests/ios/tests/` - to run all ios test screens

- `pytest <test case name>` to run specific test case

- `pytest <test case name>` to run specific test case and create html report at end of execution


### To run test cases on BrowserStack

### Prerequisites
- [Python3](https://www.python.org/downloads/)
- [Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)

## Linting

Follow the link to [improve the quality of code](./docs/linting.md)

### Integration Steps
- Complete the following steps to integrate your Python test suite using BrowserStack SDK.

### Set BrowserStack Credentials
- `export BROWSERSTACK_USERNAME="************"`
- `export BROWSERSTACK_ACCESS_KEY="************"`

Saving your BrowserStack credentials as environment variables makes it simple to run your test suite from your local or CI environment.

### Install BrowserStack Python SDK
- `python3 -m pip install browserstack-sdk`
- `browserstack-sdk setup --username "**************" --key "**************"`

Execute the following commands to install BrowserStack Python SDK for plug-and-play integration of your test suite with BrowserStack.

### Setup
- Update `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` in `browserstack.yml` file

- Update device name and version for android and ios in `browserstack.yml` file
  - platformName: `Android`/`iOS`
  - deviceName: `Google Pixel 7 pro`/`iPhone 14 pro max`
  - platformVersion: `13.0`/`16`

- Rename `user_preferences_sample.yml` to `user_preferences.yml` and set the following values:

    - set `target_environment` to `Android` or `iOS`
      - target_environment: Android

    - set valid credentials to login
      - login_user_name: username
      - login_password: password

- If you want to run on any other device/OS for android/iOS you can visit this link to see all available devices in browserstack (https://www.browserstack.com/list-of-browsers-and-platforms/automate)

- To run parallel execution on multiple devices, more platform details can be given with their device name and platform version
### Run

- `PLATFORM_NAME=Android browserstack-sdk pytest -v tests/android/tests/` to run all android
test screens

- `PLATFORM_NAME=iOS browserstack-sdk pytest -v tests/ios/tests/` to run all ios
test screens
