import numpy as np

def Laberinto_Wrapper(M):
    n = M.shape[0]
    incrX = [0, 1, 0, -1]
    incrY = [1, 0, -1, 0]
    M_mejor = np.copy(M)
    longitud_mejor = n ** 2

    M[0, 0] = 'P'
    longitud_mejor = Laberinto(M, n - 1, 0, 0, incrX, incrY, 1, M_mejor, longitud_mejor)

    print("Pasos:", longitud_mejor)
    print(M_mejor)


def Laberinto(M, n, x, y, incrX, incrY, longitud_parcial, M_mejor, longitud_mejor):
    if x == n and y == n:
        if longitud_parcial < longitud_mejor:
            longitud_mejor = longitud_parcial
            for i in range(n + 1):
                for j in range(n + 1):
                    M_mejor[i, j] = M[i, j]
    else:
        for k in range(4):
            x += incrX[k]
            y += incrY[k]
            if x >= 0 and y >= 0 and x <= n and y <= n and M[x, y] == 'E':
                longitud_parcial += 1
                M[x, y] = 'P'

                if longitud_parcial <= longitud_mejor:
                    longitud_mejor = Laberinto(M, n, x, y, incrX, incrY, longitud_parcial, M_mejor, longitud_mejor)

                longitud_parcial -= 1
                M[x, y] = 'E'
            x -= incrX[k]
            y -= incrY[k]
    return longitud_mejor


M = np.array([['E', 'E', 'E', 'E', 'E', 'E', 'E', 'W', 'W', 'W'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'W', 'W', 'W', 'W', 'W', 'E', 'E'],
              ['E', 'E', 'E', 'W', 'W', 'W', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'W', 'W', 'W', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'W', 'E', 'E', 'E', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'W', 'W', 'W', 'W', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'W', 'E', 'E', 'W', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'W', 'E', 'E', 'W', 'E', 'E', 'E'],
              ['E', 'E', 'E', 'E', 'E', 'E', 'W', 'W', 'W', 'E']])

Laberinto_Wrapper(M)
