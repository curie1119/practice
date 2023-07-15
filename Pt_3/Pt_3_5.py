def is_composite(n):
    k = 2
    while k ** 2 <= n and n % k != 0:
        k = k + 1
    return (k ** 2 > n)

b = [i for i in range(int(input("Начальное значение: ")), int(input("Конечное значение: ")) + 1) if is_composite(i) == False]
print(b)