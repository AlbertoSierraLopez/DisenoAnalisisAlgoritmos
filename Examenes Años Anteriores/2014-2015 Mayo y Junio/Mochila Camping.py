# M guarda pesos, queremos maximizar el peso sin pasarnos de C
def Mochila_Camping_Wrapper(M, C):
    n = len(M)
    sol_parcial = [0] * n
    sol_mejor = [0] * n
    peso_mejor = Mochila_Camping(M, 0, C, sol_parcial, 0, sol_mejor, -1)
    print(sol_mejor)
    return peso_mejor

def Mochila_Camping(M, i, C, sol_parcial, peso_parcial, sol_mejor, peso_mejor):
    if i == len(M):
        if peso_parcial <= C and peso_parcial > peso_mejor:
            peso_mejor = peso_parcial
            for j in range(len(M)):
                sol_mejor[j] = sol_parcial[j]
    else:
        for k in range(2):
            if peso_parcial + k * M[i] <= C:
                sol_parcial[i] = k
                peso_parcial += k * M[i]

                peso_mejor = Mochila_Camping(M, i + 1, C, sol_parcial, peso_parcial, sol_mejor, peso_mejor)

                sol_parcial[i] = 0
                peso_parcial -= k * M[i]

    return peso_mejor


M = [8, 10, 12, 4, 6]
C = int(input())
print(Mochila_Camping_Wrapper(M, C))
