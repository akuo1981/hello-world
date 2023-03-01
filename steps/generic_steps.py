from behave import step
#from selenium import webdriver
from appium import webdriver
from selenium.webdriver.common.keys import Keys

@step('I open the app')
def i_open_the_app(context):
    if context.platform == "android":
        #to define android capability
        dc = {
          "appium:device": "Android12",
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
    #assert context.driver.currentActivity == dc['appActivity'], 'App is not launched'
    print("")


