def Suma_Subconjunto_Wrapper(L, s):
    n = len(L)
    sol_parcial = [0] * n
    sol_optima = [0] * n
    cardinal_optima = Suma_Subconjunto(L, s, 0, sol_parcial, 0, 0, sol_optima, n + 1)
    print(sol_optima)
    return cardinal_optima


def Suma_Subconjunto(L, s, i, sol_parcial, cardinal_parcial, suma_parcial, sol_optima, cardinal_optima):
    if i == len(L):
        if suma_parcial == s and cardinal_parcial < cardinal_optima:
                cardinal_optima = cardinal_parcial
                for j in range(len(L)):
                    sol_optima[j] = sol_parcial[j]
    else:
        for k in range(2):
            if (suma_parcial + k * L[i]) <= s:
                sol_parcial[i] = k
                suma_parcial += k * L[i]
                cardinal_parcial += k

                cardinal_optima = Suma_Subconjunto(L, s, i + 1, sol_parcial, cardinal_parcial, suma_parcial, sol_optima, cardinal_optima)

                sol_parcial[i] = 0
                suma_parcial -= k * L[i]
                cardinal_parcial -= k

    return cardinal_optima


L = [1, 2, 3, 5, 6, 7, 9]
s = int(input())
print(Suma_Subconjunto_Wrapper(L, s))
