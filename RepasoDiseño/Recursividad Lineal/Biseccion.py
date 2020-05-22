def Biseccion(a, b, f, epsilon):    # f() es una función continua en el intervalo (a, b)
    z = (a + b) / 2
    if abs(f(z)) < epsilon:
        return z
    elif f(a) * f(z) < 0:
        return Biseccion(a, z, f, epsilon)
    else:
        return Biseccion(z, b, f, epsilon)


def f(x):
    return x * x - 2


print(Biseccion(0, 10, f, 10 ** -6))