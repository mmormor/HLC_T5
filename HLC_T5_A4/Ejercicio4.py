def contar_digitos(numero):
    
    digitos = 0
    for n in numero :
        digitos += 1
        
    return digitos

numero=int(input("Introduzca un número: "))
resultado=contar_digitos(str(numero))
print(resultado)

