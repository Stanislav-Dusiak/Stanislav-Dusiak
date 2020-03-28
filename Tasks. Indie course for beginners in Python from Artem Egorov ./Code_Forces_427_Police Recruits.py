"""The police department of your city has just started its journey. Initially, 
they don’t have any manpower. So, they started hiring new recruits in groups.
Meanwhile, crimes keeps occurring within the city. One member of the police 
force can investigate only one crime during his/her lifetime. If there is no 
police officer free (isn't busy with crime) during the occurrence of a crime, 
it will go untreated. Given the chronological order of crime occurrences and 
recruit hirings, find the number of crimes which will go untreated."""

n = int(input())
a = list(map(int, input().split()))
unsolved_crimes = 0
police_officers = 0
crimes = 0
m = len(a)
for i in range(m):
    if crimes == 0 and a[i] == -1 and police_officers == 0:
        unsolved_crimes += 1
    elif a[i] == -1:
        police_officers -= 1
    if a[i] > 0:
        police_officers += a[i]
print(unsolved_crimes)

