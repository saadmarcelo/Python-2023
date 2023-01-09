# Map Function
    # Muito utilizada com listas
    # Aplicar uma funcao a um Iterable, por item.

lista1 = [1,2,3,4]
def mult(x):
    return x * 2

print(mult(2))

lista2 = map(mult, lista1)

print(list(lista2))