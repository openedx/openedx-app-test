# openedx-app-test
This repository serves as a collection of automated end-to-end test cases for the Open edX mobile applications designed for both Android and iOS platforms.
It aims to ensure the reliability and functionality of the Open edX mobile apps by automating the testing process and providing a comprehensive suite of test cases.

## Installations
- [node](https://nodejs.org/en/)
- [appium](https://appium.io/docs/en/latest/quickstart/)
- [Java jdk](https://www.oracle.com/europe/java/technologies/downloads/)
- Note: Java jdk is necessary if you want to automate android apps irrespective of test language

- Recommended to install requirements other than the above via the script
  -     source scripts/venv.sh
- This will install all the requirements present in the requirements file as well as the pre-commit hooks. For more info on pre-commit hooks you can check out the doc under linting heading.
###### iOS(Simulator)
 - Xcode with command line tools or simple command line tools

###### Android(Phone/Tablet/Simulator)
 - [Android SDK](https://developer.android.com/tools)
 - Install platform-tools and build-tools from the same link mentioned above

 Don't forget to set environment variables for adb, platform-tools etc.*

#### Setup
- connect/start Android/iOS Device/Simulator
- Browse tests/ directory
- Rename 'user_preferences_sample.yml' to 'user_preferences.yml' and set the following values,
- Update the yml file as per instruction in the yml file.
- install edx(iOS/Android) app on specific device/simulator or simple pass app path in yml

#### Run
- Check out/download the source code, browse its directory

        git clone https://github.com/openedx/openedx-app-test

- `pytest` - to run all test cases

- `pytest tests/android/tests/ ` - to run all android test screens

- `pytest tests/ios/tests/` - to run all ios test screens

- `pytest <test case name>` to run specific test case

- `pytest <test case name>` to run specific test case and create html report at end of execution

- `pytest -m <marker>` to run tests related to a specific marker

New markers can be added to files and should be listed inside the pytest.ini file.

### To run test cases on BrowserStack

### Prerequisites
- [Python3](https://www.python.org/downloads/)
- [Pip3](https://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3)

## Linting

Follow the link to [improve the quality of code](./docs/linting.md)

### Integration Steps
- Complete the following steps to integrate your Python test suite using BrowserStack SDK.

### Set BrowserStack Credentials and other env variables
- `export BROWSERSTACK_USERNAME="************"`
- `export BROWSERSTACK_ACCESS_KEY="************"`
- `export PLATFORM_NAME=Android/iOS`

Saving your BrowserStack credentials as environment variables makes it simple to run your test suite from your local or CI environment.
PLATFORM_NAME is a custom variable used to make test run unique and identifiable.

### Install BrowserStack Python SDK
It is present in the requirements.txt file and is installed already in your env

### Setup
- Add following environment variables
  - `BROWSERSTACK_USERNAME`
  - `BROWSERSTACK_ACCESS_KEY`
  - `PLATFORM_NAME`

- vales for `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` can be found in your browserstack profile.

- Update device name and version for android and ios in `browserstack.yml` file. A complete list of available devices can be found on https://www.browserstack.com/list-of-browsers-and-platforms/automate
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

- `browserstack-sdk pytest tests/android/tests/ --env browserstack` to run all android
test screens

- `browserstack-sdk pytest tests/ios/tests/ --env browserstack` to run all ios
test screens

- `browserstack-sdk pytest -m ANDROID_SMOKE --env browserstack` to run all tests with smoke marker

You can also use any other way of selecting tests which are available under pytest

### Allure Report
By default each pytest command execution will clean out the allure-results folder as specified in the `pytest.ini` file.
In order to create a report on your local machine use the command
- `allure serve` this will generate allure report and serve it at local endpoint provided in the terminal where the command is run
To create a single file allure report for sharing purpose use the following command
- `allure generate allure-results --clean --single-file -o allure-report ` This will generate a single html file under allure-report folder as specified in the command with `-o` option.
