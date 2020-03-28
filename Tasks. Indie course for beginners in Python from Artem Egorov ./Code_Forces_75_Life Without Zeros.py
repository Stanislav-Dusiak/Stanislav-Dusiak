"""Can you imagine our life if we removed all zeros from it?
For sure we will have many problems. In this problem we will have a simple
example if we removed all zeros from our life, it's the addition operation.
Let's assume you are given this equation a + b = c, where a and b are positive
integers, and c is the sum of a and b. Now let's remove all zeros from this
equation. Will the equation remain correct after removing all zeros? For
example if the equation is 101 + 102 = 203, if we removed all zeros it will
be 11 + 12 = 23 which is still a correct equation. But if the equation
is 105 + 106 = 211, if we removed all zeros it will be 15 + 16 = 211 which is
not a correct equation."""

y = int(input())
z = int(input())
a = y
b = z
c = y + z
k = 0
d = []
d1 = []
d2 = []
while a > 0:
    k = a % 10
    if k != 0:
        d.append(k)
    a = a // 10
d.reverse()
v = ''.join(str(e) for e in d)
while b > 0:
    k1 = b % 10
    if k1 != 0:
        d1.append(k1)
    b = b // 10
d1.reverse()
v1 = ''.join(str(e) for e in d1)
while c > 0:
    k2 = c % 10
    if k2 != 0:
        d2.append(k2)
    c = c // 10
d2.reverse()
res = ''.join(str(e) for e in d2)
if int(v) + int(v1) == int(res):
    print('YES')
else:
    print('NO')

