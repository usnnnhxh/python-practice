# loja1 = {"maçã": 10, "banana": 5, "uva": 8}
# loja2 = {"banana": 3, "uva": 7, "manga": 4}

# # resultado esperado:
# # {"maçã": 10, "banana": 8, "uva": 15, "manga": 4}

# lojas = {}

# lojas.update(loja1)

# lojas.update(loja2)


# for fruta in loja1:

#      if fruta in loja2:
#         lojas[fruta] = loja1.get(fruta) + loja2.get(fruta)

# print(lojas)

loja1 = {"maçã": 10, "banana": 5, "uva": 8}
loja2 = {"banana": 3, "uva": 7, "manga": 4}

lojas = {}

for fruta, quantidade in loja1.items():
    lojas[fruta] = quantidade

for fruta, quantidade in loja2.items():
    lojas[fruta] = lojas.get(fruta) + quantidade

