num1=int(input('Introduce el primer numero '))
num2=int(input('Introduce el segundo numero '))
num3=int(input('Introduce el tercer numero '))
if(num1==num2 and num2==num3):
    print('Los tres numero son iguales')
elif(num1>num2 and num1>num3 ):
    print('El ',num1,' es mayor que',num2,' y ',num3)

elif(num2>num3 and num2>num1):
    print('El ',num2,' es mayor que',num1,' y ',num3)

elif(num3>num2 and num3>num1):
    print('El ',num3,' es mayor que',num1,' y ',num2)

elif(num1==num2 and num1==num3):
    print('Los tres numeros son igaules por lo que no hay mayor')

elif(num1==num2):
    print('Hay un empate entre los mayores: ',num1, 'y ',num2)

elif(num1==num3):
   print('Hay un empate entre los mayores: ',num1, 'y ',num3)
elif(num2==num3):
    print('Hay un empate entre los mayores: ',num2, 'y ',num3)    