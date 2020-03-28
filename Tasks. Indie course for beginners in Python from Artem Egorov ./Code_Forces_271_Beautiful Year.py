""""https://codeforces.com/contest/271/problem/A"""

n = int(input())
a = []
b = []
z = n + 1
k = set(b)
for i in str(n):
    a.append(i)
while len(a) != len(k):
    for j in str(z):
        b.append(j)
    z += 1
    k = set(b)
    b = []
print(z - 1)
