#Crea un programa que pida al usuario el radio de un círculo y muestre su
#diámetro, su circunferencia y su área.
#Supón que pi es aproximadamente 3.14159.


PI=3.14159

radio=float(input('ingrese el radio del circulo: '))
print(f'el diametro del circulo es:{round(radio*2,2)}')
print(f'la circunferencia del circulo es:{round(2*PI*radio,2)} ')
print(f'el area del circulo es:{round(PI*radio*radio,2)} ')