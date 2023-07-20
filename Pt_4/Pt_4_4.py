from itertools import combinations
nums = list(map(int, input("Введите числа: ").split()))
num = int(input("Введите число: "))
new_nums = []
for x in range(1, len(nums) + 1):
    for y in combinations(nums, x):
        if sum(y) == num:
            new_nums.append(sorted(y))
print(new_nums)
