""""Valera runs a 24/7 fast food cafe. He magically learned that next day n
people will visit his cafe. For each person we know the arrival time: the i-th
person comes exactly at hi hours mi minutes. The cafe spends less than a minute
to serve each client, but if a client comes in and sees that there is no free
cash, than he doesn't want to wait and leaves the cafe immediately. Valera is
very greedy, so he wants to serve all n customers next day
(and get more profit). However, for that he needs to ensure that at each
moment of time the number of working cashes is no less than the number of
clients in the cafe. Help Valera count the minimum number of cashes to work at
his cafe next day, so that they can serve all visitors.
Input
The first line contains a single integer n (1 ≤ n ≤ 105), that is the number
of cafe visitors.
Each of the following n lines has two space-separated integers hi and
mi (0 ≤ hi ≤ 23; 0 ≤ mi ≤ 59), representing the time when the i-th person comes
into the cafe.
Note that the time is given in the chronological order. All time is given
within one 24-hour period.
Output
Print a single integer — the minimum number of cashes, needed to serve all
clients next day."""

n = int(input())
times = [0] * (24 * 60)
for i in range(n):
    h, m = map(int, input().split())
    t = (h * 60) + m
    times[t] += 1

print(max(times))
