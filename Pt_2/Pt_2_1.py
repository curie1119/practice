import random
print("фиолетовый, красный, синий, оранжевый, зелёный")
colour = random.choice(["фиолетовый", "красный", "синий", "оранжевый", "зелёный"])
again = True
while again:
    choice = input("Выберите цвет из вышеперечисленных:  ")
    choice = choice.lower()
    if colour == choice:
        print("Отлично!")
        again = False
    else:
        if colour == "фиолетовый":
            print("Цвет баклажана?")
        elif colour == "красный":
            print("Цвет помидора?")
        elif colour == "синий":
            print("Цвет голубики?")
        elif colour == "оранжевый":
            print("Цвет апелсина?")
        else:
            print("Цвет огурца?")
