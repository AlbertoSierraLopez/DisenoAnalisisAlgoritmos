def seleccion_actividades(n, s, f):
    _ordenar_actividades(n, s, f)
    return _algoritmo_voraz(s, f, 0, n)


# Ordena los arrays de actividades en función de la finalización (f) de menor a mayor mediante bubble sort. Aunque f
# guía la ordenación, todos los cambios que se hacen en f deben replicarse en s para mantener la estructura de
# pares (inicio, fin)
def _ordenar_actividades(n, s, f):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if f[j] < f[j - 1]:
                aux_f = f[j]
                aux_s = s[j]
                f[j] = f[j - 1]
                s[j] = s[j - 1]
                f[j - 1] = aux_f
                s[j - 1] = aux_s


# k representa el subproblema
def _algoritmo_voraz(s, f, k, n):
    m = k + 1
    while m < n and s[m] < f[k]:
        m = m + 1
    if m <= n:
        return 1 + _algoritmo_voraz(s, f, m, n)
    else:
        return 0


####################
# Función iterativa para leer una lista de n números enteros
def lee_lista(n):
    a = []
    if n > 0:
        cadenaEntrada = input()
        for i in range(0, n):
            elemento = int(cadenaEntrada.split(" ")[i])
            a.append(elemento)
    return a


####################


n = int(input())
s = lee_lista(n)
f = lee_lista(n)
print(seleccion_actividades(n, s, f))