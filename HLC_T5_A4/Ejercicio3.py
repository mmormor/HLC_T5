def bas_exp(a,b):
        cont=a
        for i in range(1,b):
                cont*=a
        
        return cont

a=int(input("Introduce la base: "))
b=int(input("Introduce el exponente: "))
resultado=bas_exp(a,b)
print(resultado)
