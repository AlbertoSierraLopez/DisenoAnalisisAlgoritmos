def Dividir_Wrapper(S):
    n = len(S)
    suma_max = sum(S)
    suma_max = suma_max // 2
    A = [0] * n
    B = [0] * n
    Dividir(S, n, 0, A, B, 0, 0, suma_max)


def Dividir(S, n, i, A, B, suma_A, suma_B, suma_max):
    if i == n:
        if suma_A == suma_B:
            print("A:", A, "\nB:", B, "\n")
    else:
        for k in range(2):

            A[i] = k
            B[i] = (1 - k)

            suma_A += k * S[i]
            suma_B += (1 - k) * S[i]

            if suma_A <= suma_max and suma_B <= suma_max:
                Dividir(S, n, i + 1, A, B, suma_A, suma_B, suma_max)

            A[i] = 0
            B[i] = 0

            suma_A -= k * S[i]
            suma_B -= (1 - k) * S[i]


S = [1, 2, 3, 4, 5, 9]
Dividir_Wrapper(S)
