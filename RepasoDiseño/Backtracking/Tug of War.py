# Ejercicio 12.7
def Tug_of_War_Wrapper(T):
    n = len(T)
    s = sum(T)
    sol_parcial = [0] * n
    sol_mejor = [0] * n
    diferencia_mejor = Tug_of_War(T, n, s, 0, 0, sol_parcial, 0, s, sol_mejor, s)
    print("conjunto", T)
    print("solución", sol_mejor)
    print("diferencia", diferencia_mejor)
    return 0


def Tug_of_War(T, n, s, i, num_elem, sol_parcial, suma_parcial, diferencia_parcial, sol_mejor, diferencia_mejor):
    if i == n:
        if num_elem == n // 2 and diferencia_parcial < diferencia_mejor:
            diferencia_mejor = diferencia_parcial
            for j in range(n):
                sol_mejor[j] = sol_parcial[j]
    else:
        for k in range(2):
            num_elem += k
            sol_parcial[i] = k
            suma_parcial += k * T[i]
            diferencia_previa = diferencia_parcial
            diferencia_parcial = abs(s - suma_parcial * 2)

            if num_elem <= n // 2:
                diferencia_mejor = Tug_of_War(T, n, s, i + 1, num_elem, sol_parcial, suma_parcial, diferencia_parcial, sol_mejor, diferencia_mejor)

            num_elem -= k
            sol_parcial[i] = 0
            suma_parcial -= k * T[i]
            diferencia_parcial = diferencia_previa

    return diferencia_mejor


T = [3, 5, 9, 14, 20, 24]
Tug_of_War_Wrapper(T)
