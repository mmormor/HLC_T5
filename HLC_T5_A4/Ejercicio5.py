def suma(n):
    if n == 0:
        return 0
    if n < 10:
        return 1
    return 1 + suma(n/10)

print(suma(1234))