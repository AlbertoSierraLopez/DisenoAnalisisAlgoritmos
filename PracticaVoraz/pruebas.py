def _ordenar_actividades(n, s, f):
    for i in range(n):
        for j in range(n - 1, i, -1):
            if f[j] < f[j - 1]:
                auxf = f[j]
                auxs = s[j]
                f[j] = f[j - 1]
                s[j] = s[j - 1]
                f[j - 1] = auxf
                s[j - 1] = auxs


n = 11                                      # n = int(input())
s = [1, 2, 0, 5, 8, 5, 6, 8, 3, 3, 12]      # s = lee_lista(n)
f = [4, 13, 6, 7, 12, 9, 10, 11, 8, 5, 14]  # f = lee_lista(n)
print(s)
print(f)
_ordenar_actividades(n, s, f)
print(s)
print(f)