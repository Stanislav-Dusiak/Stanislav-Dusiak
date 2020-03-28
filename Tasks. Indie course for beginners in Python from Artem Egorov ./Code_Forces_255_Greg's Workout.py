""""Greg is a beginner bodybuilder. Today the gym coach gave him the training
plan. All it had was n integers a1, a2, ..., an. These numbers mean that Greg
needs to do exactly n exercises today. Besides, Greg should repeat the i-th in
order exercise ai times. Greg now only does three types of exercises: "chest"
exercises, "biceps" exercises and "back" exercises. Besides, his training is
cyclic, that is, the first exercise he does is a "chest" one, the second one is
"biceps", the third one is "back", the fourth one is "chest", the fifth one is
"biceps", and so on to the n-th exercise. Now Greg wonders, which muscle will
get the most exercise during his training. We know that the exercise Greg
repeats the maximum number of times, trains the corresponding muscle the most.
Help Greg, determine which muscle will get the most training.
Input
The first line contains integer n (1 ≤ n ≤ 20). The second line contains n 
integers a1, a2, ..., an (1 ≤ ai ≤ 25) — the number of times Greg repeats the 
exercises.

Output
Print word "chest" (without the quotes), if the chest gets the most exercise, 
"biceps" (without the quotes), if the biceps gets the most exercise and print 
"back" (without the quotes) if the back gets the most exercise.

It is guaranteed that the input is such that the answer to the problem
is unambiguous."""

n = int(input())
a = list(map(int, input().split()))
m = len(a)
k = []
chest = []
biceps = []
back = []
for i in range(m):
    back = a[2::3]
    biceps = a[1::3]
    chest = a[::3]
if sum(back) >= sum(chest) and sum(back) >= sum(biceps):
    print('back')
if sum(chest) >= sum(back) and sum(chest) >= sum(biceps):
    print('chest')
if sum(biceps) >= sum(chest) and sum(biceps) >= sum(back):
    print('biceps')

