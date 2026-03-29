precos = {
    
}

total = 0

while True:
    item = input("Item: ")
    if not item.isalpha(): 
        print("Invalid!")    
    elif item.upper() == "QUIT":
        break

    price = float(input("Price: "))
    precos[item] = price

for price in precos.values():
    total += price
print(total)


