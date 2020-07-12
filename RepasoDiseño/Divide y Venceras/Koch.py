import math
import numpy as np
import matplotlib.pyplot as plt

def koch_curve(p, q, n):
    if n == 0:     # The base case is just a line segment
        plt.plot([p[0, 0], q[0, 0]], [p[1, 0], q[1, 0]], 'k-')
    else:

        v = q - p
        koch_curve(p, p + v / 3, n - 1)

        R_60 = np.array([[math.cos(math.pi / 3),
                           -math.sin(math.pi / 3)],
                          [math.sin(math.pi / 3),
                           math.cos(math.pi / 3)]])

        x = p + v / 3 + R_60 * v / 3
        koch_curve(p + v / 3, x, n - 1)

        koch_curve(x, p + 2 * v / 3, n - 1)

        koch_curve(p + 2 * v / 3, q, n - 1)


def koch_snowflake(n):
    p = np.array([[0], [0]])
    q = np.array([[1], [0]])
    r = np.array([[0.5], [math.sqrt(3) / 2]])
    koch_curve(p, r, n)
    koch_curve(r, q, n)
    koch_curve(q, p, n)


fig = plt.figure()
fig.patch.set_facecolor('white')

n = int(input())
koch_snowflake(n)

plt.axis('equal')
plt.axis('off')
plt.show()