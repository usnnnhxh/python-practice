estoque = {"maçã": 10, "banana": 5, "laranja": 8}

tirar = int(input("remover: "))
sum = int(input("adicionar: "))


estoque["maçã"] = (estoque["maçã"] - tirar)
estoque["banana"] = (estoque["banana"] + sum ) 

for item, quantidade in estoque.items():
    if quantidade < 0:
        print("Item invalido.")
    else:
        print(item, quantidade)