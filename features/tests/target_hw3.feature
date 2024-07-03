Feature: Scenario for target homework

  Scenario: User sees empty cart
    Given Open Target
    When Click on Cart
    Then Cart is Empty


  Scenario: User Checks for sign in
    Given Open Target
    When Click Sign In
    Given Click Sign in from right bar
    Then Verify sign in form is there


