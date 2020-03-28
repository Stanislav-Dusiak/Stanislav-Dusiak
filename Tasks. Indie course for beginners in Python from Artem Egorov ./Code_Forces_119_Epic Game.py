"""Simon and Antisimon play a game. Initially each player receives one
fixed positive integer that doesn't change throughout the game. Simon receives
number a and Antisimon receives number b. They also have a heap of n stones.
The players take turns to make a move and Simon starts. During a move a player
should take from the heap the number of stones equal to the greatest common
divisor of the fixed number he has received and the number of stones left in
the heap. A player loses when he cannot take the required number of stones
(i. e. the heap has strictly less stones left than one needs to take).
Your task is to determine by the given a, b and n who wins the game."""

h, z, n = map(int, input().split())
i = 0
while n > 0:
    a = h
    b = z
    k = n
    while k > 0:
        c = a % k
        a = k
        k = c
    if n >= a:
        n -= a
        i += 1
    else:
        break
    k = n
    while k > 0:
        c = b % k
        b = k
        k = c
    if n >= b:
        n -= b
        i += 1
    else:
        break
if i % 2 == 0:
    print('1')
else:
    print('0')

