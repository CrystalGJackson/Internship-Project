Feature: Test Scenarios for Search functionality
#
##  Scenario: User can search for a product
##    Given Open Google page
##    When Input Car into search field
##    And Click on search icon
##    Then Product results for Car are shown
#
#    Scenario: User can click on verifications settings option and verify the right page opens
#      Given Open the main page
#      When Log in to the page
#      Then Click on "settings" at the left side menu
#      Then Click on the verification option
#      Then Verify the right page opens
#      Then Verify "upload image" and "Next step" buttons are available


  Scenario: User can click on verifications settings option and verify the right page opens
      Given Open the main page
      When Log in to the page
      Then Click on "market offers"
      Then Click on "menu" at the top left
      Then Click on the verification option
      Then Verify the right page opens
      Then Verify "upload image" and "Next step" buttons are available