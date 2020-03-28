""""https://codeforces.com/contest/263/problem/A"""

a = []
z = 0
v = 0
for k in range(5):
    a.append(list(map(int, input().split())))
for i in a:
    for j in i:
        if j == 1:
            z = a.index(i) + 1
            v = i.index(j) + 1
print(abs(3 - z) + abs(3 - v))

