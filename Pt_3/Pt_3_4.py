list1 = input("Введите строку чисел: ").split()
squares = [int(i) ** 2 for i in list1]
print(squares)