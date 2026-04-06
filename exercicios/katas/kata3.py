#Escreva a função top_vendedores(vendedores, n) que recebe uma lista
#de dicionários com "nome" e "vendas", e retorna os nomes dos N
#melhores vendedores, ordenados do maior para o menor.

vendedores = [
    {"nome": "Carlos", "vendas": 40},
    {"nome": "Ana", "vendas": 85},
    {"nome": "Bruno", "vendas": 60},
    {"nome": "Diana", "vendas": 20},
    {"nome": "Eva", "vendas": 75},
]

def top_vendedores(vendedores, n):
    top_funcionarios = {}
    for vendedor in vendedores:
        nome = vendedor["nome"]
        top_funcionarios[nome] = vendedor["vendas"]

    ordered = sorted(top_funcionarios.items(), key=lambda item: item[1], reverse=True)

    final_list = []

    for nome in ordered[:n]:
        final_list.append(nome[0])

    return final_list
    
top_vendedores(vendedores, 4)