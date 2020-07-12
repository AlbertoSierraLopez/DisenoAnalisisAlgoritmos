# Modifica a
def insertar(a, n, sup):
    if sup < 0:
        a.insert(0, n)
    elif a[sup] <= n:
        a.insert(sup + 1, n)
    else:
        insertar(a, n, sup - 1)


# Devuelve una copia de a
def insertar_ordenada(a, x):
    n = len(a)
    if n == 0 or a[n - 1] <= x:
        return a + [x]
    else:
        return insertar_ordenada(a[0:n - 1], x) + [a[n-1]]


def insert_sort(a):
    n = len(a)
    if n <= 1:
        return a
    else:
        return insertar_ordenada(insert_sort(a[0:n - 1]), a[n - 1])


lista = [1, 3, 5, 7, 9]
lista1 = [7, 9, 3, 1, 5]

'''
x = int(input())
insertar(lista, x, len(lista)-1)
'''

x = int(input())
lista2 = insertar_ordenada(lista, x)

lista3 = insert_sort(lista1)

print("lista", lista)
print("lista1", lista1)
print("lista2", lista2)
print("lista3", lista3)
