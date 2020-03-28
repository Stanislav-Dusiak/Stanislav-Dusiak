""""https://codeforces.com/contest/405/problem/A"""

"""method 1"""

n = int(input())
a = list(map(int, input().split()))
c = [0] * (max(a) + 1)
for i in a:
    c[i] += 1
for j in range(len(c)):
    if c[j] > 0:
        print((str(j) + ' ') * c[j], end='')

"""method 2"""

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(*a)

