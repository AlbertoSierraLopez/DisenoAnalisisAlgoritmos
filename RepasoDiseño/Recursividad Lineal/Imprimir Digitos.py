def Imprimir_Izq_Der(n):
    if n < 10:
        print(n)
    else:
        Imprimir_Izq_Der(n // 10)
        print(n % 10)


def Imprimir_Der_Izq(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        Imprimir_Der_Izq(n // 10)



n = int(input())
Imprimir_Izq_Der(n)
print("####")
Imprimir_Der_Izq(n)
