def is_composite(n):
    k = 2
    while k ** 2 <= n and n % k != 0:
        k = k + 1
    return k ** 2 > n


c = []
a = int(input("Начальное значение: "))
b = int(input("Конечное значение: "))
for i in range(a, b + 1):
    if is_composite(i):
        c.append(i)
print(c)
