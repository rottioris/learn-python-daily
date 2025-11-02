# Son inmutables, no puedes cambiar su contenido

# Se pueden concatenar / multiplicar

n1 = 'Hola'
n2 = 'Ori'
print(n1*10)
# Son multilineas
n3 = """Este es
un salto de linea
con comillas dobles
o simples"""

print(n3)
# Se pueven verificar substrings
print("simple" in n3) # True or False
print('dobles' not in n3)

# Se puede calcular el largo con Len
print(len(n3))