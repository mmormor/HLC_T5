def vocal_conso():
    frase= 'hola mundo'
    vocales=['a','e','i','o','u']
    contador_voc=0
    contador_cons=0
    for i in frase:
        if i in vocales :
            contador_voc+=1
        else:
            contador_cons+=1
    print('Vocales',contador_voc,'Consonantes',contador_cons)      
vocal_conso()