""""https://codeforces.com/problemset/problem/141/A?locale=en"""

a = input()
b = input()
n = input()
c = a + b
z = [0] * 26
v = [0] * 26
count_yes = 0
count_no = 0
for i in c:
    nomer = ord(i) - 65
    z[nomer] += 1
for j in n:
    nomer = ord(j) - 65
    v[nomer] += 1
for g in range(len(z)):
    if z[g] == v[g]:
        count_yes += 1
    else:
        count_no += 1
if count_no > 0:
    print('NO')
else:
    print('YES')

