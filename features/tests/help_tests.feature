Feature: Tests for Help pages

  Scenario: User can select Help topic Promotions & Coupons
    Given Open Help page for Returns
    When Select Help topic Gift Cards
    Then Verify help GiftCard page opened

