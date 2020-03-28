""""https://codeforces.com/problemset/problem/841/A?locale=en"""

"""method 1"""

n, k = map(int, input().split())
s = input()
c = [0] * 26
count_yes = 0
count_no = 0
for i in s:
    nomer = ord(i) - 97
    c[nomer] += 1
for j in range(len(c)):
    if c[j] <= k:
        count_yes += 1
    else:
        count_no += 1
if count_no > 0:
    print('NO')
else:
    print('YES')

"""method 2"""

balls, friends = map(int, input().split())
colors = input()
s = {}
count_yes = 0
count_no = 0
for i in colors:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1
for j in s:
    if s[j] <= friends:
        count_yes += 1
    else:
        count_no += 1
if count_no >= 1:
    print('NO')
else:
    print('YES')

