list1 = set([1,2,3,4,5,6])
print(list1)

s1 = {1,2,3,4,5,6}
s1.add(7)
s1.add(2) # Evita itens duplicados
s1.update([7,8,9,10])
s1.remove(10)

print(s1)