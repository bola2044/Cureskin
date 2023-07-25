Feature: Search results UI is correct
@smoke
Scenario: Verify first results have name, image and price
    Given Open cure skin main page
    And Open shop all
    Then Verify first results have name
    And Verify first results have an image
    And Verify first results have a price