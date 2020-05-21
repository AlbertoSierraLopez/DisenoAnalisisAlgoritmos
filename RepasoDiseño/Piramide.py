def Piramidion(n, m):
    if n > 0:
        Piramidion(n - 1, m)
        for i in range(m - n):
            print(" ", end='')
        for j in range(2 * n - 1):
            print("X", end='')
        for i in range(m - n):
            print(" ", end='')
        print('')


n = int(input())
Piramidion(n, n)