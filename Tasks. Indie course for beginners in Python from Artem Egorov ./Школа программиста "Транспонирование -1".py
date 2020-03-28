""""https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=120&id_problem=742"""

a = []
z = []
n = int(input())
for i in range(n):
    z.append([0] * n)
for k in range(n):
    a.append(list(map(int, input().split())))
for i in range(len(a)):
    for j in range(len(a)):
        z[i][j] = a[j][i]
for i in z:
    print(*i)

