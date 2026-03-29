word = "banana"

letras = { }


for letter in word:
    if letter in letras:
        letras[letter] += 1
    else:
        letras[letter] = 1

print(letras)   