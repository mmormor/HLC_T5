def contar_digitos(numero):
    
    digitos = 0
    dig=0
    for n in numero :
        digitos += 1
    for n in range(1,digitos+1):
        dig+=n   
    print('La suma de toods los numeros es ',dig)
   
    
    

numero=int(input("Introduzca un número: "))
contar_digitos(str(numero))

