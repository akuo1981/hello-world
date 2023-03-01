from appium.webdriver.common.appiumby import AppiumBy
from webdriver_manager.core import driver
from behave import step, use_step_matcher

from pageobjects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):

    #constant variables are in upper case

    #IOS
    SIGNUP_BUTTON = (By.ID, 'intro-screen/sign-up-button')

    FIRST_NAME = (By.ID, 'signup-phone-screen/first-name-input')
    LAST_NAME = (By.ID, 'signup-phone-screen/last-name-input')
    PHONE_NUM = (By.ID, 'signup-phone-screen/phone-number-input')
    EMAIL = (By.ID, 'signup-phone-screen/email-address-input')
    NEXT = (By.ID, 'signup-phone-navbar/next-button')

    VERIFICATION_CODE = (By.ID, 'signup-verify-screen/verification-code-input')

    #Android
    SIGNUP_BUTTON_AND = (By.XPATH, '//android.view.ViewGroup[@content-desc="intro-screen/sign-up-button"]')
    #SIGNUP_BUTTON_AND = (By.ID, 'intro-screen/sign-up-button')
    #SIGNUP_BUTTON_AND = "intro-screen/sign-up-button"
    #SIGNUP_BUTTON_AND = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="intro-screen/sign-up-button")
    #SIGNUP_BUTTON_AND = driver.find_element_by_accessibility_id("intro-screen/sign-up-button")
    #SIGNUP_BUTTON_AND = webdriver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="intro-screen/sign-up-button")
    #SIGNUP_BUTTON_AND = (By.ACCESSIBILITY_ID, 'intro-screen/sign-up-button')

    FIRST_NAME_AND = (By.XPATH, '//android.widget.EditText[@content-desc="signup-phone-screen/first-name-input"]')
    LAST_NAME_AND = (By.XPATH, '//android.widget.EditText[@content-desc="signup-phone-screen/last-name-input"]')
    PHONE_NUM_AND = (By.XPATH, '//android.widget.EditText[@content-desc="signup-phone-screen/phone-number-input"]')
    EMAIL_AND = (By.XPATH, '//android.widget.EditText[@content-desc="signup-phone-screen/email-address-input"]')
    NEXT_AND = (By.XPATH, '//android.view.ViewGroup[@content-desc="signup-phone-navbar/next-button"]/android.widget.TextView')

    #VERIFICATION_CODE_AND = (By.XPATH, '//android.view.ViewGroup[@content-desc="signup-verify-screen/verification-code-input"]/android.view.ViewGroup')
    #VERIFICATION_CODE_AND = (By.XPATH, '//android.view.ViewGroup[@content-desc="signup-verify-screen/verification-code-input"]')
    VERIFICATION_CODE_AND = (By.XPATH, '//android.widget.EditText[@content-desc="signup-verify-screen/verification-code-input"]')

    # iOS Functions
    @property
    def signup_button(self):
            return self.driver.find_element(*self.SIGNUP_BUTTON)

    @property
    def first_name(self):
        return self.driver.find_element(*self.FIRST_NAME)

    @property
    def last_name(self):
        return self.driver.find_element(*self.LAST_NAME)

    @property
    def phone_number(self):
        return self.driver.find_element(*self.PHONE_NUM)

    @property
    def email(self):
        return self.driver.find_element(*self.EMAIL)

    @property
    def next_button(self):
        return self.driver.find_element(*self.NEXT)

    @property
    def verification_code(self):
        return self.driver.find_element(*self.VERIFICATION_CODE)

    #Android Functions
    @property
    def signup_button_and(self):
        return self.driver.find_element(*self.SIGNUP_BUTTON_AND)

    @property
    def first_name_and(self):
        return self.driver.find_element(*self.FIRST_NAME_AND)

    @property
    def last_name_and(self):
        return self.driver.find_element(*self.LAST_NAME_AND)

    @property
    def phone_number_and(self):
        return self.driver.find_element(*self.PHONE_NUM_AND)

    @property
    def email_and(self):
        return self.driver.find_element(*self.EMAIL_AND)

    @property
    def next_button_and(self):
        return self.driver.find_element(*self.NEXT_AND)

    @property
    def verification_code_and(self):
        return self.driver.find_element(*self.VERIFICATION_CODE_AND)

