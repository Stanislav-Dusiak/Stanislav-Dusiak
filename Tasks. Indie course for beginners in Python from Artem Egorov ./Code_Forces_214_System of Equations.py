"""Furik loves math lessons very much, so he doesn't attend them, unlike Rubik.
But now Furik wants to get a good mark for math. For that Ms. Ivanova, his math 
teacher, gave him a new task. Furik solved the task immediately. Can you?
You are given a system of equations:"""
"""You are given a system of equations: a**2 + b = n a + b**2 = m; 
You should count, how many there are pairs of integers (a, b) (0 ≤ a, b) 
which satisfy the system."""

"""First method"""

n, m = map(int, input().split())
if (m + n) < 10:
    x = (m + n) ** 2
else:
    x = max(n, m)
a = -1
b = 0
count = 0
for i in list(range(x)):
    if a ** 2 + b == n and a + b ** 2 == m:
        a += 1
    else:
        a += 1
        for j in list(range(x)):
            if a ** 2 + b == n and a + b ** 2 == m:
                count += 1
                b += 1
            else:
                b += 1
        b = 0
print(count)


"""Second method"""

n, m = map(int, input().split())
if (m + n) < 10:
    x = (m + n) ** 2
else:
    x = max(n, m)
a = 0
b = 0
count = 0
for i in list(range(x)):
    for j in list(range(x)):
        if a ** 2 + b == n and a + b ** 2 == m:
            count += 1
            b += 1
        else:
            b += 1
    a += 1
    b = 0
print(count)

