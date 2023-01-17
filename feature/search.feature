Feature: Some feature description

  #@wip
  Scenario: Search Instawork on Google
    Given I go to Google
    When I search for "Instawork"
    Then I should see "Instawork: Work Local Shifts 4+ - App Store"

  @wip
  Scenario: Search Instawork on Google and find its position
    Given I go to Google
    When I search for "Instawork"
    Then I should see "Instawork: Work Local Shifts 4+ - App Store" and its position
