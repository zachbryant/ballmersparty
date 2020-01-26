'''
Title     : Find Angle MBC
Subdomain : Math
Domain    : Python
Author    : Ahmedur Rahman Shovon
Created   : 15 July 2016
Problem   : https://www.hackerrank.com/challenges/find-angle/problem
'''

import random

from hackgen import TestInputFormat, TestGenerator, Language


class findAngleMBC(TestInputFormat):
    """
    Input format of Clock Delay challenge.
    https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay
    """

    # difficulty levels with test file number
    # difficulty level is [0-9]
    __diff = [(5, 10), (10, 30), (50, 100), (100, 300), (100, 300),
              (300, 600), (600, 900), (800, 1000), (900, 1000), (950, 1000)]

    def inputs(self, difficult_level: int) -> None:
        #q = random.randint(*self.__diff[difficult_level])  # number of test cases
        #print(q)
        #for n in range(q):
            # constraints for h1 m1 h2 m2 k
            AB = random.randint(0, 100)
            BC = random.randint(0, 100)
            print(AB)
            print(BC)


# input format instance
input_format = findAngleMBC()

# input: #of test, input format, solution, name
test_generator = TestGenerator(10, input_format, Language.python('logic'), "FindAngleMBC")
test_generator.run()

