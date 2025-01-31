def contar_digitos(numero):
    
    digitos = 0
    for n in numero :
        digitos += 1
        
    print(digitos)

numero=int(input("Introduzca un número: "))
contar_digitos(str(numero))

