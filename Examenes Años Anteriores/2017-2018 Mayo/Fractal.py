import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def Fractal(n, s, p):

    if n == 1:
        Dibuja_Cuadrado(p, s)
    else:
        p11 = np.add(p, [-(2 * s), (2 * s)])
        p12 = np.add(p, [(2 * s), (2 * s)])
        p21 = np.add(p, [-(2 * s), -(2 * s)])
        p22 = np.add(p, [(2 * s), -(2 * s)])

        Fractal(n - 1, p11, s // 2)
        Fractal(n - 1, p12, s // 2)
        Fractal(n - 1, p21, s // 2)
        Fractal(n - 1, p22, s // 2)

        Dibuja_Cuadrado(p, s)


def Dibuja_Cuadrado(p, s):
    # plt.gca().add_patch(Rectangle((p[0] - s/2, p[1] - s/2), 1, 1, linewidth=0.5)) ?
    return 0


p = [0, 0]
s = 1
n = int(input())
Fractal(n, s, p)
