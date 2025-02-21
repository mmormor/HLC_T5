def n_esimo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return n_esimo(n-1)+n_esimo(n-2)
   
n=int(input("Introduce un numero: "))
resultado=n_esimo(n)
<<<<<<< HEAD
print(resultado)
=======
print(resultado)
>>>>>>> d137e77e8b90803bd73eb4e070ef23cfac3a4223
