Feature: Search results UI is correct

  Scenario: Verify first results have name, image and price
    Given Open cure skin main page
    And Open shop all
    Then Verify first results have name,image and price