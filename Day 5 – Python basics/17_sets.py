# los sets se pueden declarar de 2 maneras: set([1,2,3...]) o {1,2,3...}
# NO! Se admiten repeticiones de elementos, ni estar organizado en indice 0,1,2
# sus elementos son inmutables

from hashlib import sha1, shake_128


mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)


s = set ([1,2,3,4,5,1,(1,2,3),1,2,4,1,4])

print(len(s))
print(2 in s) 

# Unir sets

s1 = {1,2,3}
s2 = {3,4,5}

s3 = s1.union(s2)
print(s3)


# agregar

s1.add(4)
print(s1)

# eliminar

s1.remove(3)
print(s1)

# descartar

s1.discard(6)
print(s1)

# pop
s1.pop() # Eliminar un elemento aleatorio
print(s1)

# clear
s1.clear()
print(s1)