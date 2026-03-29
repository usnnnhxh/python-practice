transacoes = [
    {"tipo": "entrada", "valor": 1500},
    {"tipo": "saida", "valor": 200},
    {"tipo": "entrada", "valor": 800},
    {"tipo": "saida", "valor": 1200},
    {"tipo": "entrada", "valor": 300},
    {"tipo": "saida", "valor": 100},
]

total_entrada = 0
total_saida = 0

contagem_entrada = 0
contagem_saida = 0

for txs in transacoes:
    if txs["tipo"] == "entrada":
        contagem_entrada += 1
        total_entrada = (txs["valor"]) + total_entrada
    else:
        contagem_saida += 1
        total_saida = txs["valor"] + total_saida

final = float(total_entrada - total_saida)

print(f"{contagem_entrada} entradas {total_entrada}, {contagem_saida} saidas {total_saida}")
if final < 0:
    print("negativou")
print(final)