def newton_raphson(x, x0, epsilon):
    if abs(f(x, x0)) < epsilon:
        return x
    else:
        xn = x - f(x, x0) / fd(x)
        return newton_raphson(xn, x0, epsilon)


def f(x, x0):
    return (x * x) - x0


def fd(x):
    return x + x


n = float(input())
n_r = newton_raphson(n, n, 10**-6)
print('%.4f' % n_r)
