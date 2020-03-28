""""https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=749&ins=1#solution"""

a = []
b = []
count = 0
n, m = map(int, input().split())
for t in range(n):
    a.append(input())
o = input()
for t1 in range(n):
    b.append(input())
for i in range(n):
    for j in range(m):
        if a[i][j] == b[i][j]:
            count += 1
print(count)

