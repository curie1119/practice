num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))
mx = max(num1, num2, num3)
mn = min(num1, num2, num3)
sr = num1 + num2 + num3 - mx - mn
print("Максимальное число: ", mx, ".", "Список чисел: ", mx, ",", sr, ",", mn)