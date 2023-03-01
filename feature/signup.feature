Feature: Test Signup Functionality

  @wip
  Scenario: Verify the user is able to sign up
    Given I open the app
    When I click on "Create an account"
    Then I should see the "First name" field
    When I add the first name as Amanda2
    And I add the last name as Kuo
    And I add the phone number as (604) 686-9434
    And I add the email address as random2@random2.com
    And I click on the Next button
    Then I should see the "Enter verification code" field

