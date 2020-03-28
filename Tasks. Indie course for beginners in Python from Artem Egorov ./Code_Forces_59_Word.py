""""http://codeforces.com/contest/59/problem/A"""

n = input()
d = len(n)
a = []
b = []
for i in n:
    if i >= 'a' and i <= 'z':
        a.append(i)
    else:
        b.append(i)
if len(b) > len(a):
    z = n.upper()
else:
    z = n.lower()
print(z)

