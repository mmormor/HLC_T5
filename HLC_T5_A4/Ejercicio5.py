<<<<<<< HEAD
def suma(n):
    if n == 0:
        return 0
    if n < 10:
        return 1
    return 1 + suma(n/10)
=======
def contar_digitos(numero):
    
    digitos = 0
    dig=0
    for n in numero :
        digitos += 1
    for n in range(1,digitos+1):
        dig+=n   
    return 'La suma de toods los numeros es ',dig
   
numero=int(input("Introduzca un número: "))
resultado=contar_digitos(str(numero))
print(resultado)
>>>>>>> d137e77e8b90803bd73eb4e070ef23cfac3a4223

print(suma(1234))