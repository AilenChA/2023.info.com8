#Escribe un programa que solicite al usuario su fecha de nacimiento en formato
#dd/mm/aaaa y luego imprima su edad en años.
#Utiliza la función .split()


fecha=input('ingrese la fecha ACTUAL en formato DD/MM/AAAAA: ')
nacimiento= input('ingrese la fecha de NACIMIENTO en formato DD/MM/AAAAA: ')

lista1=fecha.split("/")
lista2=nacimiento.split("/")

print(f'Su edad aproximadamente es de {int(lista1[2])-int(lista2[2])} años, ¿correcto?')