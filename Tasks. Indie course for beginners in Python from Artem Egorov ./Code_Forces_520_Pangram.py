""""http://codeforces.com/problemset/problem/520/A"""

"""method 1"""

n = int(input())
z = input()
a = z.lower()
if len(set(a)) == 26:
    print('YES')
else:
    print('NO')

"""method 2"""

n = int(input())
a = input()
d = a.lower()
f = 'abcdefghijklmnopqrstuvwxyz'
z = len(d)
y = []
for i in range(z):
    if d[i] in f and d[i] not in y:
        y.append(d[i])
if len(y) >= 26:
    print('YES')
else:
    print('NO')

