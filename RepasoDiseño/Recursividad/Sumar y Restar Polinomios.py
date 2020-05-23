def Sumar_Polinomios(p, q):



def Imprimir_Polinomio(a, i):
    k = len(a)
    if k == 0:
        print("0")
    elif k == 1:
        print(a[0])
    else:
        if a[0] != 0:
            if i > 1:
                print(a[0], "x^", i, " +", end=' ', sep='')
            else:
                print(a[0], "x", " +", end=' ', sep='')
        Imprimir_Polinomio(a[1:], i - 1)


a = [3, 5, 0, 2, 1]
Imprimir_Polinomio(a, len(a) - 1)
