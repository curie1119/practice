s = ["Пятница", "Матч", "Звезда", "Культура"]
for i in s:
    print(i + ",")
tvprog = input("Введите название ещё одной телепередачи: ")
index = int(input("И введите позицию, на которую она должна быть вставлена: "))
s.insert(index - 1, tvprog)
for i in s:
    print(i + ",")
