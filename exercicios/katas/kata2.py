# Dada uma lista de strings, retorne uma nova lista
# contendo apenas as strings que começam com letra maiúscula.

# verificar outras partes da string, checkar index 0 da palavra

# Exemplos:
# ["Hello", "world", "Python", "is", "Cool"] → ["Hello", "Python", "Cool"]
# ["apple", "Banana", "cherry"]              → ["Banana"]
# ["abc", "def"]                             → []

def filter_capitalized(words):
    isUpper = []
    for word in words:
        if word[0].isupper():
            isUpper.append(word)
    return isUpper

print(filter_capitalized(["Hello", "world", "Python", "is", "Cool"]))