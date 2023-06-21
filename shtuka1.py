def palindrome(string):         # функция palindrome принимает аргумент-строку
    return string == string[::-1]       # сравнение строки с её перевернутым вариантом, возвращение True или False

print(palindrome('level'))
print(palindrome('dot'))

