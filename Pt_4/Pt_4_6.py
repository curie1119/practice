def rot13(s):
    key = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" \
          "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "мнопрстуфхцчшщъыьэюяабвгдеёжзийклМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛ" \
          "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in s)


print(rot13(input("Введите строку: ")))
