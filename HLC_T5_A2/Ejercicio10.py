def estrella():
    estrella=int(input('Introduce un numero'))
    contador=0
    for index in range(estrella):
        contador+=1
        estrella='★'
        print(estrella*contador)

estrella()

