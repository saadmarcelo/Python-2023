# Set (listas)
    # Similar a listas
    # Evita itens duplicados
    # Nao utiliza index

list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # union
print(num1 - num2) # Diference
print(num1 ^ num2) # Symetric difference
print(num1 & num2) # And
