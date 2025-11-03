

from traceback import print_tb


dic = {'c1':'v1','c2':'v2'}
res = dic['c1']

print(res)


cliente = {'nombre':'ori','apellido':'rotti','peso':12,'talla':1.42}
consulta = cliente['apellido']
print(consulta)


diccionario = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}}

print(diccionario['c2'][1])
print(diccionario['c3']['s2'])

ejs = {'c1':['a','b','c'],'c2':['d','e','f']}

print(ejs['c2'][1].upper())

d1 = {1:'a',2:'b'} # agregar
d1[3] = 'c'

print(d1)

d1[2] = 'B' #sobreescribir
print(d1)


print(d1.keys())
print(d1.values())
print(d1.items())