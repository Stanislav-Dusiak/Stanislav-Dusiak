""""https://codeforces.com/problemset/problem/509/A"""

n = int(input())
tri = []
a =[]
for t in range(n):
    tri.append([0] * n)
for t in range(1):
    for t1 in range(n):
        tri[t][t1] = 1
for t2 in range(n):
    for t3 in range(1):
        tri[t2][t3] = 1
for i in range(1, n):
    for j in range(1, n):
        tri[i][j] = tri[i - 1][j] + tri[i][j - 1]
        a.append(tri[i][j])
if n == 1:
    print(1)
else:
    print(max(a))

