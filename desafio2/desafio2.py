# Desafío 2: Analizador de textos
# Requisitos técnicos:
# Se te pide crear un programa que le pida al usuario que ingresar un texto
# cualquiera, por ejemplo, un artículo o una frase.
# Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
# elección.
# Nuestro código va a procesar esa información para realizar los análisis
# necesarios para devolverle al usuario la siguiente información:
# 1- Cantidad de veces que aparece cada una de letras que eligió.
# Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
# string
# Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
# encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
# minúscula.
# 2- Cuantas palabras hay en total en todo el texto.
# Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
# 3- Cual es la primera letra y cuál es la última. (Indexación)
# 4- Mostrar el texto en orden inverso.
# 5- Decir si la palabra "python" aparece en el texto.
# Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
# string para mostrar al usuario.


texto=input('Ingrese alguna frase o texto: ')

letra1=input('Ingresa la 1ª letra: ')
letra2=input('Ingresa la 2ª letra: ')
letra3=input('Ingresa la 3ª letra: ')



texto = texto.lower()
letras=[letra1.lower(),letra2.lower(),letra3.lower()]


for letra in letras:
    print(f' La letra {letra} apareció {texto.count(letra)} veces. ')

palabras = texto.replace('.','')
palabras= palabras.replace(':','')
palabras= palabras.replace(';','')
palabras_sep= palabras.split(' ')

cant_palabras=len(palabras_sep)

print ('La cantidad de palabras en el texto es de: ', cant_palabras)    

print('La primera letra es:',palabras[0],'La ultima letra es:',palabras[-1])


texto_reversa=palabras[::-1]

palabras_reversa= palabras_sep[::-1]
print('El texto en forma inversa (literalmente):',texto_reversa)

texto_palabras_reversa=' '.join(palabras_reversa)
print('El texto en forma inversa como string:', texto_palabras_reversa)

if ('python' in texto):
    print('Existe python en el texto')
else:
    print('NO existe python en el texto')    