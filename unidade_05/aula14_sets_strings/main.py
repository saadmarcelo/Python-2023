# Set (Listas)
    # Similiar a lista
    # Evita itens duplicados
    # Nao utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

#set4 = set1.union(set2) # Uniao sem os duplicados
#set4 = set1.difference(set3) # Diferenca
set4 = set1.intersection(set2) # valores pertencentes aos 2 grupos


print(set4)