# Created by lw1337 at 8/3/24
Feature: Target login page tests

  Scenario: user sees error msg for login
    Given Open target main page
    When Click sign in
    And From right side click sign in
    When Enters wrong email
    And Enters wrong password
    And Enter sign in
    Then Verifies that error message is shown
