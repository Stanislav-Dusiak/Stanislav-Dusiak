""""https://codeforces.com/contest/122/problem/A"""

n = int(input())
z = n
e = 0
a = []
while z != 1:
    d = str(z)
    for i in set(d):
        if i != '4' and i != '7':
            a.append(i)
    if len(a) == 0:
        a = []
        if n % z == 0:
            print('YES')
            break
        else:
            z -= 1
            a = []
    else:
        z -= 1
        a = []
if z == 1:
    print('NO')

