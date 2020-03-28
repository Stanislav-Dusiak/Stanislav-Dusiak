""""https://codeforces.com/problemset/problem/1015/A"""

n, k = map(int, input().split())
h = list(range(1, k + 1))
c = []
z = []
for i in (list(range(n))):
    a = list(map(int, input().split()))
    x = 1
    for j in range(len(h)):
        if a[0] <= x <= a[1]:
            c.append(x)
            x += 1
        else:
            x += 1
for f in range(len(h)):
    if h[f] not in c:
        z.append(h[f])
print(len(z))
print(*z)

