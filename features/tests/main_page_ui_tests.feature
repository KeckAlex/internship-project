Feature: Main Page UI tests

  Scenario: User can open market tab and add company option
    Given Open sign in page
    And Verify Sign in page opened
    When Sign in to account
    Then At the left side menu click on Market
    And Verify the right market-companies page opens
    And Click on “Add Company” button
    And Verify the right for-the-agency page opens
    And Verify the btn "Publish my company" is clickable