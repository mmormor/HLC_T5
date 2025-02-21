def suma(n):
    if n == 0:
        return 0
    else:
        return n%10 + suma(int(n/10))
n=int(input("Introduzca un número: "))
print(suma(n))

