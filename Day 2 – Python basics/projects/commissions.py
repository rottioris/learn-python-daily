nombre = input('Ingrese su nombre: ')
ventas = input('Ingrese sus ventas: ')

resultado = float(ventas) * 13 / 100

print(f'Ok {nombre}, este mes ganaste {round(resultado,4)}')