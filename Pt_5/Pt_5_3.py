import csv


def bk(start1, end1):
    bks = []
    with open("Books.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            year = int(row["Год выпуска"])
            if end1 <= year <= start1:
                print("Убедитесь, "
                      "что вы не перепутали начальный год и конечный")
                a = int(input("Введите начальный год: "))
                b = int(input("Введите конечный год: "))
                bk(a, b)
            for year in range(start1, end1 + 1):
                year = str(year)
                if year == row["Год выпуска"]:
                    print(row)
                    bks.append(row)
        if not bks:
            print("В этом промежутке нет книг!")


try:
    start = int(input("Введите начальный год: "))
    end = int(input("Введите конечный год: "))
    bk(start, end)
except ValueError:
    print("Введите числа!")
    start = int(input("Введите начальный год: "))
    end = int(input("Введите конечный год: "))
    bk(start, end)
