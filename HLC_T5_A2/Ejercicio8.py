def cuadrado():
    num = int(input('Introduce un número entero positivo: '))

    cua = [i**2 for i in range(1,num+1)]
    print(cua)
cuadrado()