""""https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=120&id_problem=744"""

a = []
z = []
n, m = map(int, input().split())
for k in range(n):
    z.append([0] * m)
for k in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        z[i][j] = a[i][m - 1 - j]
for i in z:
    print(*i)

