def suma(numero):
    con=1
    for n in range(1,numero+1):
        con*=n
    return con
    
numero=int(input("Introduce un numero: "))
resultado=suma(numero)
print(resultado)
