n = int(input("Введите число: "))
even = lambda x: "Число – чётное" if x % 2 == 0 else "Число – нечётное"
print(even(n))
