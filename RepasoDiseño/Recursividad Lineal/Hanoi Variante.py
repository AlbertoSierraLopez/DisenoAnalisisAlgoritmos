def Hanoi(n, O, D, A):
    if n > 0:
        Hanoi(n - 1, O, D, A)
        print("Mover", n, "de", O, "a", A)
        Hanoi(n - 1, D, O, A)
        print("Mover", n, "de", A, "a", D)
        Hanoi(n - 1, O, D, A)


n = int(input())
Hanoi(n, "Origen", "Destino", "Auxiliar")
