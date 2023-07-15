nums = list(map(int, input("Введите строку чисел: ").split()))
sr = lambda a: sum(a) / len(a)
print(sr(nums))