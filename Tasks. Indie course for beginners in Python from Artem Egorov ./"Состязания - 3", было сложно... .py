""""https://informatics.msk.ru/mod/statements/view3.php?id=282&chapterid=358#1"""

humans, tries = map(int, input().split())
mtr = []
maximums = []
sums = []
for _ in range(humans):
    results = list(map(int, input().split()))
    maximums.append(max(results))
    sums.append(sum(results))

max_of_maximums = max(maximums)
equals_indices = []
for i in range(len(maximums)):
    if maximums[i] == max_of_maximums:
        equals_indices.append(i)

if len(equals_indices) > 1:
    filtered_sums = []
    for eq_i in equals_indices:
        filtered_sums.append(sums[eq_i])

    max_sum = max(filtered_sums)
    print(sums.index(max_sum))

else:
    print(equals_indices[0])

