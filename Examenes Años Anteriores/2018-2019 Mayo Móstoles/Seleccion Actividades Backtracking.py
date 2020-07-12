# Problema de Subconjuntos en el que hay que devolver el mejor
def Seleccion_Actividades_Wrapper(C, F):
    n = len(C)
    sol_parcial = [0] * n
    return Seleccion_Actividades(C, F, 0, n, sol_parcial, 0, sol_parcial, -1)


def Seleccion_Actividades(C, F, i, n, sol_parcial, cardinal_parcial, mejor_sol, mejor_cardinal):
    if i == n:
        if cardinal_parcial > mejor_cardinal:
            for j in range(0, len(sol_parcial)):
                mejor_sol[j] = sol_parcial[j]
    else:
        for k in range(2):
            if k == 0 or Valido(C, F, i, sol_parcial):
                sol_parcial[i] = k
                cardinal_parcial = cardinal_parcial + k

                mejor_sol = Seleccion_Actividades(C, F, i + 1, n, sol_parcial, cardinal_parcial, mejor_sol, mejor_cardinal)

    return mejor_sol


def Valido(C, F, i, sol_parcial):
    ok = True
    j = 0
    while j < len(C) and ok:
        if sol_parcial[j]:
            ok = (F[i] <= C[j]) or (C[i] >= F[j])
        j = j + 1
    return ok


C = [1, 2, 0, 5, 8, 5, 6, 8, 3, 3, 12]
F = [4, 13, 6, 7, 12, 9, 10, 11, 8, 5, 14]
print(Seleccion_Actividades_Wrapper(C, F))
