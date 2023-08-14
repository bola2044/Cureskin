Feature: Tests for main page UI
@smoke
  Scenario: User can open shop page
    Given Open cure skin main page
    And Open shop all
    Then Verify user can see 19 products for cure

@smoke
   Scenario: User can search shop all
     Given Open cure skin main page
     When User click search button
     Then Select shop all to open page


  Scenario: User can open https://cureskin.com/ and see UI components
    Given Open cure skin page
    Then User can see UI components

  Scenario: User can download app and correct page opens
      Given open cure skin page
      And Click on download app button
      Then verify correct page opens


  Scenario: User can click on "About Us" in the header and correct page (https://cureskin.com/about-cureskin/) opens
    Given Open cure skin page
    Then User can click on About us
    And Verify about us page opens About Us

   Scenario: User can click on "Testimonials" in the header and correct page (https://cureskin.com/testimonials/) opens
     Given Open cure skin page
     Then User can click on Testimonials
     And Verify correct page opens Testimonials page