


intentos=0
while True:
    password=input('ingrese su contraseña: ')
    intentos=+1
    if( password == 'root'):
        print('bienvenido a su cuenta')
        break
    elif(intentos==3):
        print('tuviste muchos inentos fallidos, se bloqueo su cuenta')
        break
    else:
        print(f'intente de nuevo. quedan{3-intentos} intentos ')





cont=0
cuntinue= (input('continuamos?'))   
while cuntinue=='1':
    cont+-1
    print(f'cuntinuamos {cont} veces ')  
    cuntinue= (input('continuamos?'))   