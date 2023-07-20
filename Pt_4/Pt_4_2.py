s = input("Введите строку: ")
pal = []
for i in range(1, len(s)):
    for j in range(i, len(s)):
        if s[i:j + 1] == s[j:i - 1:-1]:
            pal.append(s[i:j + 1])
print(pal)
