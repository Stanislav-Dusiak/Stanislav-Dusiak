""""https://codeforces.com/problemset/problem/577/A"""

n, x = map(int, input().split())
a = []
b = []
count = 0
for i in range(1, n + 1):
    if x % i == 0 and (x / i) <= n:
        count += 1.
print(int(count))

