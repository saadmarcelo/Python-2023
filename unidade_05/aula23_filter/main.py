# Filter Function
    # Muito utilizado com listas
    # Aplicar uma funcao a um Iterable, filtrando os items

valores = [10,12,34,44,57]

def remover20(x):
    return x > 20

print(list(filter(remover20, valores)))

print(list(filter(lambda x: x > 20, valores)))