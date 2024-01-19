Feature: Search Content

  Scenario: Searching for 'furry rabbits'
    Given A client of the API
    When A search for pages containing "furry rabbits" is executed
    Then A page with the "title" "Sesame Street" is found