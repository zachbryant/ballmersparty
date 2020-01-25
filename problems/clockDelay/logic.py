# problem link:
#https://www.hackerrank.com/contests/hourrank-28/challenges/clock-delay/problem
#

q = int(input())

for i in range(q):
    h1, m1, h2, m2 = map(int, raw_input().split())
    k = int(input())
    delay = (h1 + k - h2) * 60 + m1 - m2
    print(delay)
