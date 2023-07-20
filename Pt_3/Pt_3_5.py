def is_composite(n):
    k = 2
    while k ** 2 <= n and n % k != 0:
        k = k + 1
    return k ** 2 > n


c = []
start = int(input("Начальное значение: "))
end = int(input("Конечное значение: "))
for i in range(start, end + 1):
    if is_composite(i) == 0:
        c.append(i)
print(c)
