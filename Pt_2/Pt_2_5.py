import random
lose = 0
vict = 0
k = 0
while k < 3:
    player = int(input("Орёл – 1 или решка – 0: "))

    if player != 0 and player != 1:
        print("Вы ввели не то число. Начните игру заново")
        break

    program = random.choice([0, 1])
    if player == program:
        vict = vict + 1
        k = 0
        print("Вы выиграли")

    else:
        lose = lose + 1
        k = k + 1
        print("Вы проиграли")

    print("Количество выиграшей составляет", vict,
          "раз(а), а проигрышей,", lose, "раз(а)")
    print()
print("Игра окончена")
