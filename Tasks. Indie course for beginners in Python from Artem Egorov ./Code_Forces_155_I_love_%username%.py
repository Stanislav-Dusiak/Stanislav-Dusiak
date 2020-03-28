"""Vasya adores sport programming. He can't write programs but he loves to
watch the contests' progress. Vasya even has a favorite coder and Vasya pays
special attention to him. One day Vasya decided to collect the results of all
contests where his favorite coder participated and track the progress of his
coolness. For each contest where this coder participated, he wrote out a single
non-negative number — the number of points his favorite coder earned in the
contest. Vasya wrote out the points for the contest in the order, in which the
contests run (naturally, no two contests ran simultaneously). Vasya considers
a coder's performance in a contest amazing in two situations: he can break
either his best or his worst performance record. First, it is amazing if during
the contest the coder earns strictly more points that he earned on each past
contest. Second, it is amazing if during the contest the coder earns strictly
less points that he earned on each past contest. A coder's first contest isn't
considered amazing. Now he wants to count the number of amazing performances
the coder had throughout his whole history of participating in contests. But
the list of earned points turned out long and Vasya can't code... That's why
he asks you to help him."""

n = int(input())
a = list(map(int, input().split()))
m = len(a)
res = 0
max = a[0]
min = a[0]
for i in range(m - 1):
    if a[i + 1] > a[i] and a[i + 1] > max:
        max = a[i + 1]
        res += 1
    if a[i + 1] < a[i] and a[i + 1] < min:
        min = a[i + 1]
        res += 1
print(res)

