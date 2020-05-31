def Permutacion_Optima(n, i, w, f_objetivo, validos, sol_parcial, peso_parcial, sol_mejor, peso_mejor):
    if i == len(n):
        if peso_parcial < peso_mejor:
            peso_mejor = peso_parcial
            for j in range(len(n)):
                sol_mejor[j] = sol_parcial[j]
    else:
        for k in range(len(n)):
            if validos[k]:

                validos[k] = False
                sol_parcial[i] = k
                peso_anterior = peso_parcial
                peso_parcial = f_objetivo(i, sol_parcial, w)

                if peso_parcial < peso_mejor:
                    peso_mejor = Permutacion_Optima(n, i + 1, w, f_objetivo, validos, sol_parcial, peso_parcial, sol_mejor, peso_mejor)

                validos[k] = True
                sol_parcial[i] = [None]
                peso_parcial = peso_anterior

    return peso_mejor


def Permutacion_Optima_Wrapper(n, w, f_objetivo):
    a = [0] * n
    for i in range(n):
        a[i] = i
    validos = [True] * n
    sol_parcial = [None] * n
    sol_mejor = [None] * n
    peso_mejor = Permutacion_Optima(a, 0, w, f_objetivo, validos, sol_parcial, 0, sol_mejor, (n ** 3) + 1)
    print(peso_mejor)
    print(sol_mejor)



def f_objetivo(m, p, w):
    sum = 0
    for i in range(m + 1):
        sum += p[i] * i
    if sum < w:
        return sum
    else:
        return w


n = int(input())
w = int(input())
Permutacion_Optima_Wrapper(n, w, f_objetivo)
