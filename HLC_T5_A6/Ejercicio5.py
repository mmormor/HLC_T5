def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

lista_ordenada = [8, 6, 1, 4]
bubble_sort(lista_ordenada)
print("Lista ordenada:", lista_ordenada)
