
from gettext import find


t = 'Este texto es la prueba de los metodos'

# upper() - pasar a mayus
ru = t[2].upper()
print(ru)

# lower() - pasar a minus
rl = t.lower()
print(rl)

# split() - separalo en partes (lista) 
rs = t.split("u")
print(rs)

# join()  - unir items usando separador

a = "Asi"
b = "funciona"
c = "el"
d = "metodo"
e = "join"
f = " ".join([a,b,c,d,e]) # Lista

print(f)

# find()  - encontrar un sub-string
rf = t,find('s')
print(rf)


# replace() - reemplazar un substring
rr = t.replace('texto','HOLA')
print(rr)