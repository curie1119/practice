import itertools
nums = input("Введите элементы: ").split()
for i in itertools.permutations(nums):
    print(i)
