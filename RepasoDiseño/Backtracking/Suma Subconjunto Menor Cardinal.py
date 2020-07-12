def Suma_Subconjunto_Menor_Cardinal(S, n, i, x, sol_parcial, cardinal_parcial, suma, sol_mejor, cardinal_mejor):
    if i == n:
        if suma == x and cardinal_parcial < cardinal_mejor:
            cardinal_mejor = cardinal_parcial
            for j in range(n):
                sol_mejor[j] = sol_parcial[j]
    else:
        for k in range(2):
            sol_parcial[i] = k
            cardinal_parcial += k
            suma += k * S[i]

            if suma <= x and cardinal_parcial <= cardinal_mejor:
                cardinal_mejor = Suma_Subconjunto_Menor_Cardinal(S, n, i + 1, x, sol_parcial, cardinal_parcial, suma, sol_mejor, cardinal_mejor)

            sol_parcial[i] = 0
            cardinal_parcial -= k
            suma -= k * S[i]

    return cardinal_mejor


def Suma_Subconjunto_Menor_Cardinal_Wrapper(S, x):
    n = len(S)
    sol_parcial = [0] * n
    sol_mejor = [0] * n
    cardinal_mejor = n + 1
    cardinal_mejor = Suma_Subconjunto_Menor_Cardinal(S, n, 0, x, sol_parcial, 0, 0, sol_mejor, cardinal_mejor)
    print(cardinal_mejor)
    print(sol_mejor)

S = [2, 6, 3, 5]
x = 8
Suma_Subconjunto_Menor_Cardinal_Wrapper(S, x)
