Feature: Simple FizzBuzz
    Implement a simple version of the FizzBuzz game

    Scenario: FizzBuzz of 5
        Given the number 5
        When I call fizzbuzz
        Then I see the output Buzz

    Scenario: Fizzbuzz [just enough]
        Given the number <input>
        When I call FizzBuzz
        Then I see the output <output>

        Examples:
        | input | output   |
        | 1     | 1        |
        | 3     | Fizz     |
        | 5     | Buzz     |
        | 6     | Fizz     |
        | 10    | Buzz     |
        | 15    | FizzBuzz |