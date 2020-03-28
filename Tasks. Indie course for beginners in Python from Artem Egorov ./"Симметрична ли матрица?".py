""""https://informatics.msk.ru/mod/statements/view3.php?id=282&chapterid=355#1"""

n = int(input())
a = []
count = 0
for k in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    for j in range(n):
        if a[i][j] == a[j][i]:
            count += 1
        else:
            count = 0
if count == n ** 2:
    print('yes')
else:
    print('no')

