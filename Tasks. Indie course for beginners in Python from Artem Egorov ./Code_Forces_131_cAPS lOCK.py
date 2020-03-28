""""https://codeforces.com/contest/131/submission/71057787"""

a = input()
count = 0
count1 = 0
b = a[1:]
for j in b:
    if 'a' <= j <= 'z':
        count += 1
    else:
        count1 += 1
if count >= 1:
    print(a)
else:
    if count1 == len(b) and 'a' <= a[0] <= 'z':
        print(a.capitalize())
    else:
        print(a.lower())

