import random

from hackgen import TestInputFormat, TestGenerator, Language


class AlphabetRangoli(TestInputFormat):
    """
    Input format of Clock Delay challenge.
    https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay
    """

    # difficulty levels with test file number
    # difficulty level is [0-9]
    __diff = [(5, 10), (10, 30), (50, 100), (100, 300), (100, 300),
              (300, 600), (600, 900), (800, 1000), (900, 1000), (950, 1000)]

    def inputs(self, difficult_level: int) -> None:
        # constraints for h1 m1 h2 m2 k
        n = random.randint(0, 27)
        print(n)


# input format instance
input_format = AlphabetRangoli()

# input: #of test, input format, solution, name
test_generator = TestGenerator(10, input_format, Language.python('logic'), "AlphabetRangoli")
test_generator.run()
