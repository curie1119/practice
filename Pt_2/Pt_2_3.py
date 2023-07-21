a = int(input("Введите число: "))


def check(x):
    n = 0
    while x != 0:
        n += 1
        x = x//10
    return n


n = check(a)
print(n)


def isarmstr(x):
    sum = 0
    abc = x
    n = check(x)
    while abc != 0:
        b = abc % 10
        sum = sum + (b**n)
        abc = abc//10
    return sum


c = isarmstr(a)
if a == c:
    print("Число", a, "является числом Армстронга")
else:
    print("Число", a, "не является числом Армстронга")
