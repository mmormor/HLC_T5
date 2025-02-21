import random

def generar_contraseña(longitud):
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    especiales = '!"#$%&'
    caracteres = letras + numeros + especiales
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    return contraseña


longitud = 20
print(generar_contraseña(longitud))
