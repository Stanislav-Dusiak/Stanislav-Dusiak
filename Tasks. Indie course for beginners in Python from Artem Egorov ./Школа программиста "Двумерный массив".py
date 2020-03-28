""""https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=120&id_problem=741"""

n, m = map(int, input().split())
a = []
s = 0
s1 = 0
for k in range(n):
    a.append(list(map(int, input().split())))
for h in a:
    s = 0
    for g in h:
        s += g
    print(s, end=' ')
print()
for i in range(m):
    s1 = 0
    for j in range(n):
        s1 += a[j][i]
    print(s1, end=' ')
print()
print()
for r in a:
    print(*r)

