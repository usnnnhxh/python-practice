clientes = [
    {"nome": "Ana", "idade": 28},
    {"nome": "", "idade": 34},
    {"nome": "Carlos", "idade": -5},
    {"nome": "Diego", "idade": 41},
    {"nome": "", "idade": -1},
]

# resultado esperado:
# [{"nome": "Ana", "idade": 28}, {"nome": "Diego", "idade": 41}]

clientes_limpo = []

for cliente in clientes:
    if cliente["nome"] != "" and cliente["idade"] > 0:
        clientes_limpo.append(cliente)

print(clientes_limpo)