""""https://codeforces.com/contest/4/problem/C"""

n = int(input())
b = {}
c = 0
for key in range(n):
    a = input()
    if a not in b.keys():
        b[a] = 0
        print('OK')
    else:
        b[a] += 1
        print(a + str(b[a]))

