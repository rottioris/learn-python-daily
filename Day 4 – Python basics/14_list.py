mi_lista = ['Juan',1.92,14,'hombre']

r_d1 = len(mi_lista)
r_d2 = mi_lista[0:2]

print(r_d1, r_d2)


l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = l1 + l2

print(l3)



l3[0] = 'beta' # sobreescribir un elemento
print(l3)

l3.append(9) # agregar un elemento
print(l3)

eliminado = l3.pop(2) # eliminar un elemento
print(l3)
print(eliminado)

# ordenar las listas

lst = ['g','o','m','c']
lst.sort()
print(lst)

lst.reverse()
print(lst)