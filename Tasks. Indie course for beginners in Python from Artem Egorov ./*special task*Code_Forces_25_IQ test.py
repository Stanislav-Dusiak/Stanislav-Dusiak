""""http://codeforces.com/problemset/problem/25/A"""

n = int(input())
a = list(map(int, input().split()))
even = []
odd = []
z = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
if len(even) > len(odd):
    z = odd
else:
    z = even
for i in range(len(a)):
    if a[i] == z[0]:
        print(i + 1)

