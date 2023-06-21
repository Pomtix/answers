def palindrome(string):
    return string == string[::-1]

print(palindrome('level'))
print(palindrome('dot'))