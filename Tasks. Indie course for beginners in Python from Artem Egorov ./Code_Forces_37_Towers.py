""""Little Vasya has received a young builder’s kit. The kit consists of
several wooden bars, the lengths of all of them are known. The bars can be put
one on the top of the other if their lengths are the same. Vasya wants to
construct the minimal number of towers from the bars. Help Vasya to use the
bars in the best way possible.
Input
The first line contains an integer N (1 ≤ N ≤ 1000) — the number of bars at
Vasya’s disposal. The second line contains N space-separated integers li — the
lengths of the bars. All the lengths are natural numbers not exceeding 1000.
Output
In one line output two numbers — the height of the largest tower and their
total number. Remember that Vasya should use all the bars."""

n = int(input())
a = list(map(int, input().split()))
m = len(a)
z = 0
count = 0
g = []
for i in range(m):
    if a.count(a[i]) > z:
        z = a.count(a[i])
for k in range(m):
    for j in range(m):
        if a[j] == a[k] and a[j] not in g:
            g.append(a[j])
print(z, len(g))

