Feature: Tests for main page UI

  Scenario: User can open shop page
    Given Open cure skin main page
    And Open shop all
#    Then Verify user can see 19 products for cure


   Scenario: User can search shop all
     Given Open cure skin main page
     When User click search button
     Then Select shop all to open page

