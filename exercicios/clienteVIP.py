clientes = [
    {"nome": "Ana", "saldo": 1500, "vip": True},
    {"nome": "Bruno", "saldo": 300, "vip": False},
    {"nome": "Carla", "saldo": 800, "vip": True},
    {"nome": "Diego", "saldo": 100, "vip": False},
]

for cliente in clientes:
    if(cliente["vip"]) and cliente["saldo"] > 500:
        print(cliente['nome'],"- Cliente Premium")
    elif (cliente["vip"]) != True and cliente["saldo"] > 500:
        print(cliente["nome"], "- Cliente comum")
    else:
        print(cliente["nome"], "saldo insuficiente")