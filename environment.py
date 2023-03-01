from utils.logger import setup_custom_logger
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def before_all(context):
    context.logger = setup_custom_logger("automation-log")
    context.app_url = context.config.userdata.get("app_url")
    context.platform = context.config.userdata.get("platform")

    context.logger.info("*" * 60)
    context.logger.info("Starting execution of automation")
    context.logger.info(f"Running on: {context.platform}")
    context.logger.info(f"APP URL: {context.app_url}")
    context.logger.info("*" * 60)

''''
def before_feature(context, feature):
    if context.platform == "android":
        #to define android capability
        dc = {
          "appium:device": "Pixel6Pro_Android13",
          "platformName": "Android",
          "appium:app": "/Users/amandakuo/Desktop/Mobile/applicant-app/bin/applicant-automation.apk",
          "appium:automationName": "UiAutomator2",
          "autoAcceptAlerts": True,
          "fullReset": True
        }
    elif context.platform == "ios":
        # to define ios capability
        dc = {
          "appium:deviceName": "iPhone 13",
          "platformName": "iOS",
          "appium:app": "/Users/amandakuo/Desktop/Mobile/applicant-app/bin/applicant-automation.app",
          "appium:platformVersion": "16.2",
          "appium:automationName": "XCUITest",
          "appium:autoAcceptAlerts": True
        }
    else:
        raise Exception("Not a valid platform provided.")

    context.driver = webdriver.Remote(command_executor=context.app_url, desired_capabilities=dc)
    assert context.driver.current_activity == dc['appActivity'], 'App is not launched'
    print("")

'''