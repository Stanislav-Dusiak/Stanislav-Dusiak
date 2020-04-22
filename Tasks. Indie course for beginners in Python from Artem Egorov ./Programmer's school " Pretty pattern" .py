""""https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=8&id_topic=121&id_problem=748&ins=1#solution"""

a = []
count_yes = 0
count_no = 0
for t in range(4):
    a.append(input())
for i in range(3):
    for j in range(3):
        if a[i][j] == a[i][j + 1] == a[i + 1][j] == a[i + 1][j + 1]:
            count_no += 1
        else:
            count_yes += 1
if count_no > 0:
    print('No')
else:
    print('Yes')

