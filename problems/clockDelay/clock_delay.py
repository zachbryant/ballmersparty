import random

from hackgen import TestInputFormat, TestGenerator, Language


class ClockDelayInputFormat(TestInputFormat):
    """
    Input format of Clock Delay challenge.
    https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay
    """

    # difficulty levels with test file number
    # difficulty level is [0-9]
    __diff = [(5, 10), (10, 30), (50, 100), (100, 300), (100, 300),
              (300, 600), (600, 900), (800, 1000), (900, 1000), (950, 1000)]

    def inputs(self, difficult_level: int) -> None:
        q = random.randint(*self.__diff[difficult_level])  # number of test cases
        print(q)
        for n in range(q):
            # constraints for h1 m1 h2 m2 k
            h1 = random.randint(0, 23)
            m1 = random.randint(0, 60)
            h2 = random.randint(h1, 24)
            k = random.randint(h2 - h1 + 1 if h1 == h2 else h2 - h1, 24 - h1)
            m2 = random.randint(0, (m1 if h1 + k == h2 else 60))
            print(h1, m1, h2, m2)
            print(k)


# input format instance
input_format = ClockDelayInputFormat()

# input: #of test, input format, solution, name
test_generator = TestGenerator(10, input_format, Language.python('logic'), "ClockDelay")
test_generator.run()
