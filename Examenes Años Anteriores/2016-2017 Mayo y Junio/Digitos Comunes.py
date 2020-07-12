def Digitos_Comunes(a):
    n = len(a)
    sol = [False] * 10
    if n == 1:
        Digitos(a[0], sol)

    else:
        sol1 = Digitos_Comunes(a[:n//2])
        sol2 = Digitos_Comunes(a[n//2:])
        Interseccion(sol1, sol2, sol)

    return sol


def Digitos(n, sol):
    if n < 10:
        sol[n] = True
    else:
        sol[n % 10] = True
        Digitos(n // 10, sol)


def Interseccion(sol1, sol2, sol):
    for i in range(10):
        if sol1[i] and sol2[i]:
            sol[i] = True


a = [2348, 1349, 7523, 3215]
print(Digitos_Comunes(a))
