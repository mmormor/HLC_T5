
def adivinar():
    num=0
    import random
    numero = random.randint(1, 50) 

    while num!=numero:
        num=int(input('Adivina el numero')) 
        if num==numero:
            print('Correcto, el numero es ',numero)
        elif num>numero:
            print('El numero es menor')
        else:
            print('El numero es mayor')

adivinar()