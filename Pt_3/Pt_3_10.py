s = input("Введите строку: ")
dict = {}
for i in s:
    if i != ' ':
        dict[i] = s.count(i)
print(dict)