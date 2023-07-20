def rot13(s):
    key = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" \
          "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" \
          "abcdefghijklmnopqrstuvwxyz" \
          "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "мнопрстуфхцчшщъыьэюяабвгдеёжзийкл" \
          "МНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛ" \
          "nopqrstuvwxyzabcdefghijklm" \
          "NOPQRSTUVWXYZABCDEFGHIJKLM"
    transform = dict(zip(key, val))
    return ''.join(transform.get(char, char) for char in s)


print(rot13(input("Введите строку: ")))
