Feature: Verifying User registration

  Scenario: Registration with valid data
    Given user is on registration page
    When  user enters user name
    And   user enters password
    And   user enters email id
    And   user click on signup
    Then  user should be registered successfully


  Scenario: Registration with duplicate data
    Given user is on registration page
    When  user enters duplicate user name
    And   user enters password
    And   user enters email id
    And   user click on signup
    Then  user should be registered successfully