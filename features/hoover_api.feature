Feature: Verify correctness of final robotic hoover position and number of patches of dirt cleaned using API

@smoke
Scenario: Verify robotic hoover final position and patches cleaned (happy-path)
    Given the room dimensions, dirt patches co-ordinates, initial hoover position and driving instructions
    When we execute navigate the imaginary robotic hoover service
    Then we get the final robotic hoover position and number of patches cleaned
    And  status code of response should be 200


@regression
Scenario: Verify robotic hoover final position and patches cleaned (negative testing)
    Given the room dimensions, dirt patches co-ordinates, initial hoover position and driving instructions
    When we execute navigate the imaginary robotic hoover service
    Then we get the final robotic hoover position and number of patches cleaned
    And  status code of response should be 201


@smoke
Scenario: Verify robotic hoover final position and patches cleaned (positive testing)
    Given the room dimensions, dirt patches co-ordinates, initial hoover position with incorrect endpoint
    When we execute navigate the imaginary robotic hoover service
    Then status code of response should be 404