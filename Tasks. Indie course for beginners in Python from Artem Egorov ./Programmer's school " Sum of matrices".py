""""https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=120&id_problem=746"""

n, m = map(int, input().split())
a = []
b = []
z = []
s = 0
for k in range(n):
    a.append(list(map(int, input().split())))
o = input()
for k1 in range(n):
    b.append(list(map(int, input().split())))
for i in range(n):
    print()
    for j in range(m):
        s += a[i][j] + b[i][j]
        print(s, end=' ')
        s = 0

