import time
from behave import step, use_step_matcher
from pageobjects.signup_page import SignUpPage

#regular expression instead of text for more powerful definition
#EX: when passing first name, last name, phone number, email from feature to steps
use_step_matcher('re')


@step('I click on "Create an account"')
def i_click_on_create_an_account(context):
    page = SignUpPage(context)
    if context.platform == "android":
        page.signup_button_and.click()
    elif context.platform == "ios":
        page.signup_button.click()
    print("")

@step('I should see the "First name" field')
def i_should_see_the_first_name_field(context):
    page = SignUpPage(context)
    time.sleep(3)
    if context.platform == "android":
        assert page.first_name_and, "First name is not displayed"
    elif context.platform == "ios":
        #assert page.first_name.is_displayed(), "First name is not displayed"
        assert page.first_name, "First name is not displayed"

@step('I add the first name as (.*)')
def i_add_the_first_name(context, first_name):
    page = SignUpPage(context)
    time.sleep(3)
    if context.platform == "android":
        page.first_name_and.send_keys(first_name)
    elif context.platform == "ios":
        page.first_name.send_keys(first_name)


@step('I add the last name as (.*)')
def i_add_the_last_name(context, last_name):
    page = SignUpPage(context)
    time.sleep(3)
    if context.platform == "android":
        page.last_name_and.send_keys(last_name)
    elif context.platform == "ios":
        page.last_name.send_keys(last_name)


@step('I add the phone number as (.*)')
def i_add_the_phone_number(context, phone):
    page = SignUpPage(context)
    if context.platform == "android":
        page.phone_number_and.send_keys(phone)
    elif context.platform == "ios":
        page.phone_number.send_keys(phone)


@step('I add the email address as (.*)')
def i_add_the_email_address(context, email):
    page = SignUpPage(context)
    time.sleep(3)
    if context.platform == "android":
        page.email_and.send_keys(email)
    elif context.platform == "ios":
        page.email.send_keys(email)


@step('I click on the Next button')
def i_click_on_the_next_button(context):
    page = SignUpPage(context)
    if context.platform == "android":
        page.next_button_and.click()
    elif context.platform == "ios":
        page.next_button.click()


@step('I should see the "Enter verification code" field')
def i_should_see_the_enter_verification_code_field(context):
    page = SignUpPage(context)
    time.sleep(3)
    if context.platform == "android":
        assert page.verification_code_and, "You are not on 'Enter verification code' screen"
    elif context.platform == "ios":
        assert page.verification_code, "You are not on 'Enter verification code' screen"