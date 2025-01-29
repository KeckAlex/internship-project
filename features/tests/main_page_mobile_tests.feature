Feature: Main Page Mobile tests

  Scenario: User can add and publish company on the mobile web
    Given Open sign in page
    And Verify Sign in page opened
    When Sign in to account
    Then On the bottom menu click on Events btn
    And Verify the proper Events calendar page opens
    And Click on “Companies” btn
    And Verify the right market-companies page opens
    And Click on “Add Company” button
    And Verify the right for-the-agency page opens
    And Verify the buttons "Publish my company" are clickable
