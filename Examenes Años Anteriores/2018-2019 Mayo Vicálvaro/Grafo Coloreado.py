import numpy as np

def Grafo_Coloreado_Wrapper(G, m):
    (p, q) = G.shape
    sol_parcial = [None] * p
    return Grafo_Coloreado(G, 0, p, m, sol_parcial)


def Grafo_Coloreado(G, i, n, m, sol_parcial):
    if i == n:
        print(sol_parcial)
        return True
    else:
        k = 0
        encontrado = False
        while k < m and not encontrado:
            if Valido(G, n - 1, i, k, sol_parcial):
                sol_parcial[i] = k

                encontrado = Grafo_Coloreado(G, i + 1, n, m, sol_parcial)

                sol_parcial[i] = None

            k = k + 1

        return encontrado


def Valido(G, n, nodo, color, parcial):
    if n < 0:
        return True
    else:
        if G[n, nodo]:
            if parcial[n] == color:
                return False
        return Valido(G, n - 1, nodo, color, parcial)


G = np.array([[0, 1, 1, 1, 1],
              [1, 0, 1, 0, 0],
              [1, 1, 0, 0, 1],
              [1, 0, 0, 0, 0],
              [1, 0, 1, 0, 0]])
m = int(input())
print(Grafo_Coloreado_Wrapper(G, m))
