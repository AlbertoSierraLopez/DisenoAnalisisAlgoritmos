def Torres_Wrapper(n):
    sol_parcial = [None] * n    # Representa las filas en las que pueden ir las torres, el indice son las columnas
    valido = [True] * n
    Torres(n, 0, sol_parcial, valido)

def Torres(n, i, sol_parcial, valido):
    if n == i:
        print(sol_parcial)
    else:
        for k in range(n):
            if valido[k]:
                sol_parcial[i] = k
                valido[k] = False
                # Las columnas nunca se ven amenazadas

                Torres(n, i + 1, sol_parcial, valido)
                sol_parcial[i] = None
                valido[k] = True


n = int(input())
Torres_Wrapper(n)
