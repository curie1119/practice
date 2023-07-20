f = lambda a: sum(a) / len(a)
nums = list(map(int, input("Введите строку чисел: ").split()))
print(f(nums))
