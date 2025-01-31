def frase():
    lista=['hola','mundo','hola','hola','mundo']
    if type(lista)!= list:
       print('No hay repetidos')
    else:
        contador= {}
        for i in lista:
            if i in contador:
                contador[i]+=1 
            else:
                contador[i]=1
        
        respuesta=list(contador.items())
        print (respuesta)

frase()