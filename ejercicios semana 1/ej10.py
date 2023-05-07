#Crea un programa que pida al usuario una cantidad en dólares y la convierta a
#euros.
#Supón que el tipo de cambio es de 0.84 euros por dólar.
dolares=float(input('ingrese la cantidad de dolares: '))
print(f'Eso nos da {round(dolares*0.84)} euros')