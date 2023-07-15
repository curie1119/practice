n = int(input("Введите число: "))
even = lambda n: n%2
if even(n) == 0:
    print("Число", n, "– чётное")
else:
    print("Число", n, "– нечётное")