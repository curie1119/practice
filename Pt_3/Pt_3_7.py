vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
a = input("Введите строку: ")
dict = {i: True if i in vowels else False for i in a.replace(' ', '')}
print(dict)