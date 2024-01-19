Feature: Pages

Scenario: Retrieving details for 'Sesame Street'
    Given The result for "furry rabbits" search contains "Sesame Street"
    When The page details for "Sesame Street" are requested
    Then It has a latest timestamp > "2023-08-17"