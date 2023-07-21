import csv

n = int(input("Сколько записей Вы хотите добавить? "))
row = []
with open("Books.csv", "a", newline='') as f:

    for i in range(n):
        writer = csv.writer(f, delimiter=",")
        bk = str(input("Название книги: "))
        avt = str(input("Автор книги: "))
        year = str(input("Год выпуска: "))
        row.append([bk, avt, year])
        writer.writerows(row)
        row = []
f.close()

name = input("Книги какого автора вы хотели бы найти? ")

with open("Books.csv", "r") as f:
    k = 0
    for el in f:
        if name in el:
            print(el)
            k += 1
    if k == 0:
        print("Книги этого автора не найдены")
