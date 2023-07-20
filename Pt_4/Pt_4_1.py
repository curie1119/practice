a = [int(i) for i in input("Введите число: ")]
maxi = int(''.join(map(str, sorted(map(int, list(a)), reverse=True))))
print("Максимальное число из данного набора:", maxi)
