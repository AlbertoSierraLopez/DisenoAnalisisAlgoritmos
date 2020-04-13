def ordenacionburbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1, i, -1):
            if lista[j] < lista[j - 1]:
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux


vLista = [5, 9, 3, 4, 8, 1, 2, 7, 6]
print(vLista)
ordenacionburbuja(vLista)
print(vLista)
