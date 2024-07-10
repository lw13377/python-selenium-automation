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


   #  HW 4
  Scenario: Checking all 10 links
      Given Open Circle Target Page
      Then Verify 10 Links


  Scenario: Verify adding items to cart
    Given Open Target
    When search for tea
    Then find results
    Then add tea to the cart
    And confirm add item to cart
    Then continue shopping
    And clear search
    When search for coffee
    Then find results
    Then add coffee to the cart
    And confirm add item to cart
    Then checkout cart

