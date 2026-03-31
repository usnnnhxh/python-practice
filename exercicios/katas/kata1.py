# Dado uma lista de números, retorne a soma
# apenas dos números negativos.
# Se não houver negativos, retorne 0.

# Exemplos:
# [1, -4, 7, -3, 2]  → -7
# [1, 2, 3]          → 0
# [-5, -1, -10]      → -16


def sum_negatives(numbers):
    total = 0 
    for number in numbers:
        if number < 0:
            total = number + total # -3 + -4
    return total
print(sum_negatives([-5, -1, -10]))