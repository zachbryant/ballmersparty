# Clock Delay

Vernon is a working man. He needs to attend a conference, and so he has to leave his home at exactly **$h_1$:$m_1$**, denoting the time in hours and minutes in a 24-hour clock. The moment he leaves, his home clock displays the correct time, **$h_1$:$m_1$**.

He returns home after exactly **k** hours. It is guaranteed that he returns on the same day, hence **$h_1 + k < 24$**. However, the home clock shows **$h_2$:$m_2$**, which may or may not be the correct time. He suspects that the home clock is lagging, and he wishes to know the duration of time in minutes by which his home clock has been lagging.
It is guaranteed that the actual time is either the same as, or after the time displayed by the clock.
Complete the function lagDuration which takes in five integers **$h_1, m_1, h_2, m_2, k$** and returns an integer denoting the duration of time in minutes by which the clock has been lagging.

**Input format**
The first line contains **q**, the number of queries.
Each query is described by two lines. The first line contains four space-separated integers **$h_1, m_1, h_2, m_2$**. The second line contains a single integer **k**.

**Constraints:**
- $1 \leq q \leq 1000$
- $0 \leq h_1 < 23$
- $0 \leq h_2 \leq 24$
- $0 \leq m_1,m_2 \leq 60$
- $1 \leq k$
- $h_1 + k < 24$
- it is guaranteed that **$h_1$:$m_1$** is strictly before **$h_2$:$m_2$**

**Output format:**
For each query, print a single line containing a single integer indicating the duration of time in minutes by which the clock has been lagging.

**Sample input:**
```
6
12 0 12 58
1
10 12 10 17
2
11 40 15 33
6
18 13 19 25
5
14 27 21 1
9
16 40 23 40
7
```
**Sample Output**
```
2
115
127
228
146
0
```

**Explanation**
In the first query, the home clock initially displays **12:00**. He returns home at **13:00**, exactly **1** hour after he leaves. But at this point, the clock displays **12:58**. Hence, the clock must be lagging by **2** minutes.

In the second query, the home clock initially displays **10:12**. He returns home at **12:12**, exactly **2** hours after he leaves. But at this point, the clock displays **10:17**. Hence, the clock must be lagging by **115** minutes.
