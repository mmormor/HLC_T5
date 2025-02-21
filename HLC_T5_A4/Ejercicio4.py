<<<<<<< HEAD
def suma(n):
    if n == 0:
        return 0
    else:
        return n%10 + suma(int(n/10))
n=int(input("Introduzca un número: "))
print(suma(n))
=======
def contar_digitos(numero):
    
    digitos = 0
    for n in numero :
        digitos += 1
        
    return digitos

numero=int(input("Introduzca un número: "))
resultado=contar_digitos(str(numero))
print(resultado)
>>>>>>> d137e77e8b90803bd73eb4e070ef23cfac3a4223

