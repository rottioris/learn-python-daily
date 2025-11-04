from sqlalchemy import tuple_


mi_tuple = (1,2,3,4,5) # con o sin parentesis es una tupla

tuple = ('juan', (10,20), 120) # los tuples son inmutables

print(tuple[1][0])


mi_tuple = list(mi_tuple) #casting
print(type(mi_tuple))

# Asignar el contenido de un tuple a diferentes variables

t = (1,2,3)
x,y,z = t    # desempacar
print(x,y,z)

# metodos de los tuples
print(t.count(1))
print(t.index(2))