from sys import getsizeof


# Generator Expressions
    # Uma forma mais rapido para listas, dicionarios e etc
    # Menos memoria alocada
    # Valores em bytes


numeros = [x * 10 for x in range(10000)]
print(type(numeros))

print(getsizeof(numeros))

print('============')

numeros = (x * 10 for x in range(10000))
print(type(numeros))
#print(list(numeros))
print(getsizeof(numeros))
