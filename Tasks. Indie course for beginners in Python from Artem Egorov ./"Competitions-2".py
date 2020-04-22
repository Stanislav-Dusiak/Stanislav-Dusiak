""""https://informatics.msk.ru/mod/statements/view3.php?id=282&chapterid=357#1"""

n, m = map(int, input().split())
a = []
b = []
z = []
v = []
for t in range(n):
    a.append(list(map(int, input().split())))
for i in a:
    b.append(max(i))
z.append(a[b.index(max(b))])
v = z[0]
print(max(b))
print(b.index(max(b)), (v.index(max(v))))

