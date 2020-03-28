""""https://informatics.msk.ru/mod/statements/view3.php?id=282&chapterid=362#1"""

n, m = map(int, input().split())
tri = []
for t in range(n):
    tri.append([0] * m)
for t in range(1):
    for t1 in range(m):
        tri[t][t1] = 1
for t2 in range(n):
    for t3 in range(1):
        tri[t2][t3] = 1
for i in range(1, n):
    for j in range(1, m):
        tri[i][j] = tri[i - 1][j] + tri[i][j - 1]
for j in tri:
    print(*j)

